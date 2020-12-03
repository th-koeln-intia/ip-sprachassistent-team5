---
title: Bezug zum Projekt
sections:
  - Snips Hermes Protokoll
  - Hermes Topics
  - Alice Topics
---

Rhasspy und Alice nutzen beide MQTT für die interne Kommunikation zwischen den verschiedenen Komponenten des Techstacks. MQTT als Protokoll allein reicht jedoch nicht, da es ein reines Kommunikationsprotokoll ohne Anwendungslogik ist.

Aus diesem Grund implementieren beide das [Hermes Protokoll von Snips][SNIPS_HERMES], das genau für den Anwendungsfall der Sprachsteuerung entwickelt worden ist und sich bewährt hat. Es bietet primär Schnittstellen für die Kommunikation zwischen den einzelnen Komponenten.

Im Folgenden geben wir einen kurzen Einblick in das Hermes Protokoll inklusive der relevanten Topics. Neben den Topics von Hermes hat Alice auch eigene Topics auf die wir eingehen werden.

[SNIPS_HERMES]: https://docs.snips.ai/reference/hermes

### Snips Hermes Protokoll

Hermes nutzt das MQTT-Protokoll zum Ausstausch von Nachrichten und spezifiziert in Form von Topics Schnittstellen für die einzelnen Komponenten. Darüber hinaus bestimmt es den gesamten Ablauf des Sprachsteuerungsprozesses: von der Aufnahme des Tons, dem Erkennen des Wakewords bis zur Erkennung und Ausführung des Intents, der Dialogführung und dem Sprachfeedback an den Nutzer.

###### Anwendungsschicht

MQTT baut meist auf TCP (Ausnahme: MQTT-SN) auf und befindet sich daher im TCP/IP-Modell auf der letzten Schicht: der Anwendungsschicht.

Da es aber den TCP/IP-Protokollstack außschließlich um weitere Funktionalität erweitert und im Gegensatz zu den gängigen Protokollen der Anwendungsschicht wie z.B. HTTP keine eigene Anwendungslogik festlegt bzw. kein festgelegtes Format für publizierte Nachrichten hat, muss das MQTT-Protokoll sozusagen um eine Schicht erweitert werden.

Das Hermes Protokoll von Snips macht genau das, es baut auf MQTT auf und definiert eine eigene Anwendungslogik.

###### Format der Nachricht

Nachrichten, die mit dem Hermes Protokoll versendet werden sind falls sie Informationen enthalten, immer im JSON-Format. Ausgenommen hier sind natürlich Nachrichten die ihren Payload nicht nutzen und Audioframes, die im WAV-Format versendet werden.

Beispiel einer Nachricht:
```
{
  "siteId" : "626b9eb0-b26d-4b0b-ab30-332c679b3012"
}
```

Jede Nachricht enthält mindestends das Feld `siteId` welches den Adressaten der Nachricht in Form einer UUID angibt.

Dies ist wichtig wenn es mehrere Geräte gibt, die miteinander interagieren. Mit `default` lässt sich das aktuelle Gerät angeben ohne die UUID zu wissen. Die UUID wird beim Systemstart erzeugt und verändert sich während der Laufzeit nicht.

Ein anderes wichtiges Feld das fast genauso oft vorkommt ist die `sessionId`. Sie wird vom Dialog Manager beim Erstellen einer neuen Session erzeugt. Dies erfolgt nachdem das Wakeword erkannt worden ist oder eine Session manuell durch eine Nachricht an das Topic `hermes/dialogueManager/startSession` erzeugt wird.


###### Sprachsteuerung und das Zusammenspiel der Komponenten

Wie bereits erwähnt bestimmt Hermes nicht nur Schnittstellen für die Kommunikation sondern auch ganz genau den Ablauf des Sprachsteuerungprozesses und wie die einzelnen Komponenten miteinander interagieren. Im Folgenden eine etwas vereinfachte Darstellung in 9 Schritten (es fehlt u.a. dialogueManager/sessionStarted):

![Hermes Message Flow](assets/images/hermes-flow.png){: .img-responsive}

### Hermes Topics

Hermes-spezifische Topics haben alle ein `hermes` als Bezeichner des ersten Topic-Levels und lassen sich dadurch leicht erkennen. Das zweite Topic-Level beschreibt immer die zuständige Komponente. 

Eine vollständige Übersicht der API (Topics inkl. Felder) erhält man [hier][SNIPS_HERMES] und [hier][SNIPS_HERMES_DIALOG].

[SNIPS_HERMES_DIALOG]: https://docs.snips.ai/reference/dialogue

### Alice Topics

Alice-spezifische Topics haben `projectalice` als Bezeichner des ersten Topic-Levels und im zweiten Topic-Level gibt es `events` und `logging`.
