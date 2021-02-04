---
title: Hermes
sections:
  - Audio Server
  - Wake Word
  - ASR
  - NLU
  - Dialog manager
  - TTS
---

<link rel="stylesheet" type="text/css" href="/assets/css/index.css">

Das Snips Protokoll wird neben anderen Implementationen mit MQTT Topics implementiert. Dazu gibt es zwei offizielle Referenz APIs. Einmal eine [Allgemeine](https://docs.snips.ai/reference/hermes) und eine speziell zum [Dialog Manager](https://docs.snips.ai/reference/dialogue). Unsere Übersicht enthält zwar alle Topics jedoch fehlt z.B. der Payload und weitere Informationen. Für einen groben Überblick ist unsere Übersicht über alle Topics jedoch gut geeignet. Um mehr Informationen zu erlangen wurde bei jedem Topic auf die offizielle Referenz verlinkt.

###### Audio Server

**Publish**

| Topic                                                        | Beschreibung                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <small>[hermes/audioServer/SITE_ID/playBytes/REQUEST_ID](https://docs.snips.ai/reference/hermes#playing-a-wav-sound)</small> | WAV Sound <small>(komplett)</small> zum Abspielen senden     |
| <small>[hermes/audioServer/SITE_ID/playBytesStreaming/REQUEST_ID/CHUNK_NUMBER/IS_LAST_CHUNK](https://docs.snips.ai/reference/hermes#streaming-a-sound)</small> | WAV Sound <small>(Teil eines Streams)</small> zum Abspielen senden |

**Subscribe**

| Topic                                                        | Beschreibung                  |
| ------------------------------------------------------------ | ----------------------------- |
| [hermes/audioServer/SITE_ID/playFinished](https://docs.snips.ai/reference/hermes#being-notified-when-sound-has-finished-playing) | WAV Sound wurde abgespielt    |
| [hermes/audioServer/SITE_ID/streamFinished](https://docs.snips.ai/reference/hermes#being-notified-when-stream-has-finished) | WAV Stream wurde abgespielt   |
| [hermes/audioServer/SITE_ID/audioFrame](https://docs.snips.ai/reference/hermes#being-notified-when-a-sound-frame-is-captured) | WAV Audio Frame wurde erfasst |

###### Wake word

**Publish**

| Topic                                                        | Beschreibung                |
| ------------------------------------------------------------ | --------------------------- |
| [hermes/hotword/toggleOn](https://docs.snips.ai/reference/hermes#activating-the-wake-word-component) | Wakeword Engine anschalten  |
| [hermes/hotword/toggleOff](https://docs.snips.ai/reference/hermes#deactivating-the-wake-word-component) | Wakeword Engine ausschalten |

**Subscribe**

| Topic                                                        | Beschreibung                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [hermes/hotword/WAKEWORD_ID/detected](https://docs.snips.ai/reference/hermes#detecting-a-wake-word) | Das Wakeword wurde erkannt. Bei nur einem Wakeword ist die Wakeword ID `default`.<br />Mit `hermes/hotword/+/detected` kann auf alle Wakewords gehört werden |

###### ASR

**Publish**

| Topic                                                        | Beschreibung                       |
| ------------------------------------------------------------ | ---------------------------------- |
| [hermes/asr/toggleOn](https://docs.snips.ai/reference/hermes#activating-the-asr-component) | ASR anschalten                     |
| [hermes/asr/toggleOff](https://docs.snips.ai/reference/hermes#deactivating-the-asr-component) | ASR ausschalten                    |
| [hermes/asr/startListening](https://docs.snips.ai/reference/hermes#telling-the-asr-component-to-start-listening) | ASR mitteilen zuzuhören            |
| [hermes/asr/stopListening](https://docs.snips.ai/reference/hermes#telling-the-asr-component-to-stop-listening) | ASR mitteilen nicht mehr zuzuhören |

**Subscribe**

| Topic                                                        | Beschreibung             |
| ------------------------------------------------------------ | ------------------------ |
| [hermes/asr/partialTextCaptured](https://docs.snips.ai/reference/hermes#obtaining-intermediate-asr-transcription-results) | Zwischenergebnis der ASR |
| [hermes/asr/textCaptured](https://docs.snips.ai/reference/hermes#obtaining-full-asr-transcription-results) | Endergebnis der ASR      |

###### NLU

**Publish**

| Topic                                                        | Beschreibung                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [hermes/nlu/query](https://docs.snips.ai/reference/hermes#sending-text-to-the-nlu-component) | NLU Text senden <small>(Normalerweise von der ASR ermittelt)</small> |
| [hermes/nlu/partialQuery](https://docs.snips.ai/reference/hermes#sending-text-to-the-nlu-component-for-slot-detection) | NLU fehlenden Teiltext eines Intents <small>(z.B. Slot)</small> senden |

**Subscribe**

| Topic                                                        | Beschreibung                                         |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| [hermes/nlu/intentParsed](https://docs.snips.ai/reference/hermes#obtaining-the-result-of-an-nlu-parsing-low-level-api) | Ergebnis der NLU <small>(ermittelter Intent)</small> |
| [hermes/nlu/slotParsed](https://docs.snips.ai/reference/hermes#obtaining-the-result-of-an-nlu-slot-detection) | Ergebnis der NLU <small>(ermittelter Slot)</small>   |
| [hermes/nlu/intentNotRecognized](https://docs.snips.ai/reference/hermes#being-notified-when-an-intent-was-not-recognised) | Es konnte kein Intent ermittelt werden               |
| [hermes/error/nlu](https://docs.snips.ai/reference/hermes#being-notified-when-an-error-has-occurred) | Über diesen Topic meldet die NLU verschiedene Fehler |

###### Dialog Manager

**Publish**

| Topic                                                        | Beschreibung                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [hermes/dialogueManager/startSession](https://docs.snips.ai/reference/dialogue#start-session) | Dialogsession starten                                        |
| [hermes/dialogueManager/continueSession](https://docs.snips.ai/reference/dialogue#outbound-message-1) | Dialog weiterführen falls z.B. weitere Nutzereingaben erforderlich sind. |
| [hermes/dialogueManager/endSession](https://docs.snips.ai/reference/dialogue#end-session) | Dialog beenden. Gesendet wenn Intent abgearbeitet ist.       |
| [hermes/dialogueManager/configure](https://docs.snips.ai/reference/dialogue#outbound-message-3) | Dialog Manager auf eine Auswahl an Intents beschränken.      |
| [hermes/injection/perform](https://docs.snips.ai/reference/dialogue#entities-injection) | Entities injizieren. Erlaubt es ASR & NLU Models direkt auf dem Gerät zu erweitern. |
| [hermes/injection/complete](https://docs.snips.ai/reference/dialogue#injection-complete) | Signalisieren, dass Entity injection fertig ist              |
| [hermes/injection/reset/perform](https://docs.snips.ai/reference/dialogue#injection-reset) | Injizierte Entities löschen und ASR & NLU neustarten         |
| [hermes/injection/reset/complete](https://docs.snips.ai/reference/dialogue#injection-reset-complete) | Signalisieren, dass injizierte Entities gelöscht sind        |

**Subscribe**

| Topic                                                        | Beschreibung                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [hermes/intent/INTENT_NAME](https://docs.snips.ai/reference/dialogue#intent) | Intent wird ausgeführt                                       |
| [hermes/dialogueManager/intentNotRecognized](https://docs.snips.ai/reference/dialogue#inbound-message-4) | Intent wurde nicht erkannt                                   |
| [hermes/dialogueManager/sessionQueued](https://docs.snips.ai/reference/dialogue#session-queued) | Sessionstart wurde angefragt obwohl eine Session aktiv ist. Session kommt in Warteschlange |
| [hermes/dialogueManager/sessionStarted](https://docs.snips.ai/reference/dialogue#session-started) | Session wurde gestartet <small>(Durch Wakeword oder manuell)</small> |
| [hermes/dialogueManager/sessionEnded](https://docs.snips.ai/reference/dialogue#session-ended) | Session wurde beendet                                        |

###### TTS

**Publish**

| Topic                                                        | Beschreibung                          |
| ------------------------------------------------------------ | ------------------------------------- |
| [hermes/tts/say](hermes/tts/say ) <small>(low level)</small> | TTS befehlen bestimmten Text zu sagen |

**Subscribe**

| Topic                    | Beschreibung        |
| ------------------------ | ------------------- |
| [hermes/tts/sayFinished](hermes/tts/sayFinished) | TTS hat gesprochen. |