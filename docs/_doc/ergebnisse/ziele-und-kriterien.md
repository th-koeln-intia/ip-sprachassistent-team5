---
title: Ziele und Bewertung
sections:
  - Entscheidende Kriterien
  - Plattformunabhängigkeit und Kompatibilität
  - Rezeption/Markt
  - Reife
  - Nutzersicht
  - Entwicklersicht
  - Ökosystem
---

Unser Ziel war es mithilfe von Alice in der Beta 4 ein Proof-of-Concept für einen Sprachassistenten zu erstellen, der datenschutzkonform ist, so weit es geht offlinefähig ist und zuverlässig für deutschsprachige Nutzer funktioniert. Daraus leiten sich unsere entscheidenden Kriterien ab, die Alice im jetzigen Zustand leider nicht ausreichend erfüllt.

Darüber hinaus haben wir die allgemeinen Bewertungskriterien Plattformunabhängigkeit und Kompatibilität, Rezeption/Markt, Reife, Nutzersicht, Entwicklersicht und Ökosystem.

### Entscheidende Kriterien

###### Datenschutzkonformität
Solange man keine Cloud-Dienste wie z.B. Google als ASR oder Google Wavenet als TTS nutzt, ist Alice von Werk aus datenschutzkonform.

###### Offline-Fähigkeit
Alice ist von Werk aus im Betrieb auch offlinefähig. Zumindest mit Skills, die keine Internetverbindung benötigen. Für die Instalaltion und Aktuallisierungen benötigt man jedoch natürlich eine Internetverbindung.

###### Zuverlässigigkeit
Aufgrund der schlechten Spracherkennung auf Deutsch lässt sich der Sprachassistent von Werk aus nicht nutzen ohne dass man auf die Google ASR wechselt. Dadurch kann der Punkt Datenschutzkonformität nicht erfüllt werden. Außerdem ist es erforderlich ein Google Cloud Computing Konto zu erstellen. Bei der Nutzung fallen Kosten an sobald man die monatliche Quota überschritten hat.

Dies ist der ausschlaggebende Punkt warum ein Proof-of-Concept derzeit nicht möglich ist.

### Plattformunabhängigkeit und Kompatibilität
Die Community bietet neben der manuellen Installation, die nach unseren Erfahrungen nach nur mit dem Raspberry Pi und Raspberry Pi OS kompatibel ist, Docker-Konfigurationen für PCs und ARM Prozesoren. Die ARM-Version haben wir nicht ausprobiert, die PC-Version aber funktioniert nur in einer bestimmten Konfiguration, welche Cloud-Dienste nutzt.

Wir haben auch versucht Alice auf virtuellen Maschinen manuell zu installieren und haben dafür die Distributionen Ubuntu und Raspberry Pi Desktop verwendet.

Im Installationsskript sind die Installationsbefehle, also sudo Kommando + Paketverwaltung apt hardgecodet. Daher funktionieren das Skript erstmal nur bei Debian-Distributionen und Derivaten.

Darüber hinaus fordert Debian und Ubuntu auf dem PC standardmäßig eine Passworteingabe, welches für die Installation deaktiviert werden müsste. Außerdem wird zum Beispiel eine bestimmte Version von Python erwartet. Da bei Ubuntu zum Beispiel die Paketquellen aktuellere Software bieten, muss man auch hier manuell ältere Software nachinstallieren.

Bis zur erfolgreichen manuellen Installation von Alice auf einer anderen Distribution oder einem anderen Gerät müsste man also erstmal viel Troubleshooting betreiben.

###### Techstack

Alice bietet eine große Auswahl an Komponenten für den Techstack. Diese können in der Weboberfläche ausgewählt werden und installieren bzw. konfigurieren sich automatisch im Hintergrund. Theoretisch ist es möglich den Techstack zu erweitern oder Modelle und Einstellungen manuell zu verändern, es ist aber nicht direkt vorgesehen und bei Veröffentlichung ist zu beachten Änderungen per GPLv3 zu lizensieren.

###### Skills

Mit Skills können Dienste wie z.B. HomeAssistant oder Zigbee2MQTT nachinstalliert werden. Falls ein Dienst im Skill Store nicht verfügbar ist, kann man ihn selbst erstellen und im Store veröffentlichen.

### Rezeption/Markt

###### Popularität
Alice ist noch nicht sehr weit verbreitet. Es ist momentan in Beta und daher erstmal nur für Entwickler zu empfehlen. Der angebotene Techstack hat jedoch Relevanz und weite Verbreitung.

###### Alleinstellungsmerkmale
Anders als Rhasspy entwickelt man mit Alice keine Individuallösung sondern erhält ein Produkt mit einem Ökosystem und muss daher nicht unbedingt selbst programmieren. Alice überzeugt außerdem mit einer automatisierten Installation und Konfiguration. Man kann außerdem sehr leicht über Discord mit der Community in Kontakt treten, die relativ aktiv und unterstützend ist.

### Reife

###### Entwicklungsstatus
Alice befindet sich momentan in der Open Beta Phase und ist daher nur für Entwickler zu empfehlen.

Wir haben die Version Beta 4 getestet, die zwar im Betrieb für eine Beta gut funktioniert hat, jedoch hier und da Bugs auftraten und man oft gezwungen war die Logs zu untersuchen um das Problem zu beheben, was für einem Normalanwender nicht zumutbar wäre. Alice selbst sagt aber auch, dass diese Nutzergruppe in der jetzigen Version noch nicht die Zielgruppe ist.

