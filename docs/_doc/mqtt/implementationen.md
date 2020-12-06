---
title: Implementationen
sections:
  - Broker
  - Clients
---

Es gibt verschiedene (Open-Source) Implementationen des MQTT-Protokolls. Eine Übersicht der verschiedenen Broker und Clients findet man [hier][WIKI_MQTT_IMPLEMENT] und in ausführlicherer Form [hier][GITHUB_MQTT_LIBS].

[WIKI_MQTT_IMPLEMENT]: https://en.wikipedia.org/wiki/Comparison_of_MQTT_implementations
[GITHUB_MQTT_LIBS]: https://github.com/mqtt/mqtt.org/wiki/libraries

### Broker

Der beliebteste Implementation eines Broker ist [Moquitto][GITHUB_MOSQUITTO] von Eclipse. Die Implementation ist Open-Source und läuft sehr zuverlässig auf dem Rapsberry Pi. Er wird standardmäßig bei Alice und Rhasspy verwendet.

[GITHUB_MOSQUITTO]: https://github.com/eclipse/mosquitto

### Clients

Es gibt für eine ganze Reihe von Programmiersprachen verschiedene Implementationen des MQTT-Clients. Darüber hinaus gibt es noch gerätespezifische Client-Implementationen wie z.B. für die Arduino Plattform.

Da Alice in Python entwickelt wird benutzt es die Python-Library [paho-mqtt][PYPI_PAHO-MQTT].

[PYPI_PAHO-MQTT]: https://pypi.org/project/paho-mqtt/

###### Clients als Endanwender

Um sich mit dem Protokoll vertraut zu machen aber auch beim Debuggen als Entwickler kann es außerdem hilfreich sein ein MQTT-Client für Endanwender zu nutzen. Neben MQTT CLI, welches sich über die Kommandozeile steuern lässt, gibt es auch grafische Anwendungen wie z.B. MQTT.fx. Beide Clients sind Open Source und in Java programmiert und sind daher plattformunabhängig. Alternativen findet man in diesem [Artikel][HIVEMQ_MQTT_CLIENTS].

[HIVEMQ_MQTT_CLIENTS]: https://www.hivemq.com/blog/seven-best-mqtt-client-tools/