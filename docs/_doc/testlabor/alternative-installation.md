---
title: Alternative Installationsversuche
sections:
  - Installation am PC mit Docker
  - Installation am PC mit Xubuntu und VMWare Workstation
  - Installation am PC mit Raspberry Pi Desktop und VMWare Workstation
  - Mehrfachinstallation am Pi mit BerryBoot
---

Neben der Installation im Guide haben wir weitere Installationsversuche unternommen. Da wir jeweils nur eine SD-Karte hatten und das mehrfache Flashen mühsam sein kann, haben wir versucht Alice am PC mit Docker und in einer VM zu installieren sowie eine Installation am Pi mit BerryBoot durchgeführt.

Nur letzteres war erfolgreich. BerryBoot hat uns insgesamt mehr Flexibilität beim Testen gebracht. Durch eine integrierte Backupfunktion der Images können wir damit verschiedene Versionen von Alice im funktionieren Zustand freezen und später wiederherstellen.

Diese Sicherheit ist in unseren Fall sehr wichtig, da wir verschiedenes an Alice ausprobiert haben und es immer sein kann, dass Alice plötzlich nicht mehr funktioniert.

Dies ist zu erwarten, da wir viel mehr ausprobieren als der gewöhnliche User. Dies sollte jedoch kein Problem mehr sein, wenn Alice aus der Betaphase gelangt. Denn in den nächsten Versionen inkl. Release Candidates erfolgt ein Bug Hunting, dass aus Alice eine noch ausgereiftere Lösung machen soll.

### Installation am PC mit Docker

