---
title: Funktionsweise
sections:
  - Zentrale Rolle des Brokers
  - Publish-Subscribe-Messaging-Muster
  - Topics
  - Topic-Filter
  - MQTT Control Packet
  - Quality-of-Service
  - Retained Messages
  - Weitere Themen
---

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