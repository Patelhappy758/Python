import sounddevice
from scipy.io.wavfile import write

def voice_recorder(seconds, file):
    print("Recording...")
    happyRecording = sounddevice.rec((seconds * 44100), samplerate=44100, channels=1)
    sounddevice.wait()  # Wait until recording is finished
    write(file, 44100, happyRecording)  # Save as WAV file
    print(f"Recording saved")

# Get user input
duration = int(input("Enter recording duration in seconds: "))
filename = input("Enter filename to save (e.g., output.wav): ")
voice_recorder(duration, filename)