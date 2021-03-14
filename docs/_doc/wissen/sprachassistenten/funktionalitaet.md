---
title: Funktionalität
sections:
  - Alice
---

Um den Sprachassistenten mit Funktionalität zu erweitern, müssen weitere Intents erzeugt werden. Diese müssen wiederum implementiert werden (Intent handling). Je nachdem welches Framework dafür verwendet wird gibt es unterschiedliche Möglichkeiten. Rhasspy unterstützt Hermes kompatible Services wie zum Beispiel Home Assistant und [Hass.io](http://Hass.io). Der Skillstore von Alice unterstützt auch verschiedene Services mithilfe von Skills.

Makerlösungen bieten aber auch eigene Entwicklungsmöglichkeiten. Unter Rhasspy kann das Intenthandling mit Python oder Nodered umgesetzt werden.

### Alice

Im Gegensatz zu Rhasspy entwickelt man mit Alice nicht unbedingt Individuallösungen. Alice hat ein eigenes Skillsystem mit einem offiziellen Store, vergleichbar mit Alexa Skills und Google Actions. Dadurch kann man bei Bedarf mit Python eigene Skills erstellen und diese im Store veröffentlichen aber auch auf eine Vielzahl von der Community entwickelten Skills zurückgreifen ohne jeglichen Programmieraufwand.

Mit Scenarios, welches eine integrierte Node Red-Instanz ist, kann man theoretisch auch Intent handling betreiben indem man auf den erkannten Intent per MQTT Topic hört. Man müsste jedoch erst einmal einen Skill ohne jegliche Funktionalität erzeugen um neue Intents erstellen zu können. Scenarios ist daher nicht zum Intent Handling ausgelegt sondern ist vielmehr zum Personalisieren vorhandener Skills gedacht.