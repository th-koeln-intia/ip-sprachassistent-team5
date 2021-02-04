---
title: Message Queuing Telemetry Transport
sections:
  - Geschichte
  - Weiterentwicklung und Standardisierung
  - Zentrale Rolle des Brokers
  - Publish-Subscribe-Messaging-Muster
  - Topics
  - Topic-Filter
  - MQTT Control Packet
  - Quality-of-Service
  - Retained Messages
  - Weitere Themen
  - Bezug zum Projekt
  - Implementationen
---

Das **Message Queuing Telemetry Transport**, kurz MQTT, ist ein offenes Telemetrieprotokoll, das auf TCP/IP aufbaut und ursprünglich für Industriesteuerungen entwickelt worden ist aber aufgrund seiner Zuverlässigkeit und seines sparsamen Umgangs mit Bandbreite und Ressourcen sich auch für den Bereich Internet of Things und Hausautomation eignet, da hier teilweise auch schwächere RISC-Mikroprozessoren zum Einsatz kommen und eine effiziente Datenübertragung daher essentiell ist.

### Geschichte

Das Protokoll wurde 1999 von Andy Stanford-Clark (IBM) und Arlen Nipper (Arcom, jetzt Cirrus Link) entwickelt um eine Öl-Pipeline über eine Satelliten-Verbindung in der Wüste zu überwachen. Sie waren damals mit dem Problem konfrontiert, verschiedene Messstellen entlang der Öl-Pipeline durch die Wüste an ein Leitsystem anzubinden. Die zu der Zeit üblichen Protokolle konnten einige der Herausforderungen dieses Projekts nicht abdecken. Unter anderem sollte die vorhandene Bandbreite sehr effizient genutzt werden und dabei wenig Energie verbraucht werden.

### Weiterentwicklung und Standardisierung

Seit 1999 hat sich MQTT weiterentwickelt und ist mitterweile bei der Version 3.1.1 angelangt. Es ist außerdem offizieller OASIS und ISO Standard (ISO/IEC 20922:2016) und es wurde bereits 2018 mit MQTT 5 ein Nachfolger spezifiziert. Heute ist das Protokoll Industriestandard wenn es um die Vernetzung für das Internet of Things, Heimautomatisierung oder aber auch Vernetzung im Kontext Industrie 4.0 geht.

Als Telemetrieprotokoll ist es mit MQTT in erster Linie möglich Text und Zahlen zwischen verschiedenen verteilten Geräten (M2M-Kommunikation) zuverlässig zu übetragen und zwar auch bei ungünstigen Bedingungen.

### Zentrale Rolle des Brokers

Die Besondernheit von MQTT ist, dass eine zuverlässige Kommunikation zwischen den Kommunikationspartnern (Clients) ***durch einen zentralen Vermittler*** (Broker) gewährleistet wird. Der Broker bildet die Schnittstelle für die Kommunikation im Netzwerk. Die Clients kommunizieren nur mit ihm und kennen sich untereinander nicht. Der Broker hat die Aufgabe, Nachrichten anzunehmen und sie an interessierte Clients weiterzugeben.

### Publish-Subscribe-Messaging-Muster

MQTT verwendet für seine Kommunikation das Publish-Subscribe-Messaging-Muster.

Hierbei senden die Absender von Nachrichten, die sogennanten **Publisher**, ihre Nachrichten nicht direkt an bestimmte Empfänger.

Vielmehr veröffentlichen sie nur die Nachricht analog zu einem Broacast. Damit die Nachricht auch irgendwo ankommt, kategorisiert der Publisher seine Nachricht beim Absenden mit einer Klasse. Die verfügbaren Empfänger, die sogennanten Subscriber, erhalten dann die Nachrichten der Klassen für die sie auch angemeldet sind. 

Beim Publishen einer Nachricht als Publisher weiß man also nicht wer die Nachricht am Ende erhält oder ob sie überhaupt jemand erhält, da es davon abhängt ob es Subscriber für die gewählte Klasse gibt.

