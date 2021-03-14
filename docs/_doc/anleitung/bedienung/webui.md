---
title: Weboberfläche
sections:
  - Home
  - Skills
  - Adminbereich und Einstellungen
  - Mein Haus
---

Mit der Weboberfläche lässt sich Alice ganz leicht konfigurieren und mit Skills erweitern. Darüber hinaus lassen sich Hintergrundprozesse mit Syslog und Alicewatch nachvollziehen.

Skills können Widgets haben, die man in Home hinzufügen kann. Smart Home Geräte und Alice Satelites kann man in Mein Haus anordnen.

Das Webinterface ist unter dem Port 5000 erreichbar. Es ist erforderlich entweder die IP-Adresse des Raspberry Pis bzw. den Hostname zu kennen um darauf zuzugreifen.

### Home

Skills bringen manchmal Widgets mit sich, die man in Home hinzufügen und anordnen kann. Dazu klickt man einfach auf den Bearbeiten-Button und erhält verschiedene Optionen. Mit dem Plus kann man neue Widgets hinzufügen.

![Webui Home Edit](assets/images/webui-home-edit.png){: .img-responsive}
![Webui Home Edit Options](assets/images/webui-home-edit-options.png){: .img-responsive style="margin-top:1em"}
![Webui Home Add Widget](assets/images/webui-home-add-widget.png){: .img-responsive style="margin-top:1em"}

Anfangs sind zwei Widgets vom Skill DateDayTimeYear verfügbar.

### Skills

Unter Skills sieht man alle installierten Skills. Zu Anfang ist das AliceCore, die Haupteinheit und vier weitere Skills.

![Webui Skills](assets/images/webui-skills.png){: .img-responsive}

###### Skillübersicht

In der Ansicht sieht man Autor, Version, das Icon der Kategorie und den Status. Man kann sich auch Intents des Skills anzeigen lassen wie auch Einstellungen verändern wenn der Skill dies erlaubt. Manche Skills haben auch eine kleine Bedienungsanleitung.

![Webui Skills Intents](assets/images/webui-skills-intents.png){: .img-responsive}

Schon von Werk aus verfügt Alice über einige Intents, die man weder deaktivieren noch entfernen kann. Dazu zählen die Intents der Skills AliceCore, Contextsensitive und RedQueen wie auch die Skills selbst.

###### Skills installieren

Um Skills hinzuzufügen klickt man oben rechts auf das Download Symbol und bekommt eine Ansicht aller verfügbaren Skills.

![Webui Skills Store](assets/images/webui-skills-download.png){: .img-responsive}

Nun kann man einen oder mehrere Skill auswählen und den Download mit dem Download-Button bestätigen.

![Webui Skills Download](assets/images/webui-skills-downloads.png){: .img-responsive}

Nun werden alle Skills im Hintegrund geladen. Leider bekommt man auf der Download Seite kein Feedback bzw. hört die Download-Animation nicht auf auch wenn der Skill schon installiert ist. In Syslogs lässt sich gut verfolgen was im Hintegrund geschieht.

### Adminbereich und Einstellungen

Um in den Adminbereich zu gelangen muss man Nutzernamen und Passwort eingeben. Standardmäßig ist das admin und 1234.

###### Alice Einstellungen

Unter Alice Einstellungen kann man unter anderem den Tech Stack konfigurieren, Advanced Debug, Dev Mode sowie Scenarios (Node Red) aktivieren/deaktivieren. Nachdem man seine Einstellungen gemacht hat muss man ganz unten mit einem Klick auf Speichern bestätigen.

###### Utilities

Unter Utilities kann man Alice und den Rapsberry neustarten, die NLU trainieren, das System und die Skills aktuallisieren, wie auch neue Benutzer und Wakewords erstellen. Man kann außerdem das Modell der Wakewords verbessern aber auch Alice auf Werkseinstellung zurücksetzen.

### Mein Haus

In mein Haus ist es möglich Räume zu erstellen, die Inneneinrichtung zu modellieren und seine Geräte in die erstellten Räume hinzuzufügen. Außerdem lässt sich ein Backup davon erstellen.