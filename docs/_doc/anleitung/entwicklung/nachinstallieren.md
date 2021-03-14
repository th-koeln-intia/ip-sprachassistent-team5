---
title: Nachinstallieren von Paketen
sections:
  - Systempaketverwaltung
  - Virtuelle Umgebungen unter Python
  - NPM bei Node Red und Zigbee2MQTT
---

Je nachdem wofür man Pakete nachinstallieren möchte oder muss, nutzt man verschiedene Packagemanager.

### Systempaketverwaltung
Einige Pakete kann man mit [apt-get](https://wiki.ubuntuusers.de/apt/apt-get/), der Paketverwaltung unter Debian-basierten Distributionen und Debian-Derivaten wie Ubuntu, nachinstallieren.

Jede dieser Distribution hat auch wenn derselbe Paketmanager verwendet wird, eigene Paketquellen. Debian-basierte Distributionen wie Raspbian bieten ältere Versionen der Programme, setzen aber auf Stabilität.

Man kann weitere Fremdquellen / [PPAs](https://wiki.ubuntuusers.de/Paketquellen_freischalten/PPA/) hinzufügen um z.B. neuere Versionen zu installieren, dadurch verliert man jedoch oft die eben genannte Stabilität und muss externen Quellen vertrauen, bei denen man nicht mit Sicherheit sagen kann ob sie vertrauenswürdig sind.

### Virtuelle Umgebungen unter Python

Andere Pakete kann oder muss man mit pip nachinstallieren. Je nachdem ob man für ProjectAlice oder Hermes LED Control Pakete nachinstallieren muss verwendet man eine andere virtuelle Umgebung.

Beispiel:
```
~/ProjectAlice/venv/bin/pip3 install pyyaml
~/hermesLedControl/venv/bin/pip3 install pyyaml
```

### NPM bei Node Red und Zigbee2MQTT

Es kann zum Beispiel sein, dass bei der Installation des Zigbee2MQTT Skills die Instalaltion der Abhängigkeiten nicht erfolgreich war oder nicht erfolgt ist. Um die Pakete manuell nachzuinstallieren nutzt man npm:
```
cd /opt/zigbee2mqtt/
npm install
```
In der `package.json` sind alle Abhängigkeiten aufgelistet.

Wenn man zum Beispiel Node Red erweitern möchte kann man Pakete mit npm nachinstallieren:
```
cd ~/.node-red/
npm install node-red-contrib-zigbee2mqtt
```
