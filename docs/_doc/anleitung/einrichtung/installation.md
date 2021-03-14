---
title: Installation
sections:
  - Installation und Konfiguration des Basissystems
  - Installation von Alice
---

Falls noch kein Betriebssystem auf der SD-Karte des Pi installiert ist oder eine frische Neuinstallation gewünscht ist, ist der Schritt [Installation und Konfiguration des Basissystems](#installation-und-konfiguration-des-basissystems) notwendig. Andernfalls kann dieser Teil übersprungen werden und es kann sofort mit der [Installation von Alice](#installation-von-alice) begonnen werden.

### Installation und Konfiguration des Basissystems

Das Betriebssystem was sich am besten für eine Installation von Project Alice eignet ist Raspberry Pi OS. Es ist möglich, dass andere Debian-Distributionen auch gut funktionieren jedoch können nach aktuellem Stand (März 2021) neuere Paketquellen oder andere Paketmanager problematisch für eine Installation sein. Die Minimalversion von Raspberry Pi OS reicht nach eigenen Versuchen aus.

###### Offizielle, vorgefertigte Images für den Pi

Wir werden nachdem wir den Pi neu aufgesetzt und konfiguriert haben Alice manuell installieren.

Es gibt aber noch die Möglichkeit ein vorgefertigtes Image inkl. Alice Installation auf die SD-Karte zu flashen. Da das Projekt noch immer in einer Beta-Phase ist, wurden für die letzten Beta-Versionen jedoch keine vorgefertigten Images erstellt. Dies wird sich laut Entwicklerteam jedoch ab der Veröffentlichung von Version 1.0 ändern.

Bis dahin ist eine manuelle Installation die empfohlene Installationsvariante.

###### Flashen der SD-Karte

Die SD-Karte kann mithilfe des [Raspberry Pi Imagers][RASPBERRY_PI_IMAGER] geflasht werden, welches eine plattformunabhängige Möglichkeit darstellt. Man wählt das gewünschte Image im Imager aus, dieses wird anschließend heruntergeladen und auf die ausgewählte SD-Karte geflasht. Mit dem Raspberry Pi Imager lassen sich außerdem auch fremde Images flashen.

[RASPBERRY_PI_IMAGER]: https://www.raspberrypi.org/software/

Es kann jedoch auch ein anderes Flashing-Tool verwendet werden Unter Linux und Mac gibt es verschiedene Open Source GUI-Anwendungen, es lässt sich aber auch `dd` in der Kommandozeile verwenden. Unter Windows gibt es u.a. [Win32DiskImager][WIN32DISKIMAGER] und [Rufus][RUFUS]. 

[WIN32DISKIMAGER]: https://sourceforge.net/projects/win32diskimager/
[RUFUS]: https://rufus.ie/

###### SSH und WLAN einrichten

Nachdem die SD-Karte geflasht ist muss um auf den Raspberry Pi ganz ohne Monitor zuzugreifen zu können der SSH-Server zunächst aktiviert werden. Dazu erstellt man in `/boot` eine leere Datei namens `ssh`.

Um auch auf den Ethernet-Anschluss zu verzichten lohnt es sich auch sofort das WLAN zu konfigurieren. Dazu erstellt man ebenfalls in `/boot` eine Datei namens `wpa_supplicant.conf` mit folgender Strutkur:
```
country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="ToBeReplaced"
    scan_ssid=1
    psk="mySecretPsk"
    key_mgmt=WPA-PSK
}
```

###### Anmeldung per SSH und erste Schritte

Nun kann man den Pi anschalten und sich per SSH anmelden. Der zum Login erforderliche Benutzername ist standardmäßig `pi` und das Standardpasswort lautet `raspberry`.

Um eine SSH-Verbindung aufzubauen kann man unter Windows entweder PuTTY, den Fork KiTTY oder auch neuerdings direkt wie unter Linux und Mac den ssh-Befehl im Terminal nutzen:

```
ssh pi@raspberrypi
```

Das Passwort lässt sich mit `passwd` ändern. Als nächstes ist es wichtig das System auf den neusten Stand zu bringen. Dies tut man mit `sudo apt-get update` gefolgt von `sudo apt-get dist-upgrade -y`.

###### Weitere Konfiguration mit Raspi-Config

Im Konfigurationstool `sudo raspi-config` lassen sich weitere Dinge konfigurieren wie Sprache, Tastatur, Hostname und Zeitzone.

![raspi-config](assets/images/raspi-config.png){: .img-responsive}

Um die GUI zu deaktivieren kann Boot / Auto Login auf `Console …` gesetzt werden. In `Interface Options` sollte SPI und I2C aktiviert werden. Anschließend sollte noch das Dateisystem unter `Advanced Options` mit `Expand Filesystem` vergrößert werden.

Nun kann das System neugestartet werden.

### Installation von Alice

Alice ist noch in Beta und unterliegt kontinuierlicher Veränderung. Die Zielgruppe sind aktuell alle, die grundlegendes Wissen zu ihren Geräten haben, Systemlogs lesen und Python Module installieren können.

###### Installation mithilfe von Docker

Neben der x86-Docker-Konfiguration gibt es außerdem noch eine [Konfiguration][DOCKER-ALICE-ARM] speziell für ARM-Architekturen (Raspberry Pi etc.). Diese haben wir selbst nicht ausprobiert. Alternativ zu einer manuellen Installation kann ab diesem Punkt Alice mithilfe von Docker installiert werden. Dazu gibt es ein [Github-Repo][DOCKER-ALICE-ARM] mit einer Anleitung zur Installation.

[DOCKER-ALICE-ARM]: https://github.com/project-alice-assistant/project-alice-docker

###### Git installieren und Alice clonen

Zunächst einmal muss (falls noch nicht vorhanden) git installiert werden:

```
sudo apt-get install git -y
```

Danach kann man auch das Repo von Project Alice im Homeverzeichnis clonen:
```
cd
git clone https://github.com/project-alice-assistant/ProjectAlice.git
```

###### Alice Konfigurieren

Vor dem Starten der Installation muss erst einmal die Konfiguration vorgenommen werden. Dazu kopiert man die Konfigurationsdatei `ProjectAlice.yaml` ins `/boot`-Verzeichnis.

```
sudo cp ~/ProjectAlice/ProjectAlice.yaml /boot/ProjectAlice.yaml
```

Nun kann man die Konfigurationsdatei mit dem Editor seiner Wahl bearbeiten. Beispielsweise mit `sudo nano /boot/ProjectAlice.yaml`.

Es lässt sich ein Mikrofontreiber von vielen auswählen, der automatisch installiert wird (ReSpeaker etc.) aber auch Sprache, Regionales, Techstack, Offlinetauglichkeit usw. einstellen. Einiges davon kann auch anschließend im Webinterface noch einmal angepasst werden.

Die Konfigurationsdatei ist im YAML-Format. Damit die Installation reibungslos verläuft muss sichergestellt werden das zwischen `:` und Wert ein Leerzeichen ist: 
&nbsp; `❌ key:value` &nbsp; `✔️ key: value`

###### Alice starten

Nun muss nur zum Repository gewechselt werden und das Python-Script gestartet werden.

```
cd ~/ProjectAlice
python3 main.py
```

Im Hintergrund wird anschließend die Installation vorgenommen, dies erfordert eine Internetverbindung, da die Treiber und weiteren Softwarekomponenten nicht im Repo enthalten sind und aus dem Netz geladen werden müssen. Alle für Alice benötigten Dienste werden eingerichtet, sodass beim nächsten Neustart alles von alleine startet und im Hintergrund läuft.

Nachdem Alice als eigener Dienst eingerichtet worden ist und im Hintergrund läuft, sieht man keine Ausgaben mehr in der Konsole. Dafür kann man aber die Logs überprüfen: `tail -f /var/log/syslog`.

Bei eingeschalteten Lautsprechern hört man beim Start von Alice einen kurzen Ton.

Es ist wichtig bei der ersten Installation zu warten bis alles was im Hintegrund geschieht wirklich zu Ende ist. Denn selbst nach Neustart werden noch weitere Sachen geladen und u.a. die NLU trainiert.

Falls Alice nicht startet gibt es einen [Troubleshooting Guide][TROUBLESHOOTING_GUIDE] von Alice selbst, der weiterhelfen kann.

[TROUBLESHOOTING_GUIDE]: https://docs.projectalice.io/setup/troubleshooting