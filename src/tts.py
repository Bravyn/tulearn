from gtts import gTTS
from pathlib import Path

# Text to be converted to speech
text = "Today is a wonderful day to build something people love!"

# Initialize gTTS object
tts = gTTS(text=text, lang='en')

# Define the path to save the speech file
speech_file_path = Path(__file__).parent / "speech.mp3"

# Save the speech to a file
tts.save(speech_file_path)

print(f"Audio saved to {speech_file_path}")
