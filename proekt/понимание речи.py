# import pyttsx3
import json, pyaudio
import vosk
from vosk import Model, KaldiRecognizer

model = Model(r"C:\Users\movavi_school\PycharmProjects\pythondfs\proekt\vosk-model-ru-0.10")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# настройки голоса
# engine = pyttsx3.init()
# volume = engine.getProperty('volume')
# engine.setProperty('volume', volume+0.50)
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate-90)
# engine.say("Hallo world")
# voices = engine.getProperty('voices')
# engine.setProperty('', voices[0].id)



#  пишем функции для распознования речи (неужели)

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer["text"]:
                yield answer["text"]

for text in listen():
    print(text)
    # engine.save_to_file(text)
    if text == "пока":
        quit()
    elif text == "привет":
        print("Приветствую, хозяин")
# engine.runAndWait()