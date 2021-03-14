---
title: Fazit
sections:
  - Offline ASRs
  - Beta Phase
  - Positives
---

Mithilfe von Project Alice in der Beta 4 kann ohne Weiteres Zutun kein zuverlässiger, open-source Sprachassistent für deutschsprachige Nutzer erstellt werden. Das Hauptproblem dabei stellt die ASR dar, da sie anders als bei Rhasspy nicht trainiert werden kann. Alice bietet jedoch Spracherkennung durch Cloud-Dienste wie Google an, die zuverlässig funktioniert. Auch wenn Alice nur nach der Erkennung des Wakewords Aufnahmen an Google sendet, wäre hiermit der Punkt Datenschutzkonformität nicht erfüllt.

### Offline ASRs

Mit den angebotenen Offline-ASRs versteht Alice den Nutzer selbst nach mehrmaligen Versuchen oft nicht. Da der Datensatz der Offline-ASRs anders als bei Cloud-Diensten viel kleiner ist, werden manche Stimmen schwerer verstanden als andere.

Die Offline-ASRs mit englischem Modell funktionieren, auch wenn nicht so zuverlässig wie Cloud Dienste, besser als die mit deutschem Modell. Die Community von Alice ist jedoch daran interessiert auch andere Sprachen als Englisch zu unterstützen und möchte daher auch besser geeignete ASRs bzw. Modelle unterstützen.

Auch wenn nicht direkt vorgesehen, ist es jedoch möglich andere Modelle als die standardmäßig installierten, zu nutzen.

### Beta Phase

Ein zuverlässiges Proof-of-Concept kann mit Alice außerdem noch nicht entstehen, da es sich in der Open Beta Phase befindet.

Wir haben die Version Beta 4 getestet, die zwar im Betrieb für eine Beta gut funktioniert hat, jedoch hier und da Bugs auftraten und man oft gezwungen war die Logs zu untersuchen um das Problem zu beheben, was für einem Normalanwender nicht zumutbar wäre. Alice selbst sagt aber auch, dass diese Nutzergruppe in der jetzigen Version noch nicht die Zielgruppe ist.

Mit der Beta 5 kamen neue Features, welche die User Experience noch einmal erheblich verbessert haben und eine bessere Integration für Smart-Home-Geräte bieten. Nach Release der Beta 5 konzentriert sich die Community nun darauf Bugs ausfindig zu machen, zu beheben und die Stabilität von Alice generell zu verbessern um in naher Zukunft einen Release Candidate zu veröffentlichen.

### Positives

Auch wenn es im Moment nicht für ein offlinefähiges und datenschutzkonformes, deutschsprachiges Proof-of-Concept reicht, ist es durchaus vorstellbar, dass wenn Alice an den gennanten Punkten arbeitet, eine sehr nutzerfreundliche wie auch entwicklerfreundliche Alternative zu anderen Maker-Lösungen daraus entstehen kann.

Dank des Skillsystems und dem eigenen Skill Store ist es in den meisten Fällen nicht nötig eigene Skills zu entwickeln. Falls ein Skill die eigenen Anforderungen nicht erfüllt, kann man sich entweder sehr einfach am Entwicklungsprozess beteiligen oder aber einen eigenen Skill entwickeln. Die Dokumentation dazu ist, wenn man grundlegende Python-Kenntnisse hat auch leicht verständlich.

Alice lebt von der Community. Auch wenn das Projekt im Moment noch überschaubar ist, hat Alice eine relativ aktive Community mit der man sehr leicht über Discord in Kontakt treten kann. Selbst als Einsteiger wird man dort begrüßt und erhält Hilfestellungen zu vielen Problemen und kann sich wie gesagt ganz einfach selbst beiteiligen und am Projekt mitwirken.

Neben dem Skillsytem ist der Installationsprozess relativ einfach im Vergleich zu anderen Maker-Lösungen, da nach anfänglicher Konfiguration per YAML-File, fast alle Abhängigkeiten und Teile des Techstacks im Hintegrund installiert werden. Im Menü kann nachträglich vieles davon angepasst werden. Alice installiert und konfiguriert nach Änderung in den Einstellungen alles für den Nutzer im Hintergund automatisch.
