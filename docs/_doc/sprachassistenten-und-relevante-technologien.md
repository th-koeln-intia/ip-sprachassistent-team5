---
title: Sprachassistenten und relevante Technologien
excerpt: Allgemeines, Services und Alice Skills
date: 2020-11-23
icon:
  type: fa
  name: fa-microphone
color: blue
sections:
  - /allgemein
  - /service
  - /teaser-alice-skills
---

# Sprachassistenten

Seitdem intelligente persönliche Sprachassistenten wie Siri (2012) oder Smart Speaker wie Amazon Echo (2014) für die breite Masse erschienen sind, hat sich viel in dem Bereich getan. Viele der großen Unternehmen wie Apple, Microsoft, Google und Amazon investieren nicht nur viel in dem Bereich sondern entwickeln auch alle ihre eigene Sprachassistenten.

Was jedoch alle kommerziellen Sprachassistenten gemein haben ist, dass sie nicht auf Privatsphäre ausgelegt sind und hauptsächlich cloudbasiert arbeiten. Wenn es um Datenschutz, Privatsphäre oder Offlinetauglichkeit geht sind diese Geräte also ungeeignet.

Seit einigen Jahren gibt es jedoch ernstzunehmende Open-Source Lösungen, die den Fokus auf den Punkt Privatsphäre legen. Diese sogennanten Maker-Lösungen werden i.d.R. auf eigener Hardware wie z.B. einem Raspberry Pi installiert und bieten neben Privatsphäre und Datenschutzkonformität außerdem oft noch eine höhere Konfigurierbarkeit und Offlinetauglichkeit.

## Private-by-design