![MQTT Publish-Subscribe](assets/images/mqtt-publish-subscribe.jpg){: .img-responsive}

### Topics

Bei **Topics** handelt es sich um die MQTT-spezifische Bezeichnung der bereits angesprochenen Klassen des Publish-Subscribe-Messaging-Musters.

Für den Nachrichtenaustausch zwischen Client und Broker ist die Wahl eines Topics erforderlich. Topics bestehen aus technischer Sicht aus einem UTF-8-String. Dieser UTF-8-String wird logisch in Levels aufgeteilt, was durch einen Slash (Topic Level Seperator) dargestellt wird. Bei dieser logische Aufteilung handelt es sich um eine Baumstruktur ähnlich wie bei Domains oder Dateipfaden.

![MQTT Topics](assets/images/mqtt-topics.png){: .img-responsive}

### Topic-Filter

Es ist Subscribern möglich mithilfe von Wildcards **Topic Filter** zu erstellen. Dadurch kann beispielsweise mit nur einem Subscription-Request mehreren Topics zugleich gefolgt werden.

###### Single-Level-Wildcard +
Diese Wildcard kann in jedem beliebigen Topic Level stehen und auch mehrmals vorkommen. Damit lässen sich alle verschiedenen Möglichkeiten eines Topic-Levels auswählen.

Beispielsweise lässt sich bei der bereits vorgestellten Topic-Struktur die Temperatur aller verfügbaren Städte folgendermaßen auswählen:

![MQTT Single-Level-Wildcard](assets/images/mqtt-single-level-wildcard.png){: .img-responsive}

###### Multi-Level-Wildcard \#
Diese Wildcard kann nur im letzten Topic-Level vorkommen und wählt alle Topics auf der gleichen Ebene aus einschließlich aller Untertopics.

![MQTT Multi-Level-Wildcard](assets/images/mqtt-multi-level-wildcard.png){: .img-responsive}

###### Topics mit $
Eine Besonderheit bei MQTT sind Topics, die mit $ anfangen. Anwendungen dürfen keine Topics nutzen, die diesen Präfix haben, da jene Topics allein für den Broker reserviert sind. Beim Nutzen von Wildcards werden solche Topics ignoriert.


### MQTT Control Packet

Das MQTT-Protokoll tauscht sogenannte MQTT Control Packets aus. Das Paket besteht besteht wie gewöhnlich aus Header (Metadaten des Pakets) und Payload (eigentliche Nachricht). Der Header ist aber wiederrum in zwei Teile aufgeteilt: Dem sogennanten *Fixed Header*, den jedes Paket hat und einem *Variable header*, welchen nur bestimmte Pakettypen verwenden. Die offizielle Spezifikation ist [hier][MQTT_CONTROL_PACKET] zu finden.

[MQTT_CONTROL_PACKET]: http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html#_Toc398718019

###### Kontrollpakettypen
MQTT unterscheidet in 14 unterschiedliche Kontrollpakettypen, die zwischen Server und Client ausgetauscht werden. Hier ist die [vollständige Übersicht der Pakettypen][MQTT_PAKET_TYPES]. Sie haben alle verschiedene Funktionen wie z.B. den Verbindungsauf und -abbau, das Veröffentlichen von Nachrichten und das Subscriben und Unsubscriben von Topics, um die wichtigsten zu nennen.

[MQTT_PAKET_TYPES]: http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html#_Toc398718021

### Quality-of-Service
Quality of Service, kurz QoS ist die Dienstgüte eines Kommunikationskanals. Das Quality-of-Service Level bestimmt die Verbindlichkeit der Zustellung einer Nachricht vom Sender zum Empfänger.

Gerade bei Netzwerken, die keine zuverlässige Datenübertragung bieten, kann dank der QoS-Levels gewählt werden wie Zuverlässig die Übertragung der Nachricht sein sollte. Dies wird im Header des Kontrollpakets definiert.

