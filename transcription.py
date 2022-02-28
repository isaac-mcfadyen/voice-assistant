import azure.cognitiveservices.speech as speechsdk
import os

speech_config = None
audio_config = None
speech_recognizer = None

def initialize_transcription():
    global speech_config
    global audio_config
    global speech_recognizer

    speech_config = speechsdk.SpeechConfig(subscription=os.getenv("AZURE_ACCESS_KEY"), region=os.getenv("AZURE_REGION"), speech_recognition_language="en-US")
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

def run_transcription():
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return True, speech_recognition_result.text
    else:
        return False, None
