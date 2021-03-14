---
title: Weitere nützliche Skills zum Download
sections:
  - Reminder
  - Calculator
  - RandomUselessFacts
  - FreeCurrencyConverterDotCom
  - SpeedTest
---

Hier haben wir einige Skills aufgelistet, die wir intressant fanden für den täglichen Gebrauch oder zur Unterhaltung. Diese Skills werden nicht bei der Erstinstallation installiert, sondern können über die Weboberfläche im Reiter Skills bei dem Downloadsymbol oben rechts heruntergeladen und installiert werden. Nach dem Download wird die NLU trainiert und der Sprachassistent ist dann nicht ansprechbar. Das kann einige Zeit dauern.

Da wir ein Prblem mit der ASR (verlinken) hatten, konnten wir kaum einen Skill richtig testen, da das Testen durch die Sprachbarriere unfassbar anstrengend und zeitaufwendig war.

### Reminder

Der Reminder ist ein Skill, mit dem man Wecker und Timer setzen kann.

##### Funktionen

Die Funktionen gehen aus den Dateien im Git von ProjectAlice hervor.
- Einen Timer mit Angabe von Minuten oder Stunden stellen.
- Einen Wecker mit Angaben einer Uhrzeit und einem Datum stellen.
- Mehrere Wecker und Timer, die gleichzeitig laufen, einstellen.
- Mit einer Melodie oder einem Signalton den Ablauf eines Timers oder Wecker bekannt geben.
- Die Wecker und Timer haben einen Namen.
- Einen Wecker oder Timer löschen.
- Der Benutzer kann eine Abfrage machen, wie viel Zeit noch bleibt bis Wecker/Timer xy klingelt.

##### Erfahrungen

Bisher wurde nach unzähligen Versuchen nur einmal ein Timer erkannt. Nach ablauf des Timers ertönte eine Melodie und danach die Ansage welcher Timer das war. 
Also ist sicher, dass es möglich ist einen Timer mit Angaben von Minuten zu erstellen. Und es liegt nahe, dass man auch mehrere Timer erstellen kann, weil der Timer immer einen Namen hat. 
Eine Funktion, uns wünschen würden wäre das Umbenennen eines Timer oder Wecker. Dies scheint nicht möglich zu sein, wenn man in die Dateien im git schaut. Man kann nur einen Timer/Wecker löschen und neu setzen mit einem anderen Namen.
Weiter ist nicht klar, ob die Wecker und Timer gespeichert bleiben, wenn ein Neustart durchgeführt wird.

### Calculator

Der Calculator ist ein Skill mit dem der Sprachassistent zu einem kleinen Taschenrechner wird.

##### Funktionen

Die Funktionen gehen aus den Dateien im Git von ProjectAlice hervor.
- Grundrechenarten
- Potenz, Wurzel
- Sinus, Cosinus, Tangenz
- Modulo

##### Analyse Talk und Dialogue Files

Man kann mit dem Skill nur maximal zwei Zahlen verrechnen und mit dem Ergebnis nicht im selben Dialog weiter rechnen. Außerdem kann man nicht mit reelen Zahlen, also pi oder e, rechnen.

### RandomUselessFacts

Damit der Sprachassistent den Benutzer mit ausreichend unnützem Wissen versorgt, sollte dieser Skill unbedingt installiert sein. Allerdings benötigt der Skill eine Verbindung zum Internet.

##### Funktionen

Nach der Analyse der Dateien im Git zu diesem Skill wird klar, dass auf eine Anfrage des Benutzers ein zufälliger nutzloser Fakt aus dem Internet geladen wird. Bei einem Fehler (z.B. keine Internetverbindung) antwortet der Sprachassistent: "Es tut mir Leid, aber es gab einen Fehler beim herunterladen eines sinnlosen Fakts".

Von diesem Skill erwarten wir, dass nach entsprechender Aufforderung ein zufälliger Fakt genannt wird. Es sollen 
genügend Fakten vorhanden sein, dass sich nicht so schnell ein Fakt wiederholt. Außerdem soll auch einstellbar sein, 
dass ein zufälliger Fakt ohne Aufforderung nach einiger Zeit genannt wird ähnlich wie bei RedQueen(https://ip-team5.intia.de/skills.html#redqueen). 

##### Wünsche

Da eine API verwendet wird, ist nicht klar über wie viele Fakten diese Datenbank verfügt oder ob es nach einer Zeit schon langweilig wird. Der Skill [RedQueen](https://ip-team5.intia.de/skills.html#redqueen) kann einen zufälligen Satz nach einiger Zeit sagen. Es wäre schön diese Funktionalität hier wiederzufinden.

### FreeCurrencyConverterDotCom

Wie der Name des Skills schon vermuten lässt brauch man eine Internetverbindung. Man kann einen beliebigen Betrag in die verschiedensten Währungen umrechnen lassen und da hier eine API verwendet wird, werden auch immer die aktuellsten Kurse zur Berechnung verwendet. Aus der Analyse des Codes im Git von diesem Skill geht hervor, dass man einen API-Key erstellen muss und der Konfiguration in den Einstellungen hinzufügen muss, um den Skill nutzen zu können. Also ist der Skill nicht sehr Benutzer bzw. Anfänger freundlich.

### SpeedTest

Nachdem man einen Speedtest gestartet hat dauert es eine Weile und dann präsentiert der Sprachassistent die Ergebnisse. Dabei wir nur die Download und die Upload Geschwindigkeit ausgegeben und nicht der Ping oder der Provider. Aus dem Code geht nicht hervor welche oder ob eine API verwendet wird. Es kann sein, dass der Skill die Geschwindigkeit zum Download Server vom ProjectAlice testet, deshalb wird auch hier eine Internetverbindung benötigt.








