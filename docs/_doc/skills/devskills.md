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

TODO: Bilder und genauere beschreibung von funktionen.

Ein Hauptproblem bei diesem Skill ist, dass man nicht mehrstufige Dialoge führen kann. Das bedeutet, wenn man zum Beispiel den Reminder(https://ip-team5.intia.de/skills.html#reminder) testet, sagt der Benutzer: "Erstelle einen Alarm für 14 Uhr" und der Assistent antwortet:
"Welche Nachricht möchtest du für den Alarm hinterlegen?" oder "Welches Thema soll der Alarm haben?" und dann wird der Dialog beendet ohne antworten zu können.

Die Funktion "Remember me" funktioniert nicht zuverlässig.

### SpeechVisualizer

Ähnlich wie der Skill Textinputwidget ist der Skill Speechvisualizer nicht unbedingt für den Benutzer, sondern für den Entwickler gedacht. Auch mit diesem Skill kann man kleine Oberflächen auf der Weboberfläche im Reiter HOME erstellen.
Diese zeigen an 

TODO: Bilder und genauere beschreibung von funktionen.

Wenn kein Intent erkannt wurde zeigt die Confidence Anzeige einen unlogisch hohen Wert an.
