---
title: Vorraussetzungen
---

Für die Installation, Troubleshooting etc. benötigt man grundlegende Kenntnisse über die Kommandozeile unter Unix-ähnlichen Betriebssystemen. Eine gute Einführung in das Thema bietet [linuxcommand.org](http://linuxcommand.org/index.php).

Darüber hinaus kann es hilfreich sein grundlegendes Wissen über [pip](https://packaging.python.org/tutorials/installing-packages/) und [virtuelle Umgebungen](https://docs.python.org/3/tutorial/venv.html) unter Python zu haben. Wir haben das zum Beispiel gebraucht, da bei einem Installationsversuch eine Abhängigkeit von Hermes LED Control nicht mitinstalliert worden ist. Im Homeverzeichnis findet man ~/ProjectAlice und ~/hermesLedControl, welche beide virtuelle Umgebungen haben. 

Um Dienste im Hintegrund läufen zu lassen verwendet Raspbian OS systemd. Hier wäre es hilfreich die wichtigsten Optionen des [systemd](https://www.digitalocean.com/community/tutorials/systemd-essentials-working-with-services-units-and-the-journal)-Kommandos zu kennen um Hintegrunddienste beenden und neustarten zu können.

Darüber hinaus ist es wichtig sich mithilfe unserer Dokumentation eine Wissensbasis über Sprachassistenten und deren Techstack, MQTT, dem Hermes Protokoll, ZigBee und ZigBee2MQTT anzueignen.