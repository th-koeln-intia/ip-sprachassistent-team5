---
title: Was benötige ich an Hardware?
sections:
  - Installation auf einem Rechner
  - Minimalanforderung
  - Smart Home
  - Von uns verwendete Hardware
---

Es ist vorzuziehen Alice auf einem Raspberry Pi zu installieren. Laut Alice selbst läuft Alice auf den Modellen (3a+, 3b, 3b+ und 4b). Dabei [genügen laut Alice][ANFORDERUNG-ALICE] 1GB an RAM. Es werden jedoch mindestens 2GB empfohlen. Die 8GB Variante lohnt sich zur Zeit (November 2020) aufgrund des Preisleistungsverhältnisses nicht.

[ANFORDERUNG-ALICE]: https://docs.projectalice.io/de/setup/requirements.html

### Installation auf einem Rechner

Es sei erwähnt, dass es neben der Installation auf einem Raspberry Pi außerdem noch eine weitere Methode gibt Alice zu installieren.

Die Alice-Community hat eine [Docker-Konfiguration][DOCKER-ALICE-X86-LINUX] bereitgestellt, die es erlaubt Alice auf Linux x86-Rechnern zu verwenden. Es soll laut Entwicklern möglich sein die Konfiguration mit WSL auf Windows lauffähig zu bekommen. Da diese Methode von der Community stammt, gibt es von Project Alice selbst keinen Support dafür.

[DOCKER-ALICE-X86-LINUX]: https://github.com/poulsp/docker-Alice-Linux-

Wir fokussieren uns in dieser Installationsanleitung ausschließlich auf die Installation auf einem Rapsberry Pi.

### Minimalanforderung

Die minimale Hardwareanforderung ist wie anfangs erwähnt ein Raspberry Pi Model 3 mit 1 GB RAM und eine Micro SD Karte mit 8 GB Speicher für das Betriebssystem.

Zusätzliche Mindestanforderungen sind ein Mikrofon und ein Lautsprecher für die Interaktion mit dem Sprachassistenten. Für den Anschluss eines Mikrofons vorhandene Schnittstellen sind entweder USB oder GPIO.

Empfehlenswert für eine deutlichere Spracherkennung ist ein Mic-Array. Wir verwenden u.a. einen ReSpeaker 4-Mic Array welcher mittels GPIO auf dem Raspberry Pi aufgesteckt werden kann, was für Produktionszwecke empfehlenswert ist, da nicht viel Platz verschwendet wird und keine weiteren Kabel benötigt werden.

Eine andere Möglichkeit ist ein USB-Mikrofon zu nutzen wie z.B. ein einfaches Headset. Dadurch benötigt man keinen zusätzlichen Lautsprecher was für Testzwecke praktisch sein kann. Lautsprecher können per Klinkenanschluss oder USB angeschlossen werden. Bluetoothlautsprecher haben wir nicht ausprobiert, müssten jedoch auch funktionieren.

### Smart Home

Für unseren Sprachassistenten verwenden wir außschließlich IoT-Geräte, welche das ZigBee Protokoll unterstützen.

###### Zigbee USB-Gateway
Um mit anderen IoT-Geräten über das ZigBee-Protokoll kommunizieren zu können benötigt man ein USB-Gateway.

Hier eine [Liste][ZigBee-USB] mit verschiedenen unterstützten Möglichkeiten.

[ZigBee-USB]: https://www.zigbee2mqtt.io/information/supported_adapters

###### Benötigte IoT-Geräte

Grundsätzlich kann man auch virtuelle Geräte und Räume erstellen und alles emulieren ohne ein eigenes Gerät dafür kaufen zu müssen.

In unserem Projekt verwenden wir jedoch eine smarte Glühbirne, die das ZigBee Protokoll unterstützt.

### Von uns verwendete Hardware

Da wir unser Projekt zu zweit durchführen haben wir auch zwei verschiedene Konfigurationen als Testumgebung:

###### Konfiguration 1
- Raspberry Pi 4b 4GB RAM (32 GB microSD Karte)
- ReSpeaker 4-Mic Array
- Conbee Stick 2
- Innr RS 230 C-2 Lampen
- Computerboxen mit USB-Stromversorgung 

###### Konfiguration 2
- [Raspberry Pi 3B][RASPBERRY-PI-3B]
- [SanDisk Ultra 16GB microSD Class 10][SANDISK-MICROSD]
- [USB EyeToy Kamera als Mic Array][EYETOY]
- [ZigBee Stick (CC2531) mit Antenne][CC2531]
- Boxen mit Klinkenstecker und externer Stromversorgung

[RASPBERRY-PI-3B]: https://www.raspberrypi.org/products/raspberry-pi-3-model-b/?resellerType=home
[SANDISK-MICROSD]: https://www.amazon.de/SanDisk-Ultra-microSDHC-Class-Speicherkarte/dp/B007JTKKOG
[EYETOY]: https://www.amazon.de/Playstation-PS3-eyetoy-Kamera-Gro%C3%9Fpackung/dp/B00LME2JGQ/ref=asc_df_B00LME2JGQ/?tag=googshopde-21&linkCode=df0&hvadid=310654667276&hvpos=&hvnetw=g&hvrand=11095610371977163915&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9060657&hvtargid=pla-754758627832&psc=1&th=1&psc=1&tag=&ref=&adgrpid=62546410740&hvpone=&hvptwo=&hvadid=310654667276&hvpos=&hvnetw=g&hvrand=11095610371977163915&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9060657&hvtargid=pla-754758627832
[CC2531]: https://de.aliexpress.com/item/4000059514865.html