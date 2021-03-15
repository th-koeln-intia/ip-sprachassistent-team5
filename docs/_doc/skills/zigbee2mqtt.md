---
title: Zigbee2Mqtt
sections:
  - TextInputWidget
  - SpeechVisualizer
---

Mit dem Skill Zigbee2Mqtt kann man eine Verbindung über einen Zigbeestick zu Zigbeelampen oder anderen Zigbeegeräten herstellen. Der Skill steht zum download zur Verfügung, aber ist offensichtlich noch nich vollständig ausgereift.

### Frühere Versionen

Einer unseren Aufgaben war über Sprache Lampen zu steuern. Die erste Version von diesem Skill, die wir verwendet haben, war für uns relativ unbrauchbar, weil der Skill lediglich die Anwendung Zigbee2Mqtt installiert hat (ohne eine Webgui). 
Es wurde keine Verbindung zu den Lampen hergestellt. Auch nach der herstellung einer Verbindung über Zigbee2Mqtt selbst, war der Skill ohne weitere Funktion. Es gab auch keine Intents, wobei nicht klar ist, ob Intents überhaupt vorgesehen sind.

### Neuere Versionen und Erwartungen

Nach einem Update, dass mitten im Projekt kam, konnte man über die Weboberfläche von ProjectAlice im Reiter Skills in den Einstellungen des Skills die Verbingung zu den Zigbeegeräten herstellen. Diese Funktion haben wir allerdings nicht getestet.
Wir erhoffen uns, dass in der Zukunft mit diesem Skill, nicht nur die Lampen verbunden werden können, sondern auch angesteuert werden können, vielleicht auch über Sprache. Doch dazu muss die neue Weboberfläche erst zuverlässi funktionieren.

### Unsere Arbeit

Um unsere Lampen nun doch noch über Sprache zu steuern, haben wir einen Skill mit Intents erstellt und die Lampensteuerung über die Webui in ProjectAlice abgebildet. [Hier]() geht es zur ganzen Geschichte
und [hier](https://ip-team5.intia.de/anleitung-entwicklung.html#skillentwicklung) geht es zur Entwicklung eines ersten Skills.
