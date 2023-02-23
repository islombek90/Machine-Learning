import speech_recognition as sr
import pyttsx3
import constants
from tkinter import *
import math_window

# ----------------------------------LIST OF SUPPORTED LANGUAGES -------------------------------------------------###

# https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134
import ui_setup

message = f'Hello {constants.name}, how can i help you?'
message2 = f'Anything else Mr.{constants.name}?'
r1 = sr.Recognizer()
r2 = sr.Recognizer()
invalid_audio = False

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
print(len(voices))
try:
    engine.setProperty('voice', voices[2].id)
except IndexError:
    engine.setProperty('voice', voices[1].id)
except IndexError:
    engine.setProperty('voice', voices[0].id)



def SpeechToText(keyword, language):

    try:
        with sr.Microphone() as source:  # use the default microphone as the audio source


            engine.say(f"speak{constants.name}")
            engine.runAndWait()
            print('Speak please')
            ui_setup.play_music('data/start_record.mp3', 1)
            audio = r1.listen(source,10,3)  # listen for the first phrase and extract it into audio data
            # audio = r1.listen(source,phrase_time_limit=1)  # listen for the first phrase and extract it into audio data

            output = r1.recognize_google(audio, language=language)
            print("You said " + output)
            constants.mic_text = output

            # audio_data = init_rec.record(source, duration=5)
            # print("Recognizing your text.............")
            # text = init_rec.recognize_google(audio_data)
            # print(text)
            if str(keyword).lower() == str(output).lower():
                ui_setup.correct_answer_sound_effect()
                print(keyword)
                if language == "en":
                    constants.point += 2
                    math_window.write_to_csv(f"{constants.name}", "en",
                                 f"{keyword}",
                                 f"{keyword}", f"{output}", "correct")
                elif language =="tr":
                    constants.point += 1
                    math_window.write_to_csv(f"{constants.name}", "tr",
                                 f"{keyword}",
                                 f"{keyword}", f"{output}", "correct")
                elif language == "ru":
                    constants.point += 3
                    math_window.write_to_csv(f"{constants.name}", "ru",
                                 f"{keyword}",
                                 f"{keyword}", f"{output}", "correct")
                elif language == "de":
                    constants.point += 4
                    math_window.write_to_csv(f"{constants.name}", "de",
                                 f"{keyword}",
                                 f"{keyword}", f"{output}", "correct")
                print(constants.point)
                ui_setup.update_point()
            else:
                math_window.write_to_csv(f"{constants.name}", f'{language}',
                             f"{keyword}",
                             f"{keyword}", f"{output}", "wrong")


    except sr.UnknownValueError:  # speech is unintelligible
        print("Could not understand audio")
        engine.say("Could not understand audio'")
        math_window.write_to_csv(f"{constants.name}", "de",
                     f"{keyword}",
                     f"{keyword}", f"no speak", "not understandable")
        engine.runAndWait()
        # continue


