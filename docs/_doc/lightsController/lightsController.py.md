---
title: LightsController
sections:
  - Was soll der Skill können
  - Talks
  - DialogueTemplate
  - LightsController.py
---


### Was soll der Skill können

Sinn und Zweck des Skills ist es über Sprache verschiedene Lampen an und aus zu schalten und deren Farbe, Helligkeit und Farbtemperatur zu ändern. In unserem Fall sind es zwei Lampen, die wir 
ab sofort "PC-Lampe" und "Sofa-Lampe" nennen. Es soll zum Beispiel möglich sein zu sagen: "Ändere die Farbe der Sofa-Lampe zu rot", "Die Farbe wurde geändert" wird geantwortet und die 
Sofa-Lampe fängt an rot zu leuchten. Es gibt also einen Intent zum einschalten, einen zum ausschalten, einen Intent zum Farbe wechseln, einen für die Helligkeit und einen für die Farbtemperatur.

### Talks

Talks sind die "Antworten", die der Sprachassistent geben kann. Hierbei gibt es verschiedene Variationen der Antworten, um den Sprachassistenten natürlicher wirken zu lassen. Wir stellen hier
immer nur eine Antwort pro Fall vor.

##### Anschalten-Intent

- "Das Licht ist jetzt an" - für das Einschalten einer oder beider Lampen.

##### Ausschalten-Intent

- "Das Licht ist jetzt aus" - für das Ausschalten einer oder beider Lampen.

##### Farbe-ändern-Intent

- "Die Farbe wurde geändert" - für Änderung der Farbe bei einer oder beider Lampen.

##### Helligkeit-ändern-Intent

- "Die Helligkeit wurde geändert" - für die Änderung der Helligkeit bei einer oder beider Lampen.

##### Farbtemperatur-ändern-Intent

- "Die Farbtemperatur wurde geändert" - für die Änderung der Farbtemperatur einer oder beider Lampen.

### DialogueTemplate

Hier stehen die Sätze, die der Benutzer sagen kann, damit ein bestimmter Intent erkannt wird. Es gibt wieder Verschiedene Variationen für jeden Fall, damit der Wille Benutzer zuverlässiger 
erkannt wird. Wir stellen wieder nur einen Satz pro Fall vor.

##### Anschalten-Intent

- "Schalte das Licht ein" - für das Einschalten beider Lampen.
- "Schalte die PC-Lampe ein" - für das Einschalten der PC-Lampe.

##### Ausschalten-Intent

- "Schalte das Licht aus" - für das Ausschalten beider Lampen.
- "Schalte die PC-Lampe aus" - für das Ausschalten der PC-Lampe.

##### Farbe-ändern-Intent

Unterstützte Farben sind zurzeit: rot,gelb,blau,grün,lila,orange,weiß.
- "Ändere die Farbe zu rot" - für das Ändern der Farbe aller Lampen zu rot.
- "Ändere die Farbe der PC-Lampe zu rot" - für das Ändern der Farbe der PC-Lampe zu rot.

##### Helligkeit-ändern-Intent



##### Farbtemperatur-ändern-Intent




### LightsController.py








