import pyaudio
import struct
import importlib
import os
from dotenv import load_dotenv

from wake_word import initialize_wake_word, run_wake_word, clean_up_wake_word
from transcription import initialize_transcription, run_transcription

load_dotenv()

# Initialize the seperate parts.
sample_rate, frame_length = initialize_wake_word()
initialize_transcription()

# Import the modules.
modules = []
for directory in os.listdir("./modules"):
    module = importlib.import_module('modules.' + directory + ".main", package=__file__)
    module.initialize()
    modules.append(module)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=sample_rate,
                input=True,
                frames_per_buffer=frame_length)


# Loop and sleep.
print("Ready!")
try:
    while True:
        # Ensure the stream is running.
        stream.start_stream()

        # Read a frame.
        audio = stream.read(frame_length)
        audio = struct.unpack_from("h" * frame_length, audio)

        # Run wake word detection.
        if run_wake_word(audio):
            # Pauae the stream.
            stream.stop_stream()

            # Run transcription.
            transcription_success, transcription = run_transcription()

            if not transcription_success:
                print("Transcription failed.")

            # Run the modules.
            for module in modules:
                can_answer = module.can_answer()
                if can_answer:
                    module.main(transcription)


except KeyboardInterrupt:
    clean_up_wake_word()
    stream.stop_stream()
    stream.close()
    p.terminate()