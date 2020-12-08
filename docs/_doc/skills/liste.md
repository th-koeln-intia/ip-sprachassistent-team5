---
title: Skills die wir getestet haben
---

Eine Auflistung aller veröffentlichten Skills gibt es auf der [Seite von Alice](https://store.projectalice.io/).

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


### Textinputwidget

Während der Arbeit am ASR von Alice, wurden wir auf Textinputwidget aufmerksam. Mit diesem Skill kann man eine kleine Oberfläche auf der Weboberfläche im Reiter HOME erstellen, 
in der man eintippen kann was der Sprachassistent sagen soll oder was er verstehen soll. Das heißt es ist kein Skill, der über Sprache aktiviert wird, sondern nur ein Tool,
um andere Skills und Funktionen besser zu testen.

TODO: Bilder und genauere beschreibung von funktionen.

Ein Hauptproblem bei diesem Skill ist, dass man nicht mehrstufige Dialoge führen kann. Das bedeutet, wenn man zum Beispiel den Reminder testet, sagt der Benutzer: "Erstelle einen Alarm für 14 Uhr" und der Assistent antwortet:
"Welche Nachricht möchtest du für den Alarm hinterlegen?" oder "Welches Thema soll der Alarm haben?" und dann wird der Dialog beendet ohne antworten zu können.

### Speechvisualizer

Ähnlich wie der Skill Textinputwidget ist der Skill Speechvisualizer nicht unbedingt für den Benutzer, sondern für den Entwickler gedacht. Auch mit diesem Skill kann man kleine Oberflächen auf der Weboberfläche im Reiter HOME erstellen.
Diese zeigen an 

TODO: Bilder und genauere beschreibung von funktionen.

Wenn kein Intent erkannt wurde zeigt die Confidence Anzeige einen unlogisch hohen Wert an.


















