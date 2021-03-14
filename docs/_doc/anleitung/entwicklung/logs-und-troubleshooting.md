---
title: Logs und Troubleshooting
sections:
  - Alice Watch und Systemlogs
  - MQTT Clients
  - ASR und Speech-to-text umgehen
  - Dialogue View
---

Das Webinterface bietet mit Alice Watch und integrierten Systemlogs Möglichkeiten um mitzuverfolgen was im Hintergrund geschieht. Bei der Beta 4 wird die Weboberfläche jedoch bei einigen Prozessen blockiert wie zum Beispiel dem Trainieren der NLU. In diesem Fall kann man nur mithilfe der Kommandozeile mitverfolgen was im Hintergrund geschieht. Außerdem kann man ältere Logs auch nur per Kommandozeile einsehen.

Das Kommando lautet:
```
tail -f /var/log/syslog
```

### Alice Watch und Systemlogs

Um in Echtzeit mitzuverfolgen was im Hintergrund geschieht reicht in den meisten Fällen jedoch Alice Watch und die Systemlogs der Weboberfäche.

Bilder, Heat Levels usw

### MQTT Clients

Um die Kommunikation zwischen den Komponenten (Hermes Protokoll), ProjectAlice Events usw. und Zigbee2MQTT mitzuverfolgen kann man einen MQTT Client nutzen und die gewünschten Topics subscriben.

Um alle Hermes-Topics zu subscriben nutzt man:
```
hermes/#
```

MQTT.fx ist ein empfehlenswerter grafischer MQTT-Client:

![MQTTfx](assets/images/mqttfx.png){: style="margin: 0 auto;margin-top: 0.35em;max-width:700px;width:100%"}

Eine Liste weiterer Topics findet man [hier](topic-uebersicht.html).

### ASR und Speech-to-text umgehen

Falls die ASR nicht zuverlässig funktioniert kann das Erkennen des richtigen Texts simuliert werden. Entweder per MQTT Publish oder bei Beta 4 mit einem Skill/Widget, welches man nachinstallieren kann.

Auch wenn die Audioausgabe nicht funktioniert gibt es ein Widget, das Abhilfe leistet.

Folgende Widgets installiert man dafür:
- SpeechVisualisier
- TextInputWidget

TextInputWidget unterstützt jedoch keine Dialoge. Falls der Intent weitere Eingaben erfordert, ist das Widget nicht geeignet.

### Dialogue View

Ab Alice Beta 5 gibt es mit der Dialogue View eine Lösung, die keine weitere Widgets benötigt und Dialoge unterstützt. 