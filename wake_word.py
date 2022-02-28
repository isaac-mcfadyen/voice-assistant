import pvporcupine

porcupine = None

def initialize_wake_word():
  global porcupine
  # Create a new PVPorcupine instance.
  porcupine = pvporcupine.create(
    access_key=os.getenv("PICOVOICE_ACCESS_KEY"),
    keyword_paths=['./data/picovoice/porcupine.ppn']
  )
  return porcupine.sample_rate, porcupine.frame_length
  

def run_wake_word(audio_frame):
  # Check if the audio frame contains the wake word.
  result = porcupine.process(audio_frame)
  if result != -1:
    print('Wake word detected!')
    return True
  else:
    return False

def clean_up_wake_word():
  # Clean up porcupine.
  porcupine.delete()