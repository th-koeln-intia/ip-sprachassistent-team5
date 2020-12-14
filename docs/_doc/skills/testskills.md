---
title: Skills, die wir getestet haben
sections:
  - Reminder
  - Calculator
  - RandomUselessFacts
  - Coronavirus
  - FreeCurrencyConverterDotCom
  - InternationalSpaceStation
  - SpeedTest
---

### Reminder

Der Reminder ist ein Skill, mit dem man Wecker und Timer setzen kann.

##### Erwartungen an den Skill

- Der Skill soll einen Timer mit Angabe von Minuten oder Stunden stellen können.
- Der Skill soll einen Wecker mit Angaben einer Uhrzeit und einem Datum stellen können.
- Der Benutzer soll mehrere Wecker und Timer, die gleichzeitig laufen, einstellen können.
- Der Skill soll eine Melodie oder Signalton haben.
- Die Wecker und Timer einzeln sollen einzeln benennbar sein.
- Die Wecker und Timer sollen umbennenbar sein.
- Der Benutzer kann einen Wecker oder einen Timer löschen.
- Der Benutzer soll eine Abfrage machen können, deren Ausgabe ist wie viel Zeit noch bleibt bis Wecker/Timer xy klingelt.
- Wenn Alice neugestartet wird, sollen die Wecker/Timer gespeichert bleiben.

##### Durchgeführte Tests

- Einen Timer stellen
- Einen Wecker stellen
- Zwei Timer und zwei Wecker stellen
- Einen Timer erstellen und löschen
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

Der Calculator ist ein Skill mit dem der Sprachassistent zu einem kleinen Taschenrechner wird.

##### Erwartungen an den Skill

- Grundrechenarten
- Potenz, Wurzel
- Mehr als zwei Zahlen
- Kompliziertere Formeln
- Negative Zahlen, Dezimalzahlen
- Reele Zahlen

##### Durchgeführte Tests

- 3 + 4
- 4 - 3
- 3 * 4
- 12 / 3
- 2 hoch 3
- Wurzel von 144
- 3 + 4 + 5
- Wurzel von (4+5)
- 3 - 4
- 4 / 3
- Pi * 2 hoch 2

##### Ergebnisse

siehe Reminder

### RandomUselessFacts

Damit der Sprachassistent den Benutzer mit ausreichend unnützem Wissen versorgt, sollte dieser Skill unbedingt installiert sein.

##### Erwartungen an den Skill

Von diesem Skill erwarten wir, dass nach entsprechender Aufforderung ein zufälliger Fakt genannt wird. Es sollen 
genügend Fakten vorhanden sein, dass sich nicht so schnell ein Fakt wiederholt. Außerdem soll auch einstellbar sein, 
dass ein zufälliger Fakt ohne Aufforderung nach einiger Zeit genannt wird ähnlich wie bei RedQueen(https://ip-team5.intia.de/skills.html#redqueen). 

##### Durchgeführte Tests

- Einen Sinnlosen Fakt abfragen.
- Einstellungen durchsuchen nach einer möglichen zeiteinstellung.

##### Ergebnisse

Nach der ersten erfolgreichen Abfrage mit richtig erkanntem Intent hing sich das ProjectAlice auf.

siehe Reminder

### Coronavirus

##### Erwartungen an den Skill

- Vortragen aktueller Zahlen und Statistiken Weltweit
- Zahlen und Statistiken nach Angabe von Land oder Region
- Vorlesen aktueller Schlagzeilen zum Thema

##### Durchgeführte Tests

- 

##### Ergebnisse

siehe Reminder

### FreeCurrencyConverterDotCom

##### Erwartungen an den Skill

Von diesem Skill erwarten wir, dass ein Betrag in einer Währung in jede beliebige andere Währung ungerechnet wird. Es sollen
alle gängigen Währungen aus den größten Wirtschaftsstaaten und beliebtesten Urlaubsggebieten unterstützt werden.

##### Durchgeführte Tests

Verschiedene Beträge in verschiedene Währungen umrechnen lassen.

##### Ergebnisse

siehe Reminder

### InternationalSpaceStation

##### Erwartungen an den Skill

Der Skill soll die aktuelle Position und Besatzung der ISS nennen können. Außerdem wäre es wünschenswert, dass 
man auch erfahren kann über welchem Kontinent die ISS aktuell zu sehen ist und wann sie das nächste mal über der 
eigenen Position zu sehen ist.

##### Durchgeführte Tests

- Abfrage der Position
- Abfrage der Besatzung

##### Ergebnisse



siehe Reminder

### SpeedTest

##### Erwartungen an den Skill

- Upload
- Download
- Ping
- Provider

##### Durchgeführte Tests

- Speedtest durchführen lassen

##### Ergebnisse

siehe Reminder



















