<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F1A24,35:1E3A4C,70:2F6F7E,100:88C0D0&height=260&section=header&text=Aariyan%20Sunu&fontSize=70&fontColor=ECEFF4&fontAlignY=36&animation=fadeIn&desc=Backend%20Engineer%20%C2%B7%20AI%20Systems%20Builder%20%C2%B7%20Problem%20Solver&descSize=19&descAlignY=56&descColor=A9D6E5" width="100%"/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=19&duration=4200&pause=1600&color=88C0D0&center=true&vCenter=true&width=760&lines=I+build+intelligent+systems.;Backend+engineering+%2B+AI+microservices.;Real-time+routing+%26+simulation+engines.;Voice+AI+%C2%B7+hardware+%C2%B7+distributed+systems.)](https://git.io/typing-svg)

<img src="https://komarev.com/ghpvc/?username=aariyan007&label=profile+views&color=2F6F7E&style=for-the-badge&labelColor=0F1A24" />
<img src="https://img.shields.io/github/followers/aariyan007?label=followers&style=for-the-badge&color=2F6F7E&labelColor=0F1A24" />
<img src="https://img.shields.io/badge/now-building_Jarvis-88C0D0?style=for-the-badge&labelColor=0F1A24" />

</div>

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=soft&color=0:0F1A24,100:1E3A4C&height=48&text=~%2F%20about&fontSize=18&fontColor=88C0D0&fontAlignY=62" />

</div>

<table>
<tr>
<td width="55%" valign="top">

```yaml
name:      Aariyan Sunu
location:  Kerala, India
degree:    BTech CSE · 7th Sem · MITS · KTU
role:      Backend Engineer + AI Systems Builder
mindset:   "I think in systems, not websites."

currently:
  - Jarvis           # voice AI assistant
  - Emergency Sim    # real-time ambulance routing
  - ESP32 wearable   # hardware terminal for Jarvis
  - Pothole CV       # road-damage microservice

open_to:   internships · collabs
```

</td>
<td width="45%" align="center" valign="middle">

<img src="https://images.weserv.nl/?url=https://raw.githubusercontent.com/devSouvik/devSouvik/master/gif3.gif" width="320" alt="coding"/>

<br/>

```console
aariyan@mits:~$ uptime
 systems online · shipping steadily
```

</td>
</tr>
</table>

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=soft&color=0:0F1A24,100:1E3A4C&height=48&text=~%2F%20projects&fontSize=18&fontColor=88C0D0&fontAlignY=62" />

</div>

<table>
<tr>
<td colspan="2">

### 🎙️ &nbsp;Jarvis — Voice AI Assistant
<sub>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Local-first voice OS replacing the keyboard entirely</sub>

</td>
</tr>
<tr>
<td width="58%" valign="top">

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#1E3A4C','primaryTextColor':'#ECEFF4','primaryBorderColor':'#88C0D0','lineColor':'#5E81AC','fontFamily':'monospace'}}}%%
flowchart LR
    A([Wake Word]) --> B[Voice Auth]
    B --> C[Whisper STT]
    C --> D{Cache hit?}
    D -- yes --> G
    D -- no --> E[Gemini Router]
    E --> F[ReAct Agent]
    F --> G[ElevenLabs TTS]
    G --> H([HUD])
