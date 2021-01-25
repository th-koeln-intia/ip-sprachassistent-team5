---
title: Skills, die bei der Installation von Alice installiert werden
sections:
  - DevMode freischalten und "leeren" Skill erstellen
  - Entwicklungsumgebungen
  - Hallo Welt Skill
---

### DevMode freischalten und "leeren" Skill erstellen

Der erste Schritt ist der wahrscheinlich leichteste und hat ein vergleichsweise großes Ergebnis

Den DevMode findet man im Admin-Bereich der Web-Oberfläche (Der Standart Benutzer ist "ADMIN" und das Standart Passwort ist "1234"). Sobald man den Schalter aktiviert hat erscheint ein neuer
TAB "DEVMODE" unter dem "ADMIN"-TAB. In diesem Bereich kann man sich einfach einen Skill erstellen. Hierbei brauch man einen Namen und man muss mindestens die Sprache Englisch unterstützen. Der 
Rest ist erstmal nicht interessant und für unseren Skill war es auch nicht relevant.

Nach einem Neustart von Alice (vorzugsweise über eine SSH-Verbindung mit 'sudo systemctl restart ProjectAlice'), erscheint der Skill in der Web-Oberfläche im Bereich "SKILLS". Unser Skill war 
"disabled" und konnte nicht enabled werden. Die Lösung war die Datei .py im Ordner skills/LightsController/widget zu löschen. [Nachzulesen hier](https://github.com/project-alice-assistant/ProjectAlice/issues/359)

### Entwicklungsumgebungen

Auf der Seite von Alice gibt es eine [Anleitung für Pycharm](https://docs.projectalice.io/community-made/getting-started-pycharm.html). Pycharm kann man seinem git-Accout verkünpfen und so
versioniert mit mehreren Entwicklern an seinem Skill arbeiten. Zum testen auf einem Raspberry Pi muss man allerdings jedesmal den git Ordner auf dem Pi updaten.

Deshalb haben wir für den LightsController [Visual Studio Code](https://code.visualstudio.com/download) mit den Erweiterungen für [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 
und für die [Entwicklung über eine SSH-Verbindung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) verwendet. Wenn alles installiert ist,
kann man die Entwicklungsumgebung mit dem Raspberry Pi über SSH verbinden. Dazu klickt man unten links auf das grüne Symbol (oder F1) und gibt "Remote-SSH: Connect to Host..." ein.
Dann gibt man <user>@<hostname> ein. Standart Username beim Raspberry Pi ist "pi" und der hostname ist in der Regel die IP-Adresse im Heimnetzwerk. Man wird dann nach einem Host gefragt, das
ist der eigene PC. Wenn man sich dann verbindet wird man noch nach dem Passwort gefragt und dann landet man auf dem Raspberry Pi.

Diese Methode war für uns einfacher, weil wir so schneller und einfacher den Skill testen konnten. Man muss nur die geänderten Dateien speichern und dann Alice neustarten im Terminal von
VS Code mit 'sudo systemctl restart ProjectAlice'. Dann kann man den Skill über Sprache testen oder noch einfacher und schneller mit den Skills 
[TextInputWidget](https://ip-team5.intia.de/skills.html#textinputwidget) und [SpeechVisualizer](https://ip-team5.intia.de/skills.html#speechvisualizer).


### Hallo Welt Skill

Der Hallo Welt Skill soll einen Satz erkennen und einen Satz antworten. Damit hat man die absoluten Basics die ein Skill können muss. Dazu muss man in dem Grundgerüst des Skills, 
dem "leeren" Skill, drei Dateien ändern.

##### Talk-file

Im Ordner ProjectAlice/skills/LightsController(MySkill) findet man einen Ordner der "talks" heißt. Hier findet man .json Dateien, eine für jede unterstützte Sprache, die man zuvor ausgewählt hat.
In einem Talk-file stehen Sätze die Alice sagen kann wenn sie einen Intent erkennt. Für den Hallo Welt Skill verändern wir die de.json Datei, dass nur noch folgendes enthalten ist:

```
{
	"halloWeltAntwort": [
		"Hallo du wunderschöne Welt"
	]	
}
```

"halloWeltAntwort" benötigen wir später im SourceCode und "Hallo du wunderschöne Welt" ist das, was der Sprachassistent später antworten wird.

##### Dialogue-file

Im selben Verzeichnis wie der talks Ordner findet man auch einen "dialogueTemplate" Ordner. Hier sind wieder .json Dateien für jede unterstützte Sprache enthalten und zusätzlich eine .sample Datei
für jede unterstützte Sprache. Uns interessiert erst mal die de.json Datei. Diese sollte folgendes enthalten:
```
{
	"skill": "MySkill",
	"slotTypes": [],
	"intents": [
		{
			"name": "halloWeltAnfrage",
			"enabledByDefault": true,
			"utterances": [
				"Hallo Alice im Wunderland"
			],
		}
}
```

Bei "MySkill" sollte der name des Skills stehen, den man am Anfang beim Erstelle gewählt hat. "slotTypes" sind leer und werden später erklärt. "halloWeltAnfrage" ist der Name des Intents. 
Dieser wird später in MySkill.py benötigt und wird auch im Webinterface angezeigt, wenn man bei Skills auf Intents ansehen klickt. Bei "utterances" stehen all jene Sätze die der 
Sprachassistent bzw. die NLU verstehen soll, hier nur "Hallo Alice im Wunderland".

##### MySkill.py

Die letzte Datei die für den Hallo Welt Skill modifiziert werden muss ist die <NameDesSkills>.py Datei. Hier sollte mindestens folgendes stehen:
```
class MySkill(AliceSkill):

	@IntentHandler('halloWeltAnfrage')
	def halloWeltIntent(self, session: DialogSession, **_kwargs):
		self.endDialog(session.sessionId, self.randomTalk(text='halloWeltAntwort'))
```

Es wird eine Klasse "MySkill" erstellt mit einer Funktion "halloWeltIntent". Der IntentHandler ruft diese Funktion auf, wenn der Intent "halloWeltAnfrage" von der NLU erkannt wurde. Die
Funktion bekommt unter anderem die Dialogsession übergeben. Daraufhin beendet die Funktion den Dialog mit einer zufälligen Antwort aus dem Talk File. In diesem Fall gibt es dort
nur eine Antwort nämlich: "Hallo du wunderschöne Welt".


##### Ergebnis

Nachdem man nun die Dateien gespeichert hat und ProjectAlice neugestartet hat, kann man das WakeWord nennen und dann sagen "Hallo Alice im Wunderland". Wenn der Satz korrekt erkannt wurde,
wird der Sprachassistent anworten: "Hallo du schöne Welt".

Auf Basis dieses Wissens könnte man zum Beispiel seinen eigenen Witze Skill schreiben. Mit utterances wie: "Erzähl mir einen Witz" oder "Mach einen Witz" und talks wie: "Ein Ball rollt um
die Ecke und fällt um" oder "trafen sich zwei Jäger beide tot".