Snips, ein französisches Unternehmen, welches seit seiner Gründung im Jahr 2013, in den Bereichen Künstliche Intelligenz und Mensch-Computer Interaktion geforscht hat, veröffentlichte 2017 erstmals eine [Spracherkennungsplattform](https://medium.com/snips-ai/hey-snips-announcing-the-first-private-by-design-voice-platform-bf23b8a843fd) bei der Privatsphäre schon beim Entwurf eine Hauptrolle gespielt hat (private-by-design). Die Privatsphäre wird hierbei dadurch gewährleistet, dass alle Berechnung offline durchgeführt werden und somit keine datenschutzkritischen Anfragen nach außen notwendig sind.

Dadruch wurde es erstmals möglich eigene ernstzunehmende Sprachassistenten auf einem Raspberry Pi zu entwickeln, die völlig datenschutzkonform und offlinetauglich waren.

Snips wurde 2019 von Sonos gekauft wodurch der Support für die öffentliche Plattform eingestellt worden ist. Mit Mycroft, Jasper, Rhasspy und Alice gibt es jedoch weitere Lösungen mit nahezu gleichem Konzept.

Auch wenn der Support für Snips eingestellt ist, sind einige Softwarekomponenten von Snips übrig geblieben, die z.B. immer noch in Rhasspy und Alice Verwendung finden.

## Funktionsweise und Stack eines Sprachassistenten

Ein Sprachassistent besteht aus mehreren Softwarekomponenten, die einen gemeinsamen Stack bilden und lässt sich wie folgt unterteilen:

- Wake word detection
- Speech-to-text (ASR)
- Intent recognition (NLU)
- Intent handling
- Text-to-speech (TTS)
- Dialog manager

**MQTT Broker**

Zentral für die Kommunikation zwischen den Komponenten ist ein MQTT Broker auf den alle Komponenten mittels Hermes Protokoll schreiben und lesen.

Ein weitverwendeter Open-Source MQTT Broker ist Eclipse Mosquitto.

**Wake word detection**

Vor jeder Bedienung muss der Sprachassistent erst einmal mittels "Wake Word" (auch als hotword bekannt) aktiviert werden. Sobald das Wort erkannt wurde, wartet der Assistent für eine bestimmte Zeit auf Anweisungen.

Bekannte Beispiel für Wake-words sind "Okay Google" für den Google Assistant und "Hey Siri".

Es gibt u.a. folgende Wake-word-engines:

- Porcupine (Alice, Rhasspy)
- Snips (Alice)
- Snowboy (Rhasspy)
- Mycroft Precise (Alice, Rhasspy)
- Rhasspy Raven (Rhasspy)
- Pocketsphinx (Rhasspy)

**ASR / STT**

Nach der Aktivierung durch die Wake-word-engine nimmt der Sprachassistent das Gesagte für eine bestimmte Zeit (ASR timeout) auf und wandelt es in Text um. Dafür ist Automatic-Speech-Recognition (ASR) bzw. Speech-to-Text (STT) verantwortlich.

Die Spracherkennung basiert auf Machine Learning Modellen. Es können entweder vorgefertigte Modelle genutzt werden (pre-trained models), die mit einer Liste von gebräuchlichen Wörtern trainiert sind oder selbst trainierte Modelle, die man mit den Befehlen trainiert, die man vom Nutzer erwartet. Letzteres verbessertet die Texterkennung, vermindert jedoch zur gleichen Zeit die Flexibilität des Systems.

Hierfür gibt es u.a. folgende Engines:

- Pocketsphinx (Alice, Rhasspy)
- Kaldi (Rhasspy)
- DeepSpeech (Alice, Rhasspy)
- Snips (Alice)
- Google (proprietär, Alice)

**Intent recognition / Natural Language Understanding (NLU)**

Nachdem das Gesprochene durch das Speech-to-Text System in Text umgewandelt worden ist, muss als nächstes erkannt werden welchen der verfügbaren Aufgaben (Intents) der Nutzer beabsichtigt. Neben der Erkennung des Intents wird außerdem die im Befehl enthaltenen Variablen (Slots), wie z.B. Zahlen, Zustände, Orte und Objekte erkannt.

Dafür gibt es u.a. folgende Systeme:

- Snips (Alice, Rhasspy)
- Fsticuffs (Rhasspy)
- Fuzzywuzzy (Rhasspy)
- RasaNLU (Rhasspy)
- Mycroft Adapt (Rhasspy)
- Flair (Rhasspy)

**Intent handling**

Nachdem der Intent erkannt ist, kommt Intenthandling ins Spiel. Hier wird der eigentliche Befehl ausgeführt und dem Nutzer bei Bedarf geantwortet.

- Mit Hermes Protokoll kompatible Services
- Home Assistant und [Hass.io](http://Hass.io)
- Node red / Scenarios
- Skills

**Text-to-speech**

Bei Bedarf antwortet der Assistent dem Nutzer mit einem vom Intenthandler bestimmten Text. Dafür ist eine Text-to-Speech (TTS) Engine nötig.

Folgende Text-to-Speech-Engines stehen zur Auswahl:

- Espeak (Rhasspy)
- PicoTTS (Alice, Rhasspy)
- Mycroft Mimic (Alice)
- NanoTTS (Rhasspy)
- MaryTTS (Rhasspy)
- OpenTTS (Rhasspy)
- Wavenet (Rhasspy)
- Amazon Polly (proprietär, Alice)
- Google Wavenet (proprietär, Alice)
- IBM Watson (proprietär, Alice)

**Dialog manager**

Der Dialog Manager verwaltet eine Sitzung, die durch ein erkanntes Wakeword oder einem manuellen `startSession` initiiert wird und koordiniert ASR, NLU und TTS.

## Schnittstellen

Die einzigen Schnittstellen, die der Nutzer für die Interaktion mit dem Sprachassistenten benötigt sind Mikrofon und Lautsprecher. Für eine verbesserte Spracherkennung ist ein Mikrofon-Array zu empfehlen. Außerdem hat der Nutzer oft noch die Möglichkeit per Weboberfläche den Sprachassistenten zu konfigurieren.

MQTT

Zigbee

Node Red