[MQTT][MQTT_QoS] unterscheidet drei QoS-Level:
- Höchstens eine Zustellung (QoS Level 0)
- Mindestends eine Zustellung (QoS Level 1)
- Genau eine Zustellung (QoS Level 2)

[MQTT_QoS]: http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html#_Toc398718099

Bei einer Nachricht mit QoS-Level 0 (default) wird das Paket einmal versendet und es gibt keine Garantie, das die Nachricht beim Empfänger ankommt.

Ab QoS-Level 1 gibt es die Garantie, jedoch werden dafür mehrere Nachrichten an den Empfänger gesendet.

Ab QoS-Level 2, dem letzten Level, hat man außerdem noch die Sicherheit, das nur eine Nachricht beim Empfänger ankommt und es keine Duplikate gibt.

### Retained Messages

Da Clients nur über den Broker miteinander kommunizieren und sich untereinander nicht kennen, kann eine Nachricht verloren gehen, falls bei einem Subscriber-Client die Verbindung im falschen Moment unterbricht. Denn der Broker übermittelt die Nachrichten standardmäßig einfach nur in Echtzeit und merkt sich nichts.

Mit dem Setzen der Retain-Flag im Header einer Nachricht wird jedoch die letztgesendete Nachricht für ein entsprechendes Topic beim Broker zwischengespeichert und kann somit bei Neuverbindung eines Subscriber-Clients angefragt werden.

### Weitere Themen
Für eine tiefere Einarbeitung in das Thema ist die [offizielle Spezifikation des Standards][MQTT] zu empfehlen.

[MQTT]: http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html

### Bezug zum Projekt

Rhasspy und Alice nutzen beide MQTT für die interne Kommunikation zwischen den verschiedenen Komponenten des Techstacks. MQTT als Protokoll allein reicht jedoch nicht, da es ein reines Kommunikationsprotokoll ohne Anwendungslogik ist.

Aus diesem Grund implementieren beide das [Hermes Protokoll von Snips][SNIPS_HERMES], das genau für den Anwendungsfall der Sprachsteuerung entwickelt worden ist und sich bewährt hat. Es bietet primär Schnittstellen für die Kommunikation zwischen den einzelnen Komponenten.

Im Folgenden geben wir einen kurzen Einblick in das Hermes Protokoll inklusive der relevanten Topics. Neben den Topics von Hermes hat Alice auch eigene Topics auf die wir eingehen werden.

[SNIPS_HERMES]: https://docs.snips.ai/reference/hermes

**Snips Hermes Protokoll**

Hermes nutzt das MQTT-Protokoll zum Ausstausch von Nachrichten und spezifiziert in Form von Topics Schnittstellen für die einzelnen Komponenten. Darüber hinaus bestimmt es den gesamten Ablauf des Sprachsteuerungsprozesses: von der Aufnahme des Tons, dem Erkennen des Wakewords bis zur Erkennung und Ausführung des Intents, der Dialogführung und dem Sprachfeedback an den Nutzer.

**Anwendungsschicht**

MQTT baut meist auf TCP (Ausnahme: MQTT-SN) auf und befindet sich daher im TCP/IP-Modell auf der letzten Schicht: der Anwendungsschicht.

Da es aber den TCP/IP-Protokollstack außschließlich um weitere Funktionalität erweitert und im Gegensatz zu den gängigen Protokollen der Anwendungsschicht wie z.B. HTTP keine eigene Anwendungslogik festlegt bzw. kein festgelegtes Format für publizierte Nachrichten hat, muss das MQTT-Protokoll sozusagen um eine Schicht erweitert werden.

Das Hermes Protokoll von Snips macht genau das, es baut auf MQTT auf und definiert eine eigene Anwendungslogik.

**Format der Nachricht**

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


**Sprachsteuerung und das Zusammenspiel der Komponenten**

