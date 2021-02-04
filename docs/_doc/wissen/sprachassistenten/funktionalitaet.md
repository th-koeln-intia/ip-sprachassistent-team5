---
title: Funktionalität
---

Um den Sprachassistenten mit Funktionalität zu erweitern müssen weitere Intents erzeugt werden. Diese müssen wiederrum implementiert werden (Intent handling). Dafür können unter anderem mit Hermes kompatible Services genutzt werden wie zum Beispiel Home Assistant und [Hass.io](http://Hass.io).

Makerlösungen bieten aber auch eigene Entwicklungsmöglichkeiten. Unter Rhasspy kann das Intenthandling mit Python oder Nodered umgesetzt werden.

Bei Alice gibt es ein Skillsystem mit einem offiziellen Store. Mit Python können ebenfalls eigene Skills erstellen und diese sogar im Store veröffentlicht werden.

Mit Scenarios (Node Red) kann man theoretisch auch Intent handling betreiben indem man auf den erkannten Intent per MQTT Topic hört. Man müsste jedoch erst einmal einen Skill ohne jegliche Funktion erzeugen um neue Intents erstellen zu können. Scenarios ist daher nicht zum Intent Handling ausgelegt sondern ist vielmehr zum Personalisieren vorhandener Skills gedacht. 