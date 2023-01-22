import sounddevice

from scipy.io.wavfile import write

seconds = 5
fps = 44100

record = sounddevice.rec(frames=seconds * fps, samplerate=fps, channels=1)
sounddevice.wait()
print(f'{record=}')
write('output.wav', fps, record)

