---
title: Alice versteht mich nicht
sections:
  - Spracherkennung
  - Befehlserkennung
---

Für eine gute Befehlserkennung muss ein gutes Zusammenspiel zwischen Sprecherkennung (ASR) und Befehlserkennung (NLU) gegeben sein.
Es kann aber auch sein, dass eine Konfiguration Sprachbefehle mancher Nutzer besser erkennt als die anderer Nutzer.

### Spracherkennung

Die ASR ist für die Spracherkennung zuständig. Sie wandelt Sprache in Text um. Anhand des erkannten Texts Text wird im nächsten Schritt von der NLU der passende Befehl bestimmt.
Damit der Befehl auch richtig erkannt werden kann, muss die ASR also gute Vorarbeit leisten.

Mithilfe der Systemlogs und Alice Watch lässt sich überprüfen was die ASR erkennt und welchen Befehl die NLU ermittelt. Bei einer erfolgreichen Spracherkennung seitens der ASR, bitte den Punkt Befehlserkennung anschauen.

Es ist ein bekanntes Problem, dass offline/open-source ASRs zumindest auf Deutsch und anderen Sprachen nicht zuverlässig funktionieren. ASRs, die in der Cloud arbeiten haben dieses Problem nicht, da sie täglich genügend Spracheingaben von ganz verschiedenen Nutzern (nach Sprache, Geschlecht, Alter etc.) erhalten und somit jeden Tag dazu lernen und ihre Spracherkennung verbessern können.

Die Modelle von Open Source ASRs werden anhand eines Textkorpus mit einer begrenzten Anzahl an Sprechern vortrainiert und werden üblicherweise im Betrieb nicht viel besser. Für die englische Sprache gibt es Modelle, die zuverlässiger funktionieren als für andere Sprachen. Es kann aber unabhängig vom Modell so sein, dass die ASR eine Stimme besser erkennt und eine andere überhaupt nicht. Daher wäre ein erster möglicher Schritt zu schauen ob der Sprachassistent eine andere Person besser versteht.

Falls dies keinen Unterschied macht ist zu überprüfen welche ASR genutzt wird. Unter Alice stehen derzeit vier verschiedene ASRs zu Verfügung:
- Pocketsphynx
- Deepspeech
- Snips ASR
- Google

Snips ist nur für Englisch verfügbar und führt bei Auswahl das System in ein Reboot-Cycle. Deepspeech kann ausgewählt werden, verwendet aber standardmäßig ein Modell für Englisch und bietet daher vom Werk aus auch keine gute Texterkennung.

Die ASR von Google funktioniert laut Entwicklern, die es selbst einsetzen sehr zuverlässig. Für die Konfiguration muss jedoch ein Google Cloud Computing Konto erstellt werden und die Verwendung des ASR-Dienstes kostet sobald die Quota überschritten ist. Ein Vorteil für den Einsatz der Google ASR mit Alice anstatt von Google Home ist, dass erst nach der Wakeworderkennung die Sprachaufnahmen an Google gesendet werden.

Ausschließlich Pocketsphynx ist für Deutsch von Werk aus einsatzfähig, liefert aber nach Erfahrung auch nicht immer zuverlässige Ergebnisse. Laut den anderen Teams funktioniert Pocketsphynx unter Rhasspy besser. Es muss an dieser Stelle gesagt werden, dass Alice die ASR nachträglich nicht trainiert bzw. anhand der verfügbaren Intents optimiert. Nur die NLU wird im jetzigen Stand trainiert.

###### Deepspeech mit deutschem Modell

Es ist möglich Deepspeech nachträglich mit einem deutschen Modell auszustatten. Dazu kann folgendes [Modell](https://github.com/AASHISHAG/deepspeech-german) verwendet werden.

Team 4 hat genau dies getan und für Rhasspy dokumentiert. Dazu kann das vortrainiertes Modell für die Version 0.7.4 verwendet werden. Bei Alice muss dafür die Datei `core/asr/model/DeepSpeechAsr.py` angepasst werden. Zum einen muss bei denden Dependencies die Version 0.7.4 anstelle von 0.6.1 angegeben werden und die API-Aufrufe entsprechend angepasst werden. Darüber hinaus kann man bei Angabe der URLs und mit einer Überprüfung der eingestellten Sprache Alice automatisch das Deutsche Modell herunterladen lassen wenn Deutsch als Sprache ausgewählt ist.

Falls Deepspeech schon aktiv ist muss nun Deepspeech in der Virtuellen Umgebung deinstalliert werden, das vorhandene Modell gelöscht werden und anschließend neugestartet werden:
```
~/ProjectAlice/venv/bin/pip3 uninstall deepspeech
rm -R ~/ProjectAlice/trained/asr/deepspeech/de/
sudo reboot
```

Nun sollte Deepspeech mit neuer Version und deutschem Modell automatisch installiert werden.

### Befehlserkennung

Falls die Spracherkennung zuverlässig genug funktioniert, kann es auch an der NLU liegen, dass der gewünschte Intent nicht erkannt wird. Wenn die NLU nicht richtig trainiert ist, liefert sie einen geringen Confidence-Wert und scheitert bei fast jedem Versuch oder erkennt womöglich sogar einen anderen, nichtgewollen Intent.

Die NLU kann man im Admin-Menü unter Utilities trainieren.