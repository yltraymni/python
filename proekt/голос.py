
import pyttsx3
engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume', volume+0.50)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-90)
engine.say("Hallo world")
voices = engine.getProperty('voices')
engine.setProperty('', voices[0].id)
engine.save_to_file("Здравствуйте, это тест для pyttsx3.", "test.mp3")
engine.runAndWait()


















import pyttsx3
engine = pyttsx3.init()

volume = engine.getProperty('volume')       # Громкость
engine.setProperty('volume', volume+0.50)   # воспроизведения

rate = engine.getProperty('rate')     # Скорость
engine.setProperty('rate', rate-90)   # воспроизведения

engine.say("Hallo world")   # Сказать

voices = engine.getProperty('voices')   # Выбор голоса
engine.setProperty('', voices[0].id)    # voices[1] - мужской, voices[0] - женский

engine.save_to_file("Здравствуйте, это тест для pyttsx3.", "test.mp3")

engine.runAndWait()     # Запускает и ждет действий