---
title: Skills, die wir getestet haben
sections:
  - Reminder
  - Textinputwidget
  - Speechvisualizer
---

### Reminder

Der Reminder ist ein Skill, mit dem man Wecker und Timer setzen kann.

##### Unsere Erwartungen an den Skill

- Der Skill soll einen Timer mit Angabe von Minuten oder Stunden stellen können.
- Der Skill soll einen Wecker mit Angaben einer Uhrzeit und einem Datum stellen können.
- Der Benutzer soll mehrere Wecker und Timer, die gleichzeitig laufen, einstellen können.
- Der Skill soll eine Melodie oder Signalton haben.
- Die Wecker und Timer einzeln sollen einzeln benennbar sein.
- Die Wecker und Timer sollen umbennenbar sein.
- Der Benutzer soll eine Abfrage machen können, deren Ausgabe ist wie viel Zeit noch bleibt bis Wecker/Timer xy klingelt.
- Wenn Alice neugestartet wird, sollen die Wecker/Timer gespeichert bleiben.

##### Tests

- Einen Timer stellen
- Einen Wecker stellen
- Zwei Timer und zwei Wecker stellen
- Abfragen, wie viel zeit noch bleibt
- Einen Wecker stellen und Alice neustarten
- Einen Wecker stellen und umbennen

##### Ergebnisse

Bisher wurde nach unzähligen Versuchen nur einmal ein Timer erkannt. Nach ablauf des Timers ertönte eine Melodie und danach die Ansage welcher Timer das war. 
Also kann man bis jetzt sagen, dass es möglich ist einen Timer mit Angaben von Minuten zu erstellen und der Timer hat auch immer einen Namen. Daher liegt es nahe, dass man auch mehrere Timer erstellen kann. 
Außerdem gibt es eine Melodie, womit eine weitere Erwartung an den Skill erfüllt wurde.

Laut der Dokumentation auf GitHub sollten die übrigen Anforderungen auch erfüllt werden. Lediglich die Frage, ob die Wecker und Timer gespeichert werden und nach dem Neustart funktionieren, bleibt offen und zu testen.

TODO: Wenn die ASR vernünftig läuft, ausführlicher testen.



### Calculator

TODO




### RandomUselessFacts

TODO






















