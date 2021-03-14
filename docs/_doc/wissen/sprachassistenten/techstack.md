---
title: Techstack eines Sprachassistenten
sections:
  - Wake word detection
  - Speech-to-text
  - Intent recognition
  - Intent handling
  - Text-to-speech
  - Dialog manager
  - Weitere Technologie
---

Ein Sprachassistent ist aus mehreren Softwarekomponenten zusammengesetzt. Die Softwarekomponenten, die einen Sprachassistenten ausmachen sind folgende:

- Wake word detection
- Speech-to-text (ASR)
- Intent recognition (NLU)
- Intent handling
- Text-to-speech (TTS)
- Dialog manager

### Wake word detection

Vor jeder Bedienung muss der Sprachassistent erst einmal mittels "Wake Word" (auch als hotword bekannt) aktiviert werden. Sobald das Wort erkannt wurde, wartet der Assistent für eine bestimmte Zeit auf Anweisungen.

Bekannte Beispiel für Wake-words sind "Okay Google" für den Google Assistant und "Hey Siri".

Es gibt u.a. folgende Wake-word-engines:

- Porcupine (Alice, Rhasspy)
- Snips (Alice)
- Snowboy (Rhasspy)
- Mycroft Precise (Alice, Rhasspy)
- Rhasspy Raven (Rhasspy)
- Pocketsphinx (Rhasspy)

### Speech-to-text

Nach der Aktivierung durch die Wake-word-engine nimmt der Sprachassistent das Gesagte für eine bestimmte Zeit (ASR timeout) auf und wandelt es in Text um. Dabei gibt es mehrere Teilergebnisse und ein finales Endergebnis. Dafür ist Automatic-Speech-Recognition (ASR) bzw. Speech-to-Text (STT) verantwortlich.

Die Spracherkennung basiert auf Machine Learning Modellen. Es können entweder vorgefertigte Modelle genutzt werden (pre-trained models), die mit einer Liste von gebräuchlichen Wörtern trainiert sind oder selbst trainierte Modelle, die man mit den Befehlen trainiert, die man vom Nutzer erwartet. Letzteres verbessertet die Texterkennung, vermindert jedoch zur gleichen Zeit die Flexibilität des Systems.

Hierfür gibt es u.a. folgende Engines:

- Pocketsphinx (Alice, Rhasspy)
- Kaldi (Rhasspy)
- DeepSpeech (Alice, Rhasspy)
- Snips (Alice)
- Google (proprietär, Alice)

### Intent recognition

Nachdem das Gesprochene durch das Speech-to-Text System in Text umgewandelt worden ist, muss als nächstes erkannt werden welchen der verfügbaren Aufgaben (Intents) der Nutzer mit seiner Anweisung beabsichtigt. Die NLU gibt außerdem an wie wahrscheinlich der gefundene Intent ist (max 1.0). Neben der Erkennung des Intents wird außerdem die im Befehl enthaltenen Variablen (Slots), wie z.B. Zahlen, Zustände, Orte und Objekte erkannt.

Diese Komponente nennt man Intent recognition oder Natural Language Understanding (NLU).

Nehmen wir an die ASR hat folgende Eingabesatz in Text umgewandelt:

<blockquote class="blockquote">
  <p class="mb-0">Wie wird das Wetter um 9 Uhr in Paris?</p>
</blockquote>

Eine gut-trainierte NLU erzeugt daraus beispielsweise folgenden strukturierten Datensatz:
<pre>
{
   "intent": {
      "intentName": "searchWeatherForecast",
      "probability": 0.95
   },
   "slots": [
      {
         "value": "paris",
         "entity": "locality",
         "slotName": "forecast_locality"
      },
      {
         "value": {
            "kind": "InstantTime",
            "value": "2018-02-08 20:00:00 +00:00"
         },
         "entity": "snips/datetime",
         "slotName": "forecast_start_datetime"
      }
   ]
}
</pre>

NLUs werden mithilfe verschiedener Ansätze realisiert. Die meisten davon verwenden eine KI (bspw. Neuronales Netzwerk) um Intent und Slots zu erkennen. Eine große Anzahl an verschiedenen Slots kann den Arbeitsaufwand beim Trainieren erhöhen. NLUs unterscheiden sich je nach Ansatz in Ihrer Flexibilität, Trainingsdauer, Erkennungsdauer und idealen Anzahl an Sätzen. Eine gute Übersicht findet man auf der [Dokumentation von Rhasspy][RHASPY-NLU] von der wir folgende Tabelle entnommen haben:

[RHASPY-NLU]: https://rhasspy.readthedocs.io/en/latest/intent-recognition/

<link rel="stylesheet" type="text/css" href="/assets/css/index.css">

