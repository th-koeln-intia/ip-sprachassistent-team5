---
title: Funktion und Besonderheiten
sections:
  - Zentrale Rolle des Brokers
  - Publish-Subscribe-Messaging-Muster
  - Topics
  - Wildcards
---

Als Telemetrieprotokoll ist es mit MQTT in erster Linie möglich Text und Zahlen zwischen verschiedenen verteilten Geräten (M2M-Kommunikation) zuverlässig zu übetragen und zwar auch bei ungünstigen Bedingungen.

### Zentrale Rolle des Brokers

Die Besondernheit von MQTT ist, dass eine zuverlässige Kommunikation zwischen den Kommunikationspartnern (Clients) ***durch einen zentralen Vermittler*** (Broker) gewährleistet wird. Der Broker bildet die Schnittstelle für die Kommunikation im Netzwerk. Die Clients kommunizieren nur mit ihm und kennen sich untereinander nicht. Der Broker hat die Aufgabe, Nachrichten anzunehmen und sie an interessierte Clients weiterzugeben.

### Publish-Subscribe-Messaging-Muster

MQTT verwendet für seine Kommunikation das Publish-Subscribe-Messaging-Muster.

Hierbei senden die Absender von Nachrichten, die sogennanten **Publisher**, ihre Nachrichten nicht direkt an bestimmte Empfänger.

Vielmehr veröffentlichen sie nur die Nachricht analog zu einem Broacast. Damit die Nachricht auch irgendwo ankommt, kategorisiert der Publisher seine Nachricht im Vorfeld mit einer Klasse. Die verfügbaren Empfänger, die sogennanten Subscriber, erhalten dann die Nachrichten der Klassen für die sie auch angemeldet sind. 

Beim Publishen einer Nachricht als Publisher weiß man also nicht wer die Nachricht am Ende erhält oder ob sie überhaupt jemand erhält, da es davon abhängt ob es Subscriber für die gewählte Klasse gibt.

![MQTT Publish-Subscribe](assets/images/mqtt-publish-subscribe.jpg){: .img-responsive}

### Topics

Bei **Topics** handelt es sich um die MQTT-spezifische Bezeichnung der bereits angesprochenen Klassen des Publish-Subscribe-Messaging-Musters.

Für den Nachrichtenaustausch zwischen Client und Broker ist die Wahl eines Topics erforderlich. Topics bestehen aus technischer Sicht aus einem UTF-8-String. Dieser UTF-8-String wird logisch in Levels aufgeteilt, was durch einen Slash (Topic Level Seperator) dargestellt wird. Bei dieser logische Aufteilung handelt es sich um eine Baumstruktur ähnlich wie bei Domains oder Dateipfaden.

![MQTT Topics](assets/images/mqtt-topics.png){: .img-responsive}

### Wildcards

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
