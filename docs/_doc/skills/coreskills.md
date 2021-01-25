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



### DateDayTimeYear



### Telemetry



### Contextsensitive