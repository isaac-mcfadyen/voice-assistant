# Voice Assistant

An open-source voice assistant.

### Modules
Voice Assistant is comprised of modules. Each module exports functions to initialize itself, tell the main handler whether it is capable of fulfilling a request, and actually fulfill the request.

Modules handle their own logic; the role of the main handler is to process transcription and call the modules.

### Technology Stack
Bring-your-own license key and accounts. Voice Assistant uses the following:
- 🎤 Picovoice Porcupine for wake word word detection (Apache License 2.0, free tier available)
- 👂 Azure Cognitive Services for speech-to-text (Commercial, free tier available)