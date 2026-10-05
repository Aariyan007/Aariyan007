"""Render a self-hosted contribution activity graph as an SVG.

Fetches the last 31 days of contributions through the GitHub GraphQL API and
draws a glowing area chart in the profile's orange-on-black theme. Running it
inside GitHub Actions removes the dependency on third-party image hosts that
rate-limit or go offline.
"""
import datetime as dt
import json
import os
import sys
import urllib.request

USER = os.environ.get("GH_USER", "Aariyan007")
TOKEN = os.environ.get("GH_TOKEN", "")
OUT = sys.argv[1] if len(sys.argv) > 1 else "dist/activity-graph.svg"

QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def fetch_days():
    now = dt.datetime.now(dt.timezone.utc)
    body = json.dumps({
        "query": QUERY,
        "variables": {
            "login": USER,
            "from": (now - dt.timedelta(days=30)).strftime("%Y-%m-%dT00:00:00Z"),
            "to": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
    }).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    if "errors" in data:
        raise SystemExit(f"GraphQL error: {data['errors']}")
    weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    return days[-31:]


def render(days):
    w, h = 900, 300
    pl, pr, pt, pb = 52, 28, 62, 44
    cw, ch = w - pl - pr, h - pt - pb
    counts = [d["contributionCount"] for d in days]
    total, peak = sum(counts), max(counts + [1])
    top = max(peak, 4)
    n = max(len(days) - 1, 1)

    pts = [(pl + cw * i / n, pt + ch - ch * c / top) for i, c in enumerate(counts)]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = f"{pl},{pt + ch} {line} {pl + cw},{pt + ch}"

    grid = "".join(
        f'<line x1="{pl}" x2="{w - pr}" y1="{pt + ch * k / 4:.1f}" y2="{pt + ch * k / 4:.1f}" '
        f'stroke="#2a1a0a" stroke-dasharray="4 6"/>'
        f'<text x="{pl - 10}" y="{pt + ch * k / 4 + 4:.1f}" text-anchor="end" fill="#8a6a45" '
        f'font-size="11">{round(top * (4 - k) / 4)}</text>'
        for k in range(5)
    )
    labels = "".join(
        f'<text x="{pts[i][0]:.1f}" y="{h - 16}" text-anchor="middle" fill="#8a6a45" font-size="11">'
        f'{dt.date.fromisoformat(days[i]["date"]).strftime("%b %d").replace(" 0", " ")}</text>'
        for i in range(0, len(days), 5)
    )
    dots = "".join(
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5 if c == peak and c else 3}" '
        f'fill="{"#ffb347" if c == peak and c else "#ff6d00"}"><title>{d["date"]}: {c}</title></circle>'
        for (x, y), c, d in zip(pts, counts, days)
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="'JetBrains Mono',Menlo,Consolas,monospace">
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0a0a0a"/><stop offset="1" stop-color="#1a0a00"/></linearGradient>
  <linearGradient id="fill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff6d00" stop-opacity=".55"/><stop offset="1" stop-color="#ff4500" stop-opacity="0"/></linearGradient>
  <filter id="glow" x="-5%" y="-20%" width="110%" height="140%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect width="{w}" height="{h}" rx="14" fill="url(#bg)" stroke="#3a1c00"/>
<text x="{pl}" y="34" fill="#ff6d00" font-size="16" font-weight="700">&gt; {USER} / contribution_activity</text>
<text x="{w - pr}" y="34" text-anchor="end" fill="#ffb347" font-size="12">{total} contributions · peak {peak}/day · last 31 days</text>
{grid}
<polygon points="{area}" fill="url(#fill)"/>
<polyline points="{line}" fill="none" stroke="#ff4500" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" filter="url(#glow)"/>
{dots}
{labels}
</svg>
"""


if __name__ == "__main__":
    os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(fetch_days()))
    print(f"wrote {OUT}")