<table style="width:100%">
<colgroup>
<col width="10%" />
<col width="15%" />
<col width="15%" />
<col width="15%" />
<col width="20%" />
<col width="15%" />
<col width="5%" />
<col width="5%" />
</colgroup>
<thead>
<tr class="header" >
<th>NLU</th>
<th>Ideale Anzahl an Sätzen</th>
<th>Trainingsdauer</th>
<th>Erkennungsdauer</th>
<th>Flexibilität</th>
<th>Lizenz</th>
<th>Alice</th>
<th>Rhasspy</th>
</tr>
</thead>
<tbody>
<tr>
<td>Snips</td>
<td>1K-100K</td>
<td>moderat</td>
<td>sehr schnell</td>
<td>erfasst unbekannte Wörter/Einheiten</td>
<td>Apache 2 Lizenz</td>
<td>✗</td>
<td>✗</td>
</tr>
<tr>
<td>Fsticuffs</td>
<td>1M+</td>
<td>sehr schnell</td>
<td>sehr schnell</td>
<td>ignoriert unbekannte Wörter</td>
<td>–</td>
<td></td>
<td>✗</td>
</tr>
<tr>
<td>Fuzzywuzzy</td>
<td>100-1K</td>
<td>schnell</td>
<td>sehr schnell</td>
<td>erlaubt fuzzy string matching</td>
<td>GPL 2.0 Lizenz</td>
<td></td>
<td>✗</td>
</tr>
<tr>
<td>RasaNLU</td>
<td>1K-100K</td>
<td>sehr langsam</td>
<td>moderat</td>
<td>erfasst unbekannte Wörter</td>
<td>Apache 2 Lizenz</td>
<td></td>
<td>✗</td>
</tr>
<tr>
<td>Mycroft Adapt</td>
<td>100-1K</td>
<td>moderat</td>
<td>schnell</td>
<td>ignoriert unbekannte Wörter</td>
<td>–</td>
<td></td>
<td>✗</td>
</tr>
<tr>
<td>Flair</td>
<td>1K-100K</td>
<td>sehr langsam</td>
<td>moderat</td>
<td>erfasst unbekannte Wörter</td>
<td>–</td>
<td></td>
<td>✗</td>
</tr>
</tbody>
</table>

### Intent handling

Nachdem der Intent erkannt ist, kommt Intenthandling ins Spiel. Hier wird der eigentliche Befehl ausgeführt und dem Nutzer bei Bedarf geantwortet.

- Mit Hermes Protokoll kompatible Services
- Home Assistant und [Hass.io](http://Hass.io)
- Node red / Scenarios
- Skills

### Text-to-speech

Bei Bedarf antwortet der Assistent dem Nutzer mit einem vom Intenthandler bestimmten Text. Dafür ist eine Text-to-Speech (TTS) Engine nötig.

Folgende Text-to-Speech-Engines stehen zur Auswahl:

- Espeak (Rhasspy)
- PicoTTS (Alice, Rhasspy)
- Mycroft Mimic (Alice)
- NanoTTS (Rhasspy)
- MaryTTS (Rhasspy)
- OpenTTS (Rhasspy)
- Wavenet (Rhasspy)
- Amazon Polly (proprietär, Alice)
- Google Wavenet (proprietär, Alice)
- IBM Watson (proprietär, Alice)

### Dialog manager

Der Dialog Manager verwaltet eine Sitzung, die durch ein erkanntes Wakeword oder einem manuellen `startSession` initiiert wird und koordiniert ASR, NLU und TTS bis ein Intent durchgeführt oder abgebrochen ist. Wenn nachdem der Intent erkannt worden ist weitere Eingaben des Nutzers erforderlich sind, kann die Sitzung verlängert werden. Es kann nur eine Sitzung zu einer Zeit geben. Wenn zeitgleich weitere Sitzungen erstellt werden, landen diese erst einmal in einer Warteschlange.

### Weitere Technologie

Der vorgestellte Techstack enthält nur die wesentlichen Komponenten eines Sprachassistenten.

Die Technologie für die Kommunikation zwischen den Komponenten fehlt jedoch zum Beispiel. Rhasspy und Alice verwenden dafür das von Snips entwickelte Hermes Protokoll in Kombination mit einem MQTT Broker. Hier wird überwiegend Mosquitto von Eclipse eingesetzt. MQTT setzt nicht auf das etablierte Client/Server-Modellen sondern verwendet das Publish/Subscribe-Modell. Bei MQTT gibt es einen Broker, der es erlaubt für ein bestimmtes Topic eine Nachricht zu publishen oder ein bestimmtes Topic zu subscriben um alle Nachrichten zu erhalten, die zu diesem Topic veröffentlicht werden.

Für den Bereich SmartHome ist außerdem das ZigBee-Protokoll wichtig, welches mit auch mit MQTT angesprochen werden kann mithilfe von ZigBee2MQTT.

Für mehr Informationen zu dem Thema bitte [Weitere Technologie](/wissen-weitere-technologie.html) anschauen.