Eine Installation auf x64-Rechnern soll mit einer von der Community erstellten [Docker-Konfiguration](https://github.com/poulsp/docker-Alice-Linux-x86.git) möglich sein. Unser Versuch ist leider gescheitert, da diese Konfiguration zur Zeit nur mit der Google ASR und Snips als Fallback sowie Amazon Polly für TTS funktioniert.

### Installation am PC mit Xubuntu und VMWare Workstation

Eine weitere Idee war es eine virtuelle Machine mit VMWare Workstation aufzusetzen. Da Raspbian debianbasiert ist haben wir zuerst auf das Debian-Derivat Xubuntu gegriffen. Bei der Installation hatten wir einige Schwierigkeiten, da Ubuntu aktuellere Software anbietet als Debian. Wir mussten manuell Python 3.7 anstelle von 3.8 mithilfe von PPAs nachinstallieren.

Aus irgendeinem Grund wurde beim Erzeugen der virtuellen Umgebung pip nicht mitinstalliert. Dafür musste man eigenhändig Symlinks im `venv` erstellen. Das nächste Problem war dass das Installationsskript `sudo` Befehle aussführt welche bei Raspberry Pi Images keine Eingabe des Passworts erfordern. Bei Ubuntu schon, daher konnte die Installation wieder nicht fortgesetzt werden. Dazu musste man die sudoers-File entsprechend anpassen.

Im Anschluss lief die Installation erfolgreich weiter sodass ein Systemd-Dienst erstellt worden ist. Dieser Dienst installiert wiederum weiter Dinge nach. Es sind mehrere Installationsschritte, die ausgeführt werden. Das Problem war jedoch dass der zweite Installationsschritt immer wiederholt wurde und die restliche Installation nicht durchgeführt worden ist. Den Grund dafür haben wir nicht weiter erforscht, da wir am Ende davon ausgegangen sind, dass die Installation von Alice nicht für Ubuntu angepasst ist. 

### Installation am PC mit Raspberry Pi Desktop und VMWare Workstation

Anstatt Debian zu nutzen haben wir für eine optimale Kompatibilität die Desktop-Version für Raspberry Pi OS installiert: [Raspberry Pi Desktop](https://www.raspberrypi.org/software/raspberry-pi-desktop/). Hier gab es keine Probleme mit den Paketquellen und die sudoers-Konfiguration war identisch wie beim Pi. Die Installation ist bis zum Ende durchgelaufen (auch wenn es ein paar Fehlermeldungen dabei gab, die nicht weiter erforscht worden sind). Ein Problem war hier, dass das Mikrofon über Pulseaudio nicht erkannt worden ist.

Aus Zeitgründen haben wir diesen Versuch leider unterbrochen und den nächsten Versuch mit BerryBoot gewagt.

### Mehrfachinstallation am Pi mit BerryBoot

Mit BerryBoot lässen sich mehrere Images auf einmal installieren. Diese können entweder alle auf der SD-Karte selbst oder auf ein externes Medium gespeichert werden. Das externe Medium kann z.B. ein einfacher USB-Stick sein aber auch ein SSD-Speicher ist möglich und sogar zu empfehlen.

BerryBoot erhöht die Flexibilität des Systems, da es nicht nötig ist verschiedene SD-Karten zu flashen bzw. die SD-Karte mehrmals zu flashen. Man hat beim Boot die Auswahl zwischen mehreren installierten Images. Diese kann man mit wenigen Klicks verwalten. Images kann man online nachinstallieren oder mittels spezieller Image-Files per USB-Stick nachflashen. Es ist möglich ein Abbild einer Installation zu erstellen und dieses später wiederherzustellen. Es ist außerdem möglich mehrere Instanzen davon zu erstellen. Ein Beispielszenario wäre die Installation zweier Instanzen der Beta Version von Alice mit verschiedenen Techstack oder unterschiedlichen Spracheinstellungen. Wir hatten beispielsweise bei der Beta 4 Probleme mit dem Umschalten von Deutsch auf Englisch.

###### Vorbereitungen

Zunächst müssen alle Partitionen auf der SD Karte gelöscht werden und eine große FAT32 erstellt werden. Falls dies der Fall ist, muss die Partition trotzdem formatiert werden sodass keine Dateien vorhanden sind.

Anschließend muss BerryBoot heruntergeladen werden. Auf Ihrer [SourceForge Seite](https://sourceforge.net/projects/berryboot/files/) gibt es BerryBoot als Zip für den Pi 4 ([pi4](https://sourceforge.net/projects/berryboot/files/berryboot-20201103-pi4.zip/download)) und ältere Pis ([pi0-pi1-pi2-pi3](https://sourceforge.net/projects/berryboot/files/berryboot-20190612-pi0-pi1-pi2-pi3.zip/download)). Die passende Zip ist herunterzuladen und in die neuformatierte Partition zu entpacken.

Falls eine [Headlessinstallation über VNC](https://www.berryterminal.com/doku.php/berryboot/headless_installation) gewünscht ist muss die Datei `cmdline.txt` erweitert werden. Bei einer Installation über WLAN auch die Datei `wpa_supplicant.conf`.

cmdline.txt
```
elevator=deadline quiet bootmenutimeout=10 qmap=de vncinstall ipv4=192.168.178.50/255.255.255.0/192.168.178.1/wlan0
```

wpa_supplicant.conf
```
country=DE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
ap_scan=1

network={
    ssid="to-be-replaced"
    psk="my-secret-psk"
}
```

Nun kann die SD-Karte eingesetzt werden und die Installation vorgenommen werden. Bei einer Headless-Installation benötigt man einen VNC-Client.

###### Installation von Images

Images können entweder online oder über einen USB-Stick installiert werden. Da bei den älteren Pis es Online kaum Images mehr gibt bleibt nur die Installation per USB-Stick. Dafür benötigt man spezielle BerryBoot Images, die man entweder [hier](https://berryboot.alexgoldcheidt.com/images/) bekommt oder unter einem unix-ähnlichen Betriebssystem selbst erstellt/umwandelt.

Bei einem langen Rechtsklick auf `Add OS` sieht man erst die Option von einem USB-Stick zu installieren. Man wählt das richtige Image aus und startet mit der Installation. Dies kann einige Minuten in Anspruch nehmen.

![Image per USB installieren](assets/images/berryboot/install-from-usb.png){: .img-responsive}