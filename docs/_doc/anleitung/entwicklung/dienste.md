---
title: Hintergrunddienste
---

Raspbian OS verwendet Systemd für Hintergrunddienste. Alice installiert einige Komponenten mit der Systempaketverwaltung, die für jedes Paket automatisch einen Hintergrunddienst für Systemd konfiguriert. Andere Pakete werden von Alice selbst installiert und konfiguriert.

Der wichtigste Dienst ist `ProjectAlice`. Um den Status des Dienstes herauszufinden verwendet man:
```
systemctl status ProjectAlice
```
Um den Dienst neuzustarten nutzt man:
```
sudo systemctl restart ProjectAlice
```

Andere Dienste, die mitinstalliert werden sind unter anderem:
- Mosquitto MQTT Broker
- Hermes LED Control
- Verschiedene Komponenten des Techstacks (meist Snips Komponenten)

Mit folgendem Kommando kann man sich alle aktiven Dienste anzeigen lassen:
```
systemctl list-units --type=service
```
Um auch Dienste anzuzeigen, die nicht aktiv sind, nutzt man:
```
systemctl list-units --type=service --all
```
