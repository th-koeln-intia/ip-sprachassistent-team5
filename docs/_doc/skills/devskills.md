---
title: Skills, die für Entwickler nützlich sind
sections:
  - TextInputWidget
  - SpeechVisualizer
---

### TextInputWidget

Während der Arbeit am ASR von Alice, wurden wir auf Textinputwidget aufmerksam. Mit diesem Skill kann man eine kleine Oberfläche auf der Weboberfläche im Reiter HOME erstellen, 
in der man eintippen kann was der Sprachassistent sagen soll oder was er verstehen soll. Das heißt es ist kein Skill, der über Sprache aktiviert wird, sondern nur ein Tool,
um andere Skills und Funktionen besser zu testen.

Ein Hauptproblem bei diesem Skill ist, dass man nicht mehrstufige Dialoge führen kann. Das bedeutet, wenn man zum Beispiel den Reminder(https://ip-team5.intia.de/skills.html#reminder) testet, sagt der Benutzer: "Erstelle einen Alarm für 14 Uhr" und der Assistent antwortet:
"Welche Nachricht möchtest du für den Alarm hinterlegen?" oder "Welches Thema soll der Alarm haben?" und dann wird der Dialog beendet ohne antworten zu können.

In der Weboberfläche muss man sich in dem sogenannten Widget einloggen. Das funktioniert mit den Daten des Admins oder einem zuvor angelegten Benutzer. Was allerdings nicht zuverlässig funktioniert ist die Funktion "Remember me", sodass man im Zweifel immer wieder die Daten eintippen muss.

### SpeechVisualizer

Ähnlich wie der Skill Textinputwidget ist der Skill Speechvisualizer nicht unbedingt für den Benutzer, sondern für den Entwickler gedacht. Auch mit diesem Skill kann man kleine Oberflächen auf der Weboberfläche im Reiter HOME erstellen.
Diese zeigen zum einen an, was der Sprachassistent verstanden hat, und zum anderen, was der Sprachassistent antwortet.

Ein kleiner Bug den wir hier entdeckt haben wird ausgelöst, wenn kein Intent erkannt wurde. Dann zeigt die Confidence Anzeige einen Wert weit über 1 an, dabei ist 1 der Maximale Confidence Wert.
