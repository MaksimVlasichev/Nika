import pyaudio
import json
from main import obr
from vosk import Model, KaldiRecognizer
model = Model('C:\\VScode\\voice_helper\\vosk-model-small-ru-0.22') 
recognizer = KaldiRecognizer(model, 16000)

cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, channels=1, rate= 16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(8192) 
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        res = json.loads(recognizer.Result())
        obr(res["text"])
        continue
        # if "выключи" in res["text"].casefold(): 
        #         print("++++")
        #         raise SystemExit