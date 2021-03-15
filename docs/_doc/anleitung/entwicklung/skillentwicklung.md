---
title: Skillentwicklung
sections:
  - Einen leeren Skill erstellen
  - Entwicklungsumgebungen
  - Hallo Welt Skill
---

Eine aktuelle und ausführliche [Anleitung zur Skillentwicklung](https://docs.projectalice.io/skill-development/) findet man in der Dokumentation von ProjectAlice selbst.

### Einen leeren Skill erstellen

Sobald man den Devmode aktiviert hat erscheint ein neuer TAB "DEVMODE" unter dem "ADMIN"-TAB. In diesem Bereich kann man sich einfach einen Skill erstellen. Hierbei brauch man einen Namen und man muss mindestens die Sprache Englisch unterstützen. Der 
Rest ist erstmal nicht interessant und für den ersten Skill. Nach einem Neustart von Alice (vorzugsweise über eine SSH-Verbindung mit 'sudo systemctl restart ProjectAlice'), erscheint der Skill in der Web-Oberfläche im Bereich "SKILLS".

### Entwicklungsumgebungen

Auf der Seite von Alice gibt es eine [Anleitung für Pycharm](https://docs.projectalice.io/community-made/getting-started-pycharm.html). Pycharm kann man seinem git-Accout verkünpfen und so
versioniert mit mehreren Entwicklern an seinem Skill arbeiten. Zum testen auf einem Raspberry Pi muss man allerdings jedesmal den git Ordner auf dem Pi updaten.

Eine andere Variante ist [Visual Studio Code](https://code.visualstudio.com/download) mit den Erweiterungen für [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) 
und für die [Entwicklung über eine SSH-Verbindung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). Wenn alles installiert ist,
kann man die Entwicklungsumgebung mit dem Raspberry Pi über SSH verbinden. Dazu klickt man unten links auf das grüne Symbol (oder F1) und gibt "Remote-SSH: Connect to Host..." ein.
Dann gibt man <user>@<hostname> ein. Standart Username beim Raspberry Pi ist "pi" und der hostname ist in der Regel die IP-Adresse im Heimnetzwerk. Man wird dann nach einem Host gefragt, das
ist der eigene PC. Wenn man sich dann verbindet wird man noch nach dem Passwort gefragt und dann landet man auf dem Raspberry Pi. Der Vorteil bei VS Code ist, dass man den Skill häufiger testen kann, wenn man allerdings mit vielen Entwicklern zusammen arbeitet ist die Versionierung und das zusammenspiel mit GIT etwas mühsam.

### Hallo Welt Skill

Der leere Skill soll jetzt mit möglichst einfachem Inhalt gefüllt werden. Im Ergebnis soll der Sprachassistent auf einen erkannten Satz einen anderen antworten. Damit hat man die absoluten Basics die ein Skill können muss.
Folgende drei Dateien müssen hierzu geändert werden.

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

Bei "MySkill" sollte der Name des Skills stehen, den man am Anfang beim erstellen gewählt hat. "halloWeltAnfrage" ist der Name des Intents. 
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
die Ecke und fällt um" oder "trafen sich zwei Jäger beide tot". Oder man könnte den Skill [RandomUselessFacts](https://ip-team5.intia.de/skills.html#randomuselessfacts) nach programmieren.