Mit der Beta 5 kamen neue Features, welche die User Experience noch einmal erheblich verbessert haben und eine bessere Integration für Smart-Home-Geräte bieten. Nach Release der Beta 5 konzentriert sich die Community nun darauf Bugs ausfindig zu machen, zu beheben und die Stabilität von Alice generell zu verbessern um in naher Zukunft einen Release Candidate zu veröffentlichen.

###### Bekannte Probleme

Hier listen wir die Probleme auf die wir in der Beta 4 bemerkt hatten. Einige davon treten mit der Beta 5 nicht mehr auf.

- Offline ASRs (nicht englisch) funktionieren nicht zuverlässig genug
- Deepspeech installiert kein deutsches Modell
- Docker Konfiguration für PCs unterstützt nur eine bestimmte Konfiguration
- Installationsskript ist nicht plattformagnostisch
- Nutzer wird bei falscher Konfiguration nicht gewarnt, sodass man nach Konfiguration in ein Reboot-Cycle kommt
- Web-UI blockiert beim Trainieren der NLU (keine Logs)
- Beim Sprachwechsel wurde die NLU nicht automatisch konfiguriert sodass das Training immer scheitert
- Buttons wie Reboot und Restart funktionieren nicht immer
- Schlechte Spracherkennung erlaubt es nicht Nutzer und personalisiertes Wakeword zu konfigurieren
- Zigbee2MQTT erlaubt es trotz gesetzter Einstellung nicht, dass sich weitere Geräte verbinden
- Abhängigkeiten müssen in manchen Fällen manuell nachinstalliert werden

### Nutzersicht

Aus Nutzersicht überzeugt Alice ansonsten aber. Durch die automatisierte Installation und Konfiguration sowie auch die intuitive Weboberfläche hat man mit Alice eine sehr nutzerfreundliche Alternative zu anderen Makerlösungen. Der Installationsprozess könnte jedoch noch weiter vereinfacht werden, sodass keine Konfiguration per YAML-Dateien nötig sind. Außerdem hat man mit der neuen Weboberfläche eine verbesserte User Experience und eine verbesserten Integration von Smart-Home Geräten. Wenn kein Troubleshooting per Konsole mehr nötig ist und die Community größer wird sodass der Skill Store mehr bietet, ist Alice aus Nutzersicht eine sehr gute Lösung.

### Entwicklersicht

###### Accessability
Für Entwickler ist die Accessability sehr hoch. Da sich Alice ständig ändert ist die Dokumenation nicht immer vollständig bzw. aktuell. In solchen Fällen bietet aber die Community über Discord oft Support.

###### Lernkurve
Nicht anders als bei anderen Maker-Lösungen ist es notwendig ein grundlegendes Verständnis von Linux und der Kommandozeile, des Techstacks eines Sprachassistenten, von MQTT, dem Hermes-Protokoll wie auch ZigBee zu haben. Die offizielle Dokumentation zur Skill-Entwicklung, der Source Code von bereits im Store erhältlichen Skills, aber auch der Support der Community helfen bei der Entwicklung von eigenen Skills sehr.

###### Testbarkeit
Die Software lässt sich gut testen. Außerdem sind einige CI-Tests standardmäßig im Git-Repo integriert. Es gibt außerdem Guidelines für Skills.

### Ökosystem

Mit dem Skillsystem und dem Open-Source Gedanken kann durchaus ein gutes Ökosystem für Sprachassistenten entstehen, falls die Community noch aktiver wird. 

###### Support
Alice lebt von der Community. Auch wenn das Projekt im Moment noch überschaubar ist, steht hinter Alice eine relativ aktive Community mit der man sehr leicht über Discord in Kontakt treten kann. Selbst als Einsteiger wird man dort begrüßt und erhält Hilfestellungen zu vielen Problemen und kann sich wie gesagt ganz einfach selbst beiteiligen und am Projekt mitwirken.

Es wird momentan fleißig an der Stabilität gearbeitet damit ein Release Candidate und anschließend die Version 1.0 in naher Zukunft veröffentlich werden kann. Im Moment deutet alles darauf hin, dass Alice auch in Zukunft weiterentwickelt und verbessert wird.

###### Governance

Der Entwicklungsprozess ist nachvollziehbar und gut erklärt. Es werden außerdem moderne und bewährte Entwicklungstools genutzt.

###### Distributoren
Man kann leicht mit den Entwicklern direkt in Kontakt treten und nachvollziehen wer an was arbeitet. Momentan gibt es in Alice Core drei aktive Entwickler und weitere Leute, die sich in der Community beteiligen und an Skills entwickeln. Es ist sehr leicht sich selbst zu beteiligen.

###### Lizensierung

Alice Core und viele andere Skills stehen unter GNU General Public License v3.0. Das bedeutet, dass die Software privat wie auch kommerziell genutzt werden kann wie auch weiterverteilt werden kann. Dabei ist aber zu beachten, dass Lizenz und Copyright nicht verändert werden. Bei Änderungen des Codes müssen die Änderungen kenntlich gemacht werden. Änderungen müssen auch unter der GPLv3-Lizenz lizensiert werden. Für die ordnusgemäße Funktion der Software gibt es keine Gewähr.