Wie bereits erwähnt bestimmt Hermes nicht nur Schnittstellen für die Kommunikation sondern auch ganz genau den Ablauf des Sprachsteuerungprozesses und wie die einzelnen Komponenten miteinander interagieren. Im Folgenden eine etwas vereinfachte Darstellung in 9 Schritten (es fehlt u.a. dialogueManager/sessionStarted):

![Hermes Message Flow](assets/images/hermes-flow.png){: .img-responsive}

**Hermes Topics**

Hermes-spezifische Topics haben alle ein `hermes` als Bezeichner des ersten Topic-Levels und lassen sich dadurch leicht erkennen. Das zweite Topic-Level beschreibt immer die zuständige Komponente. Eine vollständige Übersicht der API (Topics inkl. Felder) erhält man [hier][SNIPS_HERMES] und [hier][SNIPS_HERMES_DIALOG].

[SNIPS_HERMES_DIALOG]: https://docs.snips.ai/reference/dialogue

**Alice Topics**

Alice-spezifische Topics lassen sich ähnlich erkennen, nur dass der Bezeichner des ersten Topic-Levels `projectalice` ist. Wir haben eine Übersicht der verschiedenen [Alice Topics][ALICE_TOPICS] erstellt.

[ALICE_TOPICS]: /topic-uebersicht.html#alice

**ZigBee2MQTT**

ZigBee2MQTT hat auch seine eigenen Topics. Der First-Level-Bezeichner ist `zigbee2mqtt` und der Second-Level-Bezeichner ist entweder der Broker oder ein Gerät. Für eine ausführliche Auflistung aller Topics ist die [offizielle Referenz](https://www.zigbee2mqtt.io/information/mqtt_topics_and_message_structure.html) empfehlenswert.

**Topicübersicht**

Für eine grobe Übersicht aller Topics haben wir außerdem eine [eigene Seite in unsere Dokumentation](/topic-uebersicht.html) erstellt.

### Implementationen

Es gibt verschiedene (Open-Source) Implementationen des MQTT-Protokolls. Eine Übersicht der verschiedenen Broker und Clients findet man [hier][WIKI_MQTT_IMPLEMENT] und in ausführlicherer Form [hier][GITHUB_MQTT_LIBS].

[WIKI_MQTT_IMPLEMENT]: https://en.wikipedia.org/wiki/Comparison_of_MQTT_implementations
[GITHUB_MQTT_LIBS]: https://github.com/mqtt/mqtt.org/wiki/libraries

**Broker**

Der beliebteste Implementation eines Broker ist [Moquitto][GITHUB_MOSQUITTO] von Eclipse. Die Implementation ist Open-Source und läuft sehr zuverlässig auf dem Rapsberry Pi. Er wird standardmäßig bei Alice und Rhasspy verwendet.

[GITHUB_MOSQUITTO]: https://github.com/eclipse/mosquitto

**Clients**

Es gibt für eine ganze Reihe von Programmiersprachen verschiedene Implementationen des MQTT-Clients. Darüber hinaus gibt es noch gerätespezifische Client-Implementationen wie z.B. für die Arduino Plattform.

Da Alice in Python entwickelt wird benutzt es die Python-Library [paho-mqtt][PYPI_PAHO-MQTT].

[PYPI_PAHO-MQTT]: https://pypi.org/project/paho-mqtt/

**Clients für Endanwender**

Um sich mit dem Protokoll vertraut zu machen aber auch beim Debuggen als Entwickler kann es außerdem hilfreich sein ein MQTT-Client für Endanwender zu nutzen. Neben MQTT CLI, welches sich über die Kommandozeile steuern lässt, gibt es auch grafische Anwendungen wie z.B. MQTT.fx. Beide Clients sind Open Source und in Java programmiert und sind daher plattformunabhängig. Alternativen findet man in diesem [Artikel][HIVEMQ_MQTT_CLIENTS].

[HIVEMQ_MQTT_CLIENTS]: https://www.hivemq.com/blog/seven-best-mqtt-client-tools/