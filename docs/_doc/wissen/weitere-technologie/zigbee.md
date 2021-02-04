---
title: ZigBee (Smart-Home)
sections:
  - Offene Standards
  - Interoperabilität
  - Verbreitung durch ZigBee Light Link
  - ZigBee-Allianz
  - Anwendungsprofile und unterschiedliche Spezifikationen
  - ZigBee 3
  - Netzwerktopologie und Akteure im Netz
  - ZigBee-Gateways
  - Alternative ZigBee-Gateways
  - Vergleich zu anderen Funkstandards
  - Bewertung
---

Um smarte Geräte/Gegenstände im Haushalt anzusteuern und in einem Netzwerk zusammenzuschließen gibt es verschiedene Schnittstellen und Standards. Es wird einerseits unterschieden in offene Standards und geschlossene Systeme und andererseits in kabelgebundene und kabellose Lösungen. In unserer Dokumentation behandeln wir ausschließlich Funkstandards und fokussieren uns dabei auf den Open-Source Standard ZigBee.

### Offene Standards

Neben proprietären Smart Home Systemen gibt es viele Hersteller, die in ihren Geräten offene Standards implementieren. Dadurch lassen sich Geräte verschiedenster Hersteller mit dem selben Protokoll ansteuern. Die Standards ZigBee und Z-Wave haben sich durchgesetzt und sind weit verbreitet. Darüber hinaus verwenden einige Systeme auch WLAN oder Bluetooth. 

### Interoperabilität

