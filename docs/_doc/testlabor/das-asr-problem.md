---
title: Das ASR Problem
sections:
  - Beschreibung des Problems
  - Unsere Lösung
  - Mögliche andere Lösungen
---


### Beschreibung des Problems

Die ASR soll die Stimme des Benutzers erkennen. Die ASR, die von ProjectAlice standartmäßig eingestellt ist, ist Pocketsphinx. Wir wollten den Sprachassistent auf deutsch entwickeln und benutzen, allerdings hat der Sprachassistent nur ganz selten
genau verstanden was wir sagen. Also haben wir uns an einer Lösung versucht.

### Unsere Lösung

Zunächst haben wir versucht die ASR von Google zu nutzen, aber dafür brauchte man eine Kreditkarte und das Projekt würde wichtige Eigenschaften, wie kostenlos und Datensicher verlieren.

Also haben wir versucht ein anderes ASR zu implementieren, nämlich Deepspeech auf deutsch. Es wurde ein Patch geschrieben der Deepspeech installieren und für Alice nutzbar machen sollte. Nach vielen Versuchen ist es Schließlich an einer nicht
vorhandenen Lizenz gescheitert.

### Mögliche andere Lösungen

Eine Möglichkeit ist den Sprachassistenten auf Englisch zu stellen und zu testen ob die englische Version besser funktioniert. Eine andere Möglichkeit wäre die Utterances der Intents zu reduzieren, dann werden nur noch bestimmte Sätze die zuverlässig funktionieren
verstanden. Denn je weniger Sätze insgesamt und je eindeutiger und verwechslungsfreier die Sätze desto besser versteht der Sprachassistent. Das ist uns während dem Projekt aufgefallen. So wurde zum Beispiel "Mach das Licht an" perfekt von "Mach das Licht aus"
aus [unserem selbstentwickelten Skill](https://ip-team5.intia.de/versuche-und-erfahrungen.html#enwicklung-eines-eigenen-skills) unterschieden.