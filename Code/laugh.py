### code for laughter detection
# import necessary packages - install if not found
import pyaudio
import wave
import time

# set parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

# open audio object and start stream
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True, frames_per_buffer=CHUNK)

# track time to run the recorder
endTime  = time.time()+5

frames = []
# get audio frames and store them
while time.time() < endTime:
    data = stream.read(CHUNK)
    frames.append(data)

# stopr reading audio and stream
stream.stop_stream()
stream.close()
audio.terminate()

#write audio to wave file
audioFile = wave.open('../audio.wav','wb')
audioFile.setnchannels(CHANNELS)
audioFile.setsampwidth(audio.get_sample_size(FORMAT))
audioFile.setframerate(RATE)
audioFile.writeframes(b''.join(frames))         
audioFile.close()
