---
title: Alice startet immer wieder neu
sections:
  - Beim ersten Start nach der Installation
  - Bei Fehlkonfiguration
---

Es kann passieren, dass Alice <small>(Version 1.0 Beta 4)</small> es aufgrund eines Fehlers nicht schafft vollständig zu booten und ständig neu startet. Falls Alice in einem Reboot-Cycle gefangen ist, kann das verschiedene Gründe haben. Dies kann sofort nach der Installation passieren üblicherweise aber auch nach dem Ändern bestimmter Einstellungen. Um den Grund dafür herauszufinden kann ein Blick in die Logfiles hilfreich sein.

```
less /var/log/syslog
```

### Beim ersten Start nach der Installation

Wir sind auf folgende Situationen gestoßen bei denen Alice beim ersten Start nach einer Neuinstallation immer wieder neustartet:

#### Kein Mikrofon

Während der Installation muss genau ein Treiber für das Mikrofon angegeben werden. Dieser wird dann bei der Installation heruntergeladen und installiert. Falls beim Neustart nach der Installation kein Mikrofon erkannt wird, da entweder der falsche Treiber bei der Installtion ausgewählt worden ist oder einfach kein Mikrofon angesteckt oder per Bluetooth verbunden ist, dann kann dies ein Grund dafür sein, dass Alice immer wieder neu startet.

#### Raspberry Pi OS Minimalimage und fehlende Abhängigkeit

In Alice wir standardmäßig Hermes LED installiert. Es kann jedoch sein, dass Hermes LED nicht startet weil das [Python-Package GPIO Zero][GPIO_ZERO] nicht installiert ist, das für die Ansteuerung der LEDs gebraucht wird. Falls Hermes LED nicht startet, kommt Alice in ein Reboot-Cycle bis Hermes LED wieder erfolgreich startet.

[GPIO_ZERO]: https://gpiozero.readthedocs.io/en/stable/index.html

```
Dec 10 12:38:35 alice python[13668]: Traceback (most recent call last):
Dec 10 12:38:35 alice python[13668]:   File "main.py", line 135, in <module>
Dec 10 12:38:35 alice python[13668]:     main()
Dec 10 12:38:35 alice python[13668]:   File "main.py", line 120, in main
Dec 10 12:38:35 alice python[13668]:     slc = HermesLedControl(args)
Dec 10 12:38:35 alice python[13668]:   File "/home/pi/hermesLedControl/models/HermesLedControl.py", line 135, in __init__
Dec 10 12:38:35 alice python[13668]:     self._ledsController = LedsController(self)
Dec 10 12:38:35 alice python[13668]:   File "/home/pi/hermesLedControl/models/LedsController.py", line 51, in __init__
Dec 10 12:38:35 alice python[13668]:     if not self.initHardware():
Dec 10 12:38:35 alice python[13668]:   File "/home/pi/hermesLedControl/models/LedsController.py", line 145, in initHardware
Dec 10 12:38:35 alice python[13668]:     from interfaces.pureGPIO import PureGPIO
Dec 10 12:38:35 alice python[13668]:   File "/home/pi/hermesLedControl/interfaces/pureGPIO.py", line 1, in <module>
Dec 10 12:38:35 alice python[13668]:     from gpiozero import LED
Dec 10 12:38:35 alice python[13668]: ModuleNotFoundError: No module named 'gpiozero'
Dec 10 12:38:35 alice systemd[1]: hermesledcontrol.service: Main process exited, code=exited, status=1/FAILURE
Dec 10 12:38:35 alice systemd[1]: hermesledcontrol.service: Failed with result 'exit-code'.
Dec 10 12:38:40 alice systemd[1]: hermesledcontrol.service: Service RestartSec=5s expired, scheduling restart.
Dec 10 12:38:40 alice systemd[1]: hermesledcontrol.service: Scheduled restart job, restart counter is at 6509.
Dec 10 12:38:40 alice systemd[1]: Stopped Hermes Led Control.
Dec 10 12:38:40 alice systemd[1]: Started Hermes Led Control.
```

Die fehlende Abhängigkeit, die zum Neustart führt ist standardmäßig beim Defaultimage von Raspberry Pi OS aber vorinstalliert. Das Minimalimage des Raspberry Pi OS jedoch installiert es nicht mit. Da Hermes LED diese Abhängigkeit nicht selbst nachläd falls sie nicht installiert ist muss dies manuell geschehen, damit Alice wieder starten kann.

##### Globale Installation mit Paketverwaltung des Systems

Unter Raspberry Pi OS lässt sich GPIO Zero mit der Paketverwaltung des Systems nachinstallieren. Unter anderen Distributionen muss geschaut werden welcher Paketmanager verwendet wird (nicht debian/ubuntu-basierte Images verwenden kein apt) und schauen ob sich das Paket in den Paketquellen befindet und vor allem wie es dort heißt.

```
sudo apt update
sudo apt install python3-gpiozero
```

Es kann jedoch sein, dass Hermes LED trotz global installierter Abhängigkeit immer noch nicht funktioniert.

##### Installation in der virtuellen Umgebung von Hermes LED

Falls man ein andere Distribution nutzt oder die globale Installation nichts bringt, kann die Abhängigkeit auch direkt in der virtuellen Umgebung von Hermes LED nachinstalliert werden.

```
~/hermesLedControl/venv/bin/pip3 install gpiozero
```

### Bei Fehlkonfiguration

Durch Fehlkonfigurationen ist es auch möglich, dass Alice in ein Reboot-Cycle kommt. Ähnlich wie beim Hermes LED Problem kann der Grund oft dafür sein, dass eine benötigte Softwarekomponente nicht startet. Dies muss in jedem Fall individuell in den Log-Files überprüft werden.

#### Kein Fallback

Wenn man beispielsweise eine nicht funktionierende ASR auswählt und als Fallback dieselbe ASR verwendet, dann startet Alice nicht mehr bis man dies manuell wieder rückgängig macht. Das Webinterface ist nicht lange genug verfügbar um die Einstellung darüber rückgängig zu machen.

Oft kommt man in ein Reboot-Cycle wenn man Snips als ASR auswählt aber Deutsch als ASR-Sprache gewählt hat oder Google verwendet obwohl man keine Credentials-Datei hinterlegt hat.

Die Konfigurationen befinden sich im JSON-Format in der Datei `~/ProjectAlice/config.json`.

```
sudo nano ~/ProjectAlice/config.json
```

In der Datei `~/ProjectAlice/configTemplate.json` findet man die Standardwerte und möglichen Einstellungswerte. Für **asr** und **asrFallback** sind das momentan <small>(Version 1.0 Beta 4)</small>:
- deepspeech
- pocketsphinx
- google
- snips <small>(nur Englisch)</small>