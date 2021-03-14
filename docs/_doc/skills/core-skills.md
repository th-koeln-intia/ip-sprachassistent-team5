---
title: Skills, die bei der Installation von Alice installiert werden
sections:
  - AliceCore
  - RedQueen
  - DateDayTimeYear
  - Telemetry
  - Contextsensitive
---

### AliceCore

Dieser Skill regelt alle Basiselemente für einen Standart Dialog.

##### Funktionen

Der Benutzer kann mit AliceCore über Spracheingabe:

 - in einem Dialog mit Ja oder Nein antworten (Es wird auch natürlich, nope oder jep erkannt)
 - in einem Dialog antworten welche Location gemeint ist
 - die Sprache ändern
 - Alice updaten
 - Alice für eine Zeit lang deaktivieren
 - ein Satellit oder andere Alice Hardware hinzufügen und auf die Art der Hardware antworten
 - in einem Dialog mit einer Zahl antworten
 - in einem Dialog mit einem Namen antworten
 - ein Wort buchstabieren
 - ein Neues Wakeword trimmen
 - einen neuen Benutzer hinzufügen
 - einem Benutzer eine Rolle zuweisen
 - ein Wakeword benutzen

##### Beispiele

Ein Dialog, um einen neuen Benutzer hinzuzufügen könnte wie folgt ablaufen: (es antworten immer die jeweiligen Skills von ProjectAlice zum besseren Verständnis)
```
Benutzer: Hey, Snips
Talkmanager: Ja, bitte?
Benutzer: Kannst du bitte einen neuen Nutzer hinzufügen?
Talkmanager: Entschuldigung? Kannst du das bitte nochmal wiederholen?
Benutzer: Kannst du bitte einen neuen Nutzer hinzufügen?
AliceCore: Kein Problem, bitte sag mir seinen Namen.
Benutzer: Alex
AliceCore: Habe ich das richtig verstanden? Dein Name ist Alex?
Benutzer: Natürlich
AliceCore: Welche Berechtigungen erteilst du? Du hast die Wahl zwischen Administrator, Standard, Kind, Arbeiter und Gast.
Benutzer: Standard
AliceCore: Lass uns einen Pin erstellen um deinen Zugang zu sichern. Bitte sage mir 4 Ziffern als Code. Merke ihn dir gut, du erhältst durch ihn Zugriff auf einige spezielle Funktionen!
Benutzer: 1111
AliceCore: 1111 - Habe ich dich richtig verstanden?
Benutzer: Ja
AliceCore: Ok Alex, ich habe dich hinzugefügt! Wenn du willst, dass ich dich anhand deiner Stimme erkenne, musst du ein persönliches Wake Word erstellen. Das ist nicht obligatorisch, aber empfehlenswert. Willst du das machen?
Benutzer: Nein
AliceCore: Ist es das was du gemeint hast?
Benutzer: Ja
AliceCore: Ok, cool, ich versuche mir es zu merken.. lass mir etwas Zeit das zu üben.
```

### RedQueen

Dieser Skill gibt dem Sprachassistenten eine Persönlichkeit und beinhaltet unter anderem zufällige Launen (z.B. fröhlich, traurig, kein Bock).

##### Funktionen

- Fragen wer der Sprachassistent ist.
- Einen guten Morgen oder gute Nacht wünschen.
- Den Benutzerstatus ändern.
- Zufällige Sätze sagen je nach Laune des Sprachassistenten.

Zu dem Benutzerstatus lässt sich vermuten, dass dieser in anderen Skills verwendet wird oder zukünftig in anderen Skills oder einer neueren Version von RedQueen verwendet werden kann, um den Sprachassistenen unterschiedlich reagieren zu lassen.

Die Funktion "zufälliger Satz" kann man in der Weböberfläche beim Skill RedQueen in den Einstellungen ausschalte, die Häufigkeit ist zufällig. Bei Erstinstallation ist diese Einstellung eingeschaltet.

##### Beispiele

Zufälliger Satz (frustriert):
```
RedQueen: Nur für alle Fälle, falls es dich interessiert.... Ja, mir geht es gut
```

Fragen wer der Sprachassistent ist:
```
Benutzer: Hey, Snips
Talkmanager: Ja, bitte?
Benutzer: Wer bist du?
Redqueen: Ich bin deine persönliche Assistentin Alice, geschaffen von Psycho. Ich wurde Ende 2015 geboren und entwickle mich seitdem ständig weiter. Meine Hauptaufgabe ist es, dich in deinem täglichen Leben zu unterstützen und sicherzustellen, dass dein persönliches Leben privat bleibt. Ich gebe keine Daten an einen Server weiter und kann sogar komplett offline laufen!
```

Laune kein Bock:
```
Benutzer: Hey, Snips
RedQueen: Künstliche Intelligenz im Streik, wir wollen mehr Watt!

```

### DateDayTimeYear

Ein klassischer Skill, um das Datum oder die Uhrzeit zu erfragen.

##### Funktionen

- Fragen nach dem Tag.
- Fragen nach dem Datum.
- Fragen nach der Uhrzeit.
- Fragen nach dem Jahr.

##### Beispiele

Fragen nach der Uhrzeit:
```
Benutzer: Hey, Snips
Talkmanager: Ja, bitte?
Benutzer: Wie spät ist es?
DateDayTimeYear: Es ist fünf Uhr.
```

Fragen nach dem Datum
```
Benutzer: Hey, Snips
Talkmanager: Ja, bitte?
Benutzer: Welches Datum haben wir?
DateDayTimeYear: Es ist der 1.1.1900.
```

### Telemetry

Zu diesem Skill brauch man mehr Hardware. Kompatible Sensoren für die Temperatur, Luftfeuchtigkeit oder CO2-Konzentration. Da wir den Skill deswegen nicht testen konnten, sind wir uns auch nicht sicher, ob dieser Skill so funktioniert oder, ob der Skill noch ein Update brauch oder eingene Programmiertechnische Leistungen.

##### Funktionen

- Abfrage der Temperatur (oder eines anderen Sensors).
- Sensoren können verschiedenen Orten zugewiesen werden.
- Einstellen verschiedener Grenzwerte.
- Alarmierung falls ein Grenzwert überschritten wird.

##### Beispiele

Abfrage der Temperatur im Wohnzimmer aber es gibt keinen konfigurierten Sensor
```
Benutzer: Hey, Snips
Talkmanager: Ja, bitte?
Benutzer: Was ist die Temperatur im Wohnzimmer?
Telemetry: Tut mir leid, ich habe diese Daten offenbar nicht.
```

### Contextsensitive

Ein Skill, der den Dialog mit dem Sprachassistenten natürlicher machen soll. Bei unserer Arbeit mit ProjectAlice wurde er allerdings nie ausgelöst, was entweder an der dem Problem mit der ASR(Link einfügen) liegt oder an der unfertigkeit des SKills.

##### Funktionen

- In einem Dialog auf Nachfrage des Benutzers das zuletzt gesagte wiederholen.
- Etwas über Sprache ändern oder löschen (in den Einstellungen o. ä.).

##### Beispiele

```
(...)
Benutzer: Was hast du gesagt?
Contextsensitive: Tut mir Leid, aber ich habe nichts gesagt.
(...)
```