Wenn ein Hersteller sich für einen offenen Standard entscheidet, ganz gleich ob WLAN, Bluetooth, ZigBee oder Z-Wave. Dann sind diese Geräte erst einmal mit Geräten, die auf einen anderen Standard setzen inkompatibel. Es gibt jedoch Versuche Interoperabilität zu erreichen indem man zwischen den verschiedenen Funkstandards übersetzt. Mehr dazu unter dem Punkt [ZigBee-Gateways](#zigbee-gateways). Außerdem kann es zum Beispiel auch sein, dass selbst ZigBee-Geräte nicht miteinander kompatibel sind da gerade in der Vergangenheit je nach Anwendungsfall unterschiedliche [ZigBee-Spezfikationen](#anwendungsprofile-und-unterschiedliche-spezifikationen) genutzt werden können.

[ZigBee Logo](assets/images/zigbee_logo.png){: style="float: right; margin-top: 0.35em" width="150px"}

ZigBee ist ein offener Funkstandard, der sich besonders für die Vernetzung von Geräten im Smart-Home-Bereich eignet, da er unterschiedlichste Geräte auf kurzen Strecken äußerst energieeffizent und zuverlässig miteinander verbindet. Durch seine Energieeffizienz eignet sich ZigBee besonders für batteriebetriebene Geräte, welche jahrelang verwendet werden können ohne das ständige Wechseln von Akkus.

In der Praxis beträgt die Funkreichweite je nach Leistung und baulicher Umgebung zwischen 10 und 20 Metern, theoretisch aber (unter idealen Bedingungen) bis zu 100 Meter. Zigbee-Netze können verschiedenen Netztopologien entsprechen. Durch das Bilden eines Mesh-Netzwerks, in dem Endgeräte Signale weiterleiten, kann die Reichweite beispielsweise erweitert werden.

ZigBee wird seit 2002 von der ZigBee-Allianz entwickelt. Die erste Version des Standards ist 2004 erschienen.

### Verbreitung durch ZigBee Light Link

Mit der Veröffentlichung des Anwendungsprofil ZigBee Light Link im Jahre 2012 gelang der Durchbruch. Die erste erste Generation der Philips Hue Beleuchtung ist im gleichen Jahr erschienen und verwendete das Anwendungsprofil als technische Grundlage. Auch andere smarte Beleuchtungssysteme wie Ikea Tradfri und Osram Lightify setzten auf die Technologie. Dadurch gelang eine weite Verbreitung von ZigBee-Geräten im Markt.

### ZigBee-Allianz

Philips, Ikea und Innr/Ledvance (Osram/Lightify) sind neben über 200 anderen Unternehmen Teil der ZigBee-Allianz. Sie haben das gemeinsame Ziel einen IoT-Standard zu entwickeln und verwenden ihn auch für eigenproduzierte Geräte. Eine Liste der Mitglieder der ZigBee-Allianz ist [hier][ZIGBEE_ALLIANCE] zu finden.

[ZIGBEE_ALLIANCE]: https://zigbeealliance.org/members/

### Anwendungsprofile und unterschiedliche Spezifikationen

In der Vergangenheit gab es unterschiedliche Spezifikationen von ZigBee, die nicht miteinander kompatibel waren und meist nur auf einen speziellen Anwendungsfall optimiert waren. 

Vor der Verbreitung von ZigBee und der Entstehung der verschiedenen Anwendungsprofile für ZigBee wie z.B. Light Link im Jahre 2012, gab es schon einige verschiedene Spezifikationen.

ZigBee Pro z.B. ist im Jahre 2007 erschienen und optimierte das ZigBee-Protokoll. Es bot eine verbesserte Sicherheit im Vergleich zu der bisherigen Spezifikation und eine größere Auswahl an Netztopologien.

Darüber hinaus gab es verschiedene Spezifikationen und Module, die für bestimmte Zwecke entwickelt worden sind. Zu nennen wäre da Green Power, Rf4ce und ZigBee IP.

Je nach Einsatzgebiet der Geräte gab es verschiedene Anwendungsprofile: ZigBee HA (HomeAutomation) für Heizungssysteme, ZigBee SE (SmartEnergy) für SmartMeter und ZigBee LL (Ligh Link) für Beleuchtungssysteme.

### ZigBee 3

ZigBee 3.0 wurde 2015 von der ZigBee Allianz angekündigt und hatte zum Ziel die einzelnen unterschiedlichen Spezifikationen in einem Standard zusammenzuführen und somit eine hohe Interoperabilität zwischen verschiedenen Geräten zu gewährleisten. Bei der Entwicklung wurde außerdem darauf Wert gelegt den Standard möglichst abwärtskompatibilität zu den bestehenden Spezifikationen zu machen.

Zu einem Standard wurden Anwendungsprofile wie HomeAutomation und Light Link aber auch die unterschiedlichen Spezifiaktionen wie ZigBee Pro, Green Power, ZigBee IP und RF4CE zusammengefasst. Mit diesem Standard ist es daher möglich Geräte unterschiedlicher Hersteller und Einsatzzwecke im gleichen Netzwerk zu verwenden, falls der Hersteller fremde Geräte zulässt.

Seit 2018 rüsten einiger Hersteller bereits im Markt erhältliche Geräte per Software-Update mit dem neuen Protokoll nach. Neue Geräte unterstützen ZigBee 3.0 mittlerweile von Haus aus.

### Netzwerktopologie und Akteure im Netz

![ZigBee Topologien](assets/images/zigbee-topologies.jpg){: .img-responsive style="float:right; max-height: 250px"}

Für den Aufbau eines Smart-Home-Systems gibt es im ZigBee-Standard drei unterschiedliche Gerätearten. Das sind End Devices, Router und Coordinators. Diese lassen sich in drei Topologien miteinander vernetzen: Stern, Baum und Mesh.

Ein ZigBee-Netzwerk hat immer nur einen Coordinator und ggf. mehrere Router und End Devices.

###### End device

Endgeräte (ZigBee-End-Devices auch ZED) haben keine verwaltende Funktion im Netzwerk. Sie sind in der Regel bateriebetriebene Geräte und Sensoren und können in den Schlafmodus versetzt werden. Sie melden sich an einen Router an und können ausschließlich mit ihm kommunizieren. Dies ist üblicherweise der nächstgelegene Router. Falls diese Router offline geht, geht für eine Weile auch die Verbindung zu all seinen Kindern verloren. Nach einem Timeout versuchen Endgeräte einen neuen Parent-Router zu finden. Manche Geräte wie Xiaomi-Geräte versuchen keinen neuen Parent-Router zu finden und bleiben daher unerreichbar falls der Router nicht wieder online geht. 

###### Router

Router (kurz ZR) haben eine verwaltende Funktion im Netzwerk. Sie leiten den Traffic der verschiedenen Knoten im Netzwerk weiter. Router sind nicht in der Lage zu schlafen, daher sind batteriegetriebene Geräte nicht als Router geeignet. Router sind sogennante Gate-Keeper des Netzwerks: d.h. sie sind dafür verantwortlich neue Geräte in das Netzwerk zu integrieren. Indem die Router den einzelnen Komponenten eine eindeutige Adresse geben, stellen sie sicher, dass keine Informationen verloren gehen. Verschiedene Router lassen sich hierarchisch in einer Baumstruktur oder dynamisch in einem Mesh-System miteinander verbinden.

###### Coordinator

Koordinatoren (kurz ZC) sind spezielle Router. Sie starten die Netzwerke mit vorgegebenen Einstellungen und funktionieren im Anschluss ganz normal als Router.

###### Topologien

Die **Stern-Topologie** sieht einen Koordinator und mehrere Endgeräte vor. Die Endgeräte können nicht direkt miteinander kommunizieren, sondern nur über den Koordinator. Fällt dieser zentrale Knoten aus, ist kein Datenaustausch mehr möglich.

In der **Baum-Topologie** gibt es einen Koordinator, wenige Router und Endgeräte. Jedes Endgerät (Kind) kommuniziert mit dem jeweiligen Router (Elternteil), die Router mit dem Koordinator in einer Baumstruktur.

In der **Mesh-Topologie** sind die Router zusätzlich untereinander vernetzt. Das ermöglicht viele alternative Pfade, um Daten von einem Knoten A zu einem Knoten B zu transportieren. Aus diesem Grund nutzen die meisten ZigBee betriebenen Smart-Home-Systeme Mesh-Netzwerke. Bis zu 65.000 Knoten sind erlaubt. Anderseits benötigen Router mehr Energie als einfache Endgeräte. Das mindert die Lebensdauer der Batterien.

### ZigBee-Gateways

Ein jedes ZigBee-System besitzt eine Basis-Station. Je nach Hersteller Gateway, Hub oder Bridge genannt. Wie bereits erwähnt ist ZigBee 3.0 grundsätzlich interoperabel. Es ist also technisch möglich Geräte verschiedener Hersteller in einem Netzwerk miteinander zu verbinden. Jedoch können sich Hersteller von Gateways auch dagegen entscheiden um Kunden an ihr Ecosystem zu binden. Eine Anbindung an die eigene Cloud gehört oft auch dazu.

###### Interoperabilität mit anderen Standards

ZigBee-Geräte lassen sich zudem nicht ohne Weiteres mit WLAN-, Bluetooth- oder Z-Wave-Geräten koppeln, da diese eine andere Sprache sprechen. Manche ZigBee-Gateways wie die Philips Hue Bridge oder der SmartThings Hub können jedoch zwischen den verschiedenen Funkstandards übersetzen.

### Alternative ZigBee-Gateways

Anstelle eines dedizierten Geräts als Gateway ist es beispielsweise möglich ein eigenes herstellerunabängiges Gateway mithilfe eines speziellen USB-Sticks und eines Raspberry Pis zu betreiben.

###### Netzwerkadapter von Texas Instruments

Es können z.B. einige Netzwerkadapter von Texas Instruments genutzt werden um ein eigenes ZigBee-Gateway zu betreiben. Das gängigste und außerdem preiswerteste Beispiel dafür ist der USB-Stick [CC2531][TI_CC2531] der ursprünglich zur Netzwerkanalyse dient aber zu einem ZigBee-Gateway umfunktioniert werden kann. Bei Händlern aus Fernost ist er schon ab Preisen von ungefähr 5 Euro erhältlich.

[TI_CC2531]: https://www.ti.com/tool/CC2531EMK

Es ist nötig ihn mit der passenden Firmware zu bespielen. Dazu wird der [Texas Instruments CC Debugger][TI_CC_DEBUGGER] und ein passendes Adapterkabel benötigt.

[TI_CC_DEBUGGER]: https://www.ti.com/tool/CC-DEBUGGER
###### ConBee II Stick

Eine weitere Alternative, die leistungsfähiger aber auch teurer ist, ist der [ConBee II Stick][CONBEE_2] von Phoscon.

[CONBEE_2]: https://phoscon.de/de/conbee2

###### Weitere Adapter

Eine Übersicht von kompatiblen Adaptern findet man [hier][ZIGBEE2MQTT_ADAPTERS].

[ZIGBEE2MQTT_ADAPTERS]: https://www.zigbee2mqtt.io/information/supported_adapters.html

###### Zigbee2MQTT

Mit [Zigbee2MQTT][ZIGBEE2MQTT] ist es möglich üblichen Geräten im Netzwerk (LAN) über das [MQTT-Protokoll][MQTT] eine Schnittstelle zum ZigBee-Netzwerk zu bieten.

[ZIGBEE2MQTT]: https://www.zigbee2mqtt.io/information/zigbee_network.html#zigbee2mqtt
[MQTT]: /mqtt.html

### Vergleich zu anderen Funkstandards
**WLAN**: Der herkömmliche WLAN-Standard WiFi 5 überträgt Daten mehr als tausendmal schneller als ZigBee, verbraucht aber auch viel Strom. Das ist bei der Videoübertragung einer smarten Überwachungskamera wegen der hohen Datenmenge notwendig. Ein batteriebetriebener Thermostat, der lediglich die Temperatur sendet, benötigt dagegen keine so große Bandbreite und profitiert von einem sparsameren Funkstandard wie ZigBee.

**Bluetooth**: Es bietet ebenfalls eine höhere Datenübertragungsrate als ZigBee, allerdings mit einer geringeren Reichweite. Aus diesem Grund dominiert Bluetooth vor allem bei drahtlosen Kopfhörern und Wearables, die Signale in einem Umkreis von wenigen Metern senden. Bei Sensoren in verschiedenen Räumen hat ZigBee ganz klar die Nase vorne.

**Z-Wave**: Es ist im Smart-Home-Bereich der Hauptkonkurrent von ZigBee. Das energiearme Protokoll kommt ebenfalls bei vielen Sensoren und Leuchtmitteln zum Einsatz, bietet eine hohe Kompatibilität und wie ZigBee eine hohe Reichweite dank Mesh-Netzwerken. Allerdings besitzt das US-Unternehmen Silicon Labs die Rechte für die Technologie. Anders als ZigBee handelt es sich bei Z-Wave also nicht um einen Open Source Standard. Dadurch können Hersteller das Protokoll nicht anpassen.

**EnOcean**: Kommt ausschließlich bei ultra-energiearmen Sensoren zum Einsatz, die durch Temperaturunterschiede und Bewegungen Strom generieren und damit ohne Batterien und externe Stromquellen auskommen. Auch ZigBee 3.0 unterstützt mit der Spezifikation Green Power diese Funktion. Insgesamt ist EnOcean weniger verbreitet als ZigBee.

### Bewertung

###### Vorteile von ZigBee

- Geringer Energieverbrauch: Sensoren und andere Smart-Home-Geräte kommen jahrelang mit ihren Batterien aus.- Hohe Kompatibilität: Die ZigBee Allianz zählt mehrere hundert Mitglieder, darunter Hersteller wie Osram, IKEA, Belkin und Signify. Ab ZigBee 3.0 lassen sich Smart-Home-Produkte verschiedener Hersteller leichter vernetzen.
- Open Source Code: Der ZigBee-Code steht jedem zur Verfügung. Herstellern steht damit frei, zusätzliche Funktionen in ihre Produkte zu implementieren.
- Hohe Reichweite: In Mesh-Netzwerken verhalten sich die Knoten als Repeater. In großen Häusern und Wohnungen verbessert sich damit die Reichweite im Vergleich zu WLAN signifikant.

###### Nachteile von ZigBee

- Kompatibilität unter ZigBee Geräten: Der Open Source Code war vor allem in der Vergangenheit unter dem Aspekt der Kompatibilität von Nachteil. Da jeder Hersteller zusätzliche Spezifikationen implementierte, sind ältere ZigBee-Geräte unterschiedlicher Marken nicht zwingend miteinander kompatibel. Seit der Einführung von ZigBee 3.0 ist der Standard jedoch einheitlicher geworden.
- Kompatibilität mit anderen Funkstandards: Wer ZigBee-Smart-Home-Produkte mit WLAN- oder Bluetooth-Geräten vernetzen will, benötigt ein Gateway. Da viele Smart-Home-Systeme wie HomeKit oder Google Home auf WLAN setzen, müssen Nutzer die Kosten für einen Gateway einplanen.