```

- Porcupine wake word + ECAPA-TDNN speaker verification
- Gemini 1.5 Flash intent router, sub-100ms on 50 cached commands
- ReAct multi-step agent, up to 5 chained planning steps
- Mood-based ElevenLabs TTS (happy / focused / tired)
- Iron Man–style HUD: radar, arc reactor, biometrics panels
- ESP32 wearable terminal over WiFi via ngrok + Flask

</td>
<td width="42%" valign="top" align="center">

<br/>

<img src="https://img.shields.io/badge/ACTIVE_DEV-88C0D0?style=for-the-badge&labelColor=0F1A24"/>

<br/><br/>

<img src="https://skillicons.dev/icons?i=py,react,flask&theme=dark" />

<br/>

<img src="https://img.shields.io/badge/Gemini-1E3A4C?style=flat-square&logo=google&logoColor=88C0D0"/>
<img src="https://img.shields.io/badge/Whisper-1E3A4C?style=flat-square&logo=openai&logoColor=88C0D0"/>
<img src="https://img.shields.io/badge/ElevenLabs-1E3A4C?style=flat-square&logoColor=88C0D0"/>
<img src="https://img.shields.io/badge/ESP32-1E3A4C?style=flat-square&logo=espressif&logoColor=88C0D0"/>

<br/><br/>

[![repo](https://img.shields.io/badge/View_Repo-THEFriend-2F6F7E?style=for-the-badge&logo=github&logoColor=ECEFF4&labelColor=0F1A24)](https://github.com/Aariyan007/THEFriend)

</td>
</tr>
</table>

<table>
<tr>
<td width="33%" valign="top">

#### 🚑 Emergency Response Sim
<sub>Real-time ambulance routing + live ETA</sub>

- React + Leaflet live map
- WebSocket sync across all clients
- Online-learning ETA per dispatch
- Dynamic shortest-path routing
- Per-incident dispatch dashboard

<img src="https://img.shields.io/badge/BUILDING-5E81AC?style=flat-square&labelColor=0F1A24"/>

<img src="https://skillicons.dev/icons?i=react,nodejs,mongodb&theme=dark" height="34"/>

</td>
<td width="33%" valign="top">

#### 🛣️ AI Pothole Detection
<sub>CV microservice for smart cities</sub>

- MobileNetV2 fine-tuned on road damage
- FastAPI, **< 200ms** per image
- Returns `{severity, confidence, bounding_region}`
- Batch inference support
- Drop-in for city pipelines

<img src="https://img.shields.io/badge/COMPLETE-A3BE8C?style=flat-square&labelColor=0F1A24"/>

<img src="https://skillicons.dev/icons?i=py,fastapi,tensorflow,opencv&theme=dark" height="34"/>

</td>
<td width="33%" valign="top">

#### 📡 Log Ingestion Platform
<sub>Observability stack from scratch</sub>

- npm-ready Node.js logger
- Full-text search across services
- Error-spike email alerting
- Multi-service log streams
- Filter by service / level / time

<img src="https://img.shields.io/badge/COMPLETE-A3BE8C?style=flat-square&labelColor=0F1A24"/>

<img src="https://skillicons.dev/icons?i=nodejs,express,mongodb&theme=dark" height="34"/>

</td>
</tr>
</table>

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=soft&color=0:0F1A24,100:1E3A4C&height=48&text=~%2F%20stack&fontSize=18&fontColor=88C0D0&fontAlignY=62" />

<br/><br/>

<table>
<tr><td align="right"><sub><b>LANGUAGES</b></sub></td><td><img src="https://skillicons.dev/icons?i=java,js,ts,py,rust&theme=dark" /></td></tr>
<tr><td align="right"><sub><b>BACKEND</b></sub></td><td><img src="https://skillicons.dev/icons?i=spring,nodejs,express,fastapi,flask&theme=dark" /></td></tr>
<tr><td align="right"><sub><b>FRONTEND</b></sub></td><td><img src="https://skillicons.dev/icons?i=react,nextjs,vite,tailwind&theme=dark" /></td></tr>
<tr><td align="right"><sub><b>DATA</b></sub></td><td><img src="https://skillicons.dev/icons?i=mongodb,firebase&theme=dark" /></td></tr>
<tr><td align="right"><sub><b>AI / ML</b></sub></td><td><img src="https://skillicons.dev/icons?i=tensorflow,opencv&theme=dark" /> &nbsp;<img src="https://img.shields.io/badge/Gemini-1E3A4C?style=flat-square&logo=google&logoColor=88C0D0"/> <img src="https://img.shields.io/badge/Whisper-1E3A4C?style=flat-square&logo=openai&logoColor=88C0D0"/> <img src="https://img.shields.io/badge/ElevenLabs-1E3A4C?style=flat-square&logoColor=88C0D0"/></td></tr>
<tr><td align="right"><sub><b>TOOLS</b></sub></td><td><img src="https://skillicons.dev/icons?i=git,linux,docker,postman&theme=dark" /> &nbsp;<img src="https://img.shields.io/badge/ESP32-1E3A4C?style=flat-square&logo=espressif&logoColor=88C0D0"/> <img src="https://img.shields.io/badge/ngrok-1E3A4C?style=flat-square&logo=ngrok&logoColor=88C0D0"/></td></tr>
</table>

</div>

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=soft&color=0:0F1A24,100:1E3A4C&height=48&text=~%2F%20activity&fontSize=18&fontColor=88C0D0&fontAlignY=62" />

<br/><br/>

<img height="170" src="https://github-readme-stats.vercel.app/api?username=aariyan007&show_icons=true&count_private=true&hide_border=true&bg_color=0F1A24&title_color=88C0D0&icon_color=5E81AC&text_color=D8DEE9&ring_color=88C0D0"/>
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?username=aariyan007&layout=compact&hide_border=true&bg_color=0F1A24&title_color=88C0D0&text_color=D8DEE9"/>

<img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=aariyan007&bg_color=0F1A24&color=D8DEE9&line=88C0D0&point=ECEFF4&area=true&area_color=2F6F7E&hide_border=true&title_color=88C0D0"/>

<img width="100%" src="https://raw.githubusercontent.com/Aariyan007/Aariyan007/output/contribution-heatmap.svg"/>

</div>

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=soft&color=0:0F1A24,100:1E3A4C&height=48&text=~%2F%20next&fontSize=18&fontColor=88C0D0&fontAlignY=62" />

<br/><br/>

<sub><b>JARVIS MODULES</b></sub>

<img src="https://img.shields.io/badge/Screen_Vision-planned-1E3A4C?style=flat-square&labelColor=0F1A24"/>
<img src="https://img.shields.io/badge/Face_%26_Emotion-planned-1E3A4C?style=flat-square&labelColor=0F1A24"/>
<img src="https://img.shields.io/badge/Voice_to_Website-planned-1E3A4C?style=flat-square&labelColor=0F1A24"/>
<img src="https://img.shields.io/badge/Code_Assistant-planned-1E3A4C?style=flat-square&labelColor=0F1A24"/>
<img src="https://img.shields.io/badge/Music_Control-planned-1E3A4C?style=flat-square&labelColor=0F1A24"/>
<img src="https://img.shields.io/badge/Ollama_Local_LLM-planned-1E3A4C?style=flat-square&labelColor=0F1A24"/>
<img src="https://img.shields.io/badge/Notes_%26_Todo-planned-1E3A4C?style=flat-square&labelColor=0F1A24"/>
<img src="https://img.shields.io/badge/Proactive_Mode-planned-1E3A4C?style=flat-square&labelColor=0F1A24"/>

<br/><br/>

<sub><b>ML ROADMAP</b></sub>

<img src="https://img.shields.io/badge/Whisper_Fine--tune-WER_12%25_→_3%25-2F6F7E?style=flat-square&labelColor=0F1A24"/>
<img src="https://img.shields.io/badge/Habit_LSTM-next--action_prediction-2F6F7E?style=flat-square&labelColor=0F1A24"/>
<img src="https://img.shields.io/badge/Vector_Memory-ChromaDB_%2F_FAISS-2F6F7E?style=flat-square&labelColor=0F1A24"/>

</div>

<br/>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0F1A24?style=for-the-badge&logo=linkedin&logoColor=88C0D0)](https://www.linkedin.com/in/aariyan-sunu)
[![Gmail](https://img.shields.io/badge/Email-0F1A24?style=for-the-badge&logo=gmail&logoColor=88C0D0)](mailto:aariyansunu28@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-0F1A24?style=for-the-badge&logo=github&logoColor=88C0D0)](https://github.com/aariyan007)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=15&duration=4500&pause=2000&color=A9D6E5&center=true&vCenter=true&width=640&lines=%22I+think+in+systems%2C+not+just+websites.%22;Let%27s+build+something+that+matters.)](https://git.io/typing-svg)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:88C0D0,30:2F6F7E,65:1E3A4C,100:0F1A24&height=150&section=footer&text=thanks%20for%20stopping%20by&fontSize=22&fontColor=ECEFF4&fontAlignY=72" width="100%"/>

</div>
