---
title: Enwicklung eines eigenen Skills
sections:
  - Schritt 1 Skill mit Intents
  - Schritt 2 NodeRed implementation
  - Schritt 3 Testen
  - Bewertung
  
---

Weil der Skill [Zigbee2Mqtt]() für unser Ziel eine Lampe über Sprache ansteuern unbrauchbar war brauchten wir eine andere Lösung. Unsere Idee: einen Skill erstellen, der (wenn auch Hardcode) für uns funktioniert.

### Schritt 1 Skill mit Intents

Hier geht es zur Kurzanleitung zur [Erstellung eines Skills](https://ip-team5.intia.de/anleitung-entwicklung.html#skillentwicklung).

Wir haben uns bei der Entwicklungsumgebung für VS Code entschieden, weil immer nur einer an dem Skill gearbeitet hat und wir so schneller und einfacher den Skill testen konnten. 
Man muss nur die geänderten Dateien speichern und dann Alice neustarten im Terminal von VS Code mit 'sudo systemctl restart ProjectAlice'. Dann kann man den Skill über Sprache testen oder noch einfacher und schneller mit den Skills 
[TextInputWidget](https://ip-team5.intia.de/skills.html#textinputwidget) und [SpeechVisualizer](https://ip-team5.intia.de/skills.html#speechvisualizer).

Schon bei diesem ersten Schritt traten die ersten Probleme auf, denn unser Skill war in der Skillübersicht von ProjectAlice "disabled" und konnte nicht enabled werden.
Die Lösung war die Datei .py im Ordner skills/LightsController/widget zu löschen. Dieses Problem ist auch bei anderen Entwicklern aufgetreten. [Nachzulesen hier](https://github.com/project-alice-assistant/ProjectAlice/issues/359)

Als nächstes müssen noch die Intents geschrieben werden, wie in unserer Anleitung beschrieben. Einen Intent zum einschalten, einen zum ausschalten und einen um die Farbe zu wechseln. Neu bei dem Farbenintent ist, dass SlotTypes verwendet werden.
Diese sind Bestandteil von dem DialogueTemplate und der Benutzer kann dadurch verschiedene Farben oder verschiedene Lampen nennen und der Sprachassistent kann auch Synonyme verstehen. Zum Beispiel lila und violett haben beiden den value violette
und ergeben später die selbe Färbung der Lampe. Wie das dann genau aussieht kann man [hier nachschauen](https://github.com/th-koeln-intia/ip-sprachassistent-team5/blob/master/skill/LightsController/dialogTemplate/de.json).

Das Ergebnis ist nach diesem Schritt ist ein Skill, mit dem man jetzt dem Sprachassistenten sowas sagen kann wie "Mach das Licht an" oder "Ändere die Farbe der PC-Lampe zu rot" und der Sprachassistent antwortet "Das Licht ist jetzt an" und "Die Farbe wurde geändert", 
auch wenn bis hierhin weder das Licht wirklich angeht noch die Farbe der Lampe sich verändert.

### Schritt 2 NodeRed implementation

Über die Webgui von ProjectAlice kann man im Adminbereich die Funktion NodeRed aktivieren. Hier fehlt allerdings ein Paket Nodes von Zigbee2Mqtt, das hinzugefügt werden muss. Zuvor sei gesagt, dass Zigbee2Mqtt auf dem Pi installiert wurde und,
weil es einfacher ist, über das Frontend von Zigbee2Mqtt die beiden Lampen verbunden wurden. Unsere Lampen heißen PC-Lampe und Sofa-Lampe.

Man benötigt jetzt die Nodes "mqtt in", um das Topic hermes/intent/<NameDesSkills> zu fangen und mit der Message weiter zu arbeiten. Zunächst wird die Message ins .json-Format übersetzt, damit die Debug Nachrichten lesbar sind.
Will man jetzt nur den Intent "Licht an" zum funktionieren bringen, brauch man einen node aus dem paket Zigbee2Mqtt, nämlich das "out" Node. In diesem stellt man die Lampen ein und wählt aus, dass diese eingeschaltet werden soll.

Möchte man allerdings die Farbe ändern benötigt man eine "switch" Node. Diese wird nach der Übersetzung der Message aufgerufen. Im Switch wird untersucht welchen Value der Slottype hat und je nach Wert geht es aus unterschiedlichen Ausgängen raus.
Bleibt nur noch an die Ausgänge je ein "out" Node zu setzen und einzustellen, dass die Lampen dann einen Hexwert entsprechend der Farbe bekommen. Möchte man nun mit einem zweiten Slottype arbeiten, um zum Beispiel unterschiedliche Lampen
mit demselben Intent anzusprechen, muss man mit zwei hinter einander geschalteten Switches arbeiten, wodurch der Flow doppelt so groß wird.

### Schritt 3 Testen

Mit den Skills [TextInputWidget](https://ip-team5.intia.de/skills.html#textinputwidget) und [SpeechVisualizer](https://ip-team5.intia.de/skills.html#speechvisualizer) kann man den Skill jetzt hervorragend testen. Es hilft auch an einigen Stellen
im NodeRed Flow "debug" Nodes einzufügen, um die Message zu lesen und zu analysieren. Zum Beispiel war es ein Problem, dass man nicht wusste welcher SlotType zuerst kommt, also zuerst die Farbe oder welche Lampe. Je nach dem muss man dann den
Flow danach ausrichten.

### Bewertung

Unser Skill ist maximal Hard gecodet und damit nicht universell einsetzbar. Wenn man zum Beispiel nur einen anderen Namen einer Lampe hat ändert sich der gesamte Flow und ein großer Teil des DialogueTemplate. Wenn man eine Lampe hinzufügen will,
muss man auch fast alles überarbeiten und an vielen anderen Stellen treten ähnliche Probleme auf.

Von den Hauptenwicklern von ProjectAlice ist es auch gar nicht vorgesehen, dass man viel oder überhaupt mit NodeRed arbeitet. Das Tool soll nur zum testen von Teilfunktionen genutzt werden. Die bessere Lösung wäre alles über Python zu programmieren.
Dies war uns aber aus zeitlichen und wegen einer Menge anderer Aufgaben nicht möglich.










