---
title: Systemweites Wakeword erstellen
sections:
  - Repository clonen
  - Dependencies installieren
  - Samples aufnehmen
  - Modell testen und Empfindlichkeit anpassen
  - Modell hinzufügen
---

Je nachdem welche Wakeword Engine man verwendet gibt es andere Möglichkeiten neue Wakewords hinzuzufügen. Für Snips gibt es dazu ein Hilfsskript.

### Repository clonen

Zunächst clonen wir das Repository welches das Hilfsskript enthält und betreten das Verzeichnis:

```
git clone https://github.com/snipsco/snips-record-personal-hotword.git
cd snips-record-personal-hotword/
```

### Dependencies installieren

Nun müssen wir die Dependencies des Skripts installieren:

```
sudo apt-get install python-numpy python-pyaudio python-soundfile
```

### Samples aufnehmen

Bevor wir mit der Aufnahme starten müssen wir zunächst den ProjectAlice-Dienst stoppen um unser Mikro freizugeben:

```
sudo systemctl stop ProjectAlice
```

Nun starten wir das Hilfsskript mit dem Namen des zu erstellenden Wakewords als Parameter:

```
python script_recording.py your_hotword_name
```

Das Wakeword soll in drei verschiedenen Geschwindigkeiten bzw. Tonlagen gesprochen werden. Eine ruhige Umgebung ist wichtig um ein gutes Modell erstellen zu können. Die Aufnahme startet indem man auf Enter drückt.

Falls Aufnahmen zu lang oder zu verschieden voneinander sind erscheinen Warnungen. Warnung zu (ALSA... and/or jack server...) bei jedem Schritt können ignoriert werden. Die samples werden für ein optimales Ergebnis auch nachbearbeitet.

Wenn das Modell erzeugt ist wird der Pfad wo das Modell liegt vom Skript angegeben. Dieser sollte notiert werden, da er für den nächsten Scritt gebraucht wird.

### Modell testen und Empfindlichkeit anpassen

Bevor das Modell testen sollte Project Alice und die Wakeword-Engine ausgeschaltet sein:

```
sudo systemctl stop snips-hotword
```

Nun kann folgendes Kommando eingegeben werden:

```
snips-hotword --model <path_to_your_model>=<sensitivity>
```

`path_to_your_model` ist der im letzten Schritt generierte Pfad und `sensitivity` ist die Empfindlichkeit. Diese sollte zwischen 0 und 1 liegen. Je höher die Sensitivity ist, desto anfälliger für Fehler ist das Wakeword. Standardmäßig ist die Sensitivity bei `0.5`.

### Modell hinzufügen

Nachdem das Modell ausreichend getestet ist, kann das Modell hinzugefügt werden. `path_to_your_model` sollte das Modell und die erzeugte `config.json` enthalten. 

```
sudo mkdir -p  ~/ProjectAlice/trained/hotwords/<your_hotword_name>; sudo mv <path_to_your_model> ~/ProjectAlice/trained/hotwords/
```

Nun kann die snips.toml Datei angepasst werden:

```
sudo nano /etc/snips.toml
```

Um das Defaultwakeword zu erhalten kann das Model erweitert werden (ansonsten ist der erste Eintrag zu ersetzen):
```
[snips-hotword]
model = ["/home/pi/ProjectAlice/trained/hotwords/snips_hotword=0.53","<new_path_to_your_model>=<sensitivity>"]
```

Wenn alles abgeschlossen ist starten wir ProjectAlice neu.

```
sudo systemctl restart snips-hotword
sudo systemctl restart ProjectAlice
```