---
title: Installations- und Bedienungsanleitung
excerpt: Vom leeren Raspberry Pi zum Sprachassistenten Alice
date: 2020-11-23
icon:
  type: fa
  name: fa-paper-plane
color: orange
sections:
  - /installation
  - /benutzeranleitung
  - /funktionen
---

# Installationsanleitungen

**Verwendete Software**
- Raspberry Pi OS Lite (Latest Version)
- BalenaEtcher
- Putty

**Verwendete Hardware**
- Raspberry Pi 4b 4GB RAM
- Conbee Stick 2
- RISP 4 MicArray
- Innr RS 230 C-2 Lampen
- 32 GB SD Karte
- Computer Boxen mit USB-Stromversorgung

**Hardware anschließen evlt mit Bildern**

## Raspberry Pi

**Schritt 1:**
[Raspberry Pi OS Lite](https://www.raspberrypi.org/documentation/installation/installing-images/) downloaden und [BalenaEtcher](https://www.balena.io/etcher/) installieren.

**Schritt 2:**
Die SD Karte muss jetzt so präpariert werden, dass das Betriebsystem sich von der SD Karte selbst installiert, sobald die Karte in den Raspberry Pi gesteckt wird.
Dazu steckt man die SD Karte in den PC und öffnet das Programm BalenaEtcher. Dann wählt man das zuvor heruntergeladene Betriebsytem und die SD Karte aus und klickt auf Flash.
Sobald der Vorgang abgeschlossen ist, enfernt man die SD Karte vom PC und steckt sie erneut ein. Damit man später eine SSH Verbindung herstellen kann erstellt man als nächstes eine neue Datei mit dem Namen "ssh" ohne Dateiendung im root Verzeichnis des Sticks, das jetzt boot heißen sollte.
Wenn man den Raspberry Pi per Wlan mit dem Netzwerk verbinden will, muss man zusätzlich noch eine Datei erstellen mit dem Namen "wpa_supplicant.conf" wieder ohne Dateiendung mit folgendem Text:
```bash
country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid=""
    scan_ssid=1
    psk=""
    key_mgmt=WPA-PSK
} 
```
Man sollte natürlich seine eigene Länderkennung verwenden und die Wlan SSID und Passwort eintragen.

**Schritt 3**
Die SD Karte aus dem Rechner entfernen und in den Raspberry Pi einstecken. Der Raspberry Pi installiert sich ganz von allein.
 
## SSH Verbindung herstellen
Hierzu wird [Putty](https://www.putty.org/) verwendet. Nach der Installation öffnet man Putty und trägt die IP Adresse des Raspberry Pi ein.
Die IP Adresse findet man heraus, wenn man in die Einstellungen des Routers geht. Bei einer FritzBox zum Beispiel geht das über den Browser mit "fritz.box" in der Navigationsleiste.
In den meisten Routern kann man auch eine statische IP-Adresse für den Raspberry Pi vergeben, dann muss man nicht immer die IP-Adresse neu herausfinden. Mit "Open" öffnet man die SSH-Verbindung und landet im Terminal des Pi. Die Anmeldedaten sind per default Benutzername "pi" mit dem Passwort "raspberry".

## Alice installieren und konfigurieren

Git installieren mit: `sudo apt-get install git -y`

Alice klonen mit: `git clone https://github.com/project-alice-assistant/ProjectAlice.git`

Die Konfigurationsdatei für die Ersteinrichtung kopieren mit: `sudo cp ~/ProjectAlice/ProjectAlice.yaml /boot/ProjectAlice.yaml`

Und kofigurieren: `sudo nano /boot/ProjectAlice.yaml`

Es öffnet sich eine große Datei mit allen möglichen Einstellungen. Wichtig ist das richtige Input Device einzustellen und die Spracherkennung mit der Länderkennung einzustellen, allerdings kann man alle Einstellungen später in einer übersichtilichen Browser UI noch ändern.
Nachdem man fertig ist mit den Einstellungen bleibt nur noch Alice zu starten: 
`cd ~/ProjectAlice`
`python3 main.py`

Den Startvorgang kann man beobachten mit: `tail -f /var/log/syslog`

Nach langer Zeit sollte über die Boxen ein "Ding" zu hören sein. Das bedeutet Alice ist bereit.

Man kann über einen PC im selben Netzwerk eine UI im Browser aufrufen. Diese findet man unter `<ip>:5000` . Im Bereich "ADMIN" findet man die Einstellungen aus der Grundkonfiguration und kann diese ändern. Den Bereich betritt man mit dem Benutzernamen "ADMIN" und dem Passwort: "1234".

## Lampen über das Netzwerk steuern

Um zu testen, ob der Conbee 2 Stick die Lampen ansteuern kann, kann man auf dem Raspberry Pi deCONZ installieren und dann mit Phoscon die Lampen über das Netzwerk suchen und ansteuern.

**deCONZ installieren**

Für den Conbee 2 Stick muss zuerst die passende deCONZ Firmware heruntergeladen werden. Dazu führt man den Befehl `wget https://deconz.dresden-elektronik.de/deconz-firmware/deCONZ_Rpi_0x26390500.bin.GCF` in der SSH-Shell des Pi's aus.

Dann flasht man die Firmware mit `sudo GCFFlasher_internal -t 60 -d /dev/ttyACM0 -f deCONZ_ConBeeII_0x26660700.bin.GCF`

Und zuletzt startet man das Programm `sudo systemctl start deconz`

Für Troubleshooting und andere geräte zum Beispiel RaspBee 2 kann [diese Anleitung](https://github.com/dresden-elektronik/deconz-rest-plugin/wiki/Update-deCONZ-manually) weiterhelfen.

**Phoscon nutzen**

Die [Phoscon App](http://phoscon.de/app) ruft man ganz einfach über den Browser auf. Nachdem man ein Passwort festgelegt hat und seine Lichter gesucht und gefunden hat, kann es schon losgehen. Von hier aus kann man manuell die Farbe, Sättigung und Helligkeit ändern, den einzelnen Lampen verschiedene Namen geben und in Gruppen zuordnen und noch vieles mehr.

Wenn deCONZ und Alice gleichzeitig auf dem Pi laufen kann es zu Problemen bis zum Absturz des Pi's kommen. Mehr dazu im [Troubleshoot](https://ip-team5.intia.de/projekt.html).











