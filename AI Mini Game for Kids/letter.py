import constants
import main_buttons
import select_language
import random
from gtts import gTTS
import os
import time
from playsound import playsound
from tkinter import *
from my_speech_recognition import SpeechToText
import ui_setup

color_list_eng = ["black", "gray", "brown", "red", "purple", "green", "yellow", "blue"]


# ---------------------------- ABC WINDOW OPERATIONAL BUTTONS ------------------------------- #


def letters_lang_select(letter_lang, letter):
    ui_setup.new_window()
    ui_setup.stop_music()
    my_label = Label(image=ui_setup.letters_bg_image)
    my_label.place(x=0, y=0, relheight=1, relwidth=1)
    ui_setup.update_point()

    canvas = Canvas(width=510, height=410, bg='white')
    screen_text = canvas.create_text(250, 200, text=letter, width=450, font=("Helvetica", 35, "bold"),
                       fill=random.choice(color_list_eng))
    canvas.grid(column=1, rowspan=10)
    list_to_be_selected = letter
    def next_command():
        letter_to_sound = random.choice(list_to_be_selected)
        canvas.itemconfig(screen_text, text=letter_to_sound, font=("Helvetica", 85, "bold"))

    main_buttons.next_button(next_command)
    main_buttons.home_button()
    main_buttons.prev_button(lang)

    def text_to_speech():
        mytext = canvas.itemcget(screen_text, 'text')

        language = letter_lang
        myobj = gTTS(text=mytext, lang=language, slow=True)
        try:
            os.remove("data/welcome1.mp3")
        except FileNotFoundError:
            print("file not created yet")
        myobj.save("data/welcome1.mp3")
        time.sleep(1)
        playsound("data/welcome1.mp3")

    main_buttons.sound_button(text_to_speech)
    main_buttons.mic_button(lambda: SpeechToText(canvas.itemcget(screen_text, 'text'), letter_lang))


def english():
    letters_lang_select("en", random.choice(constants.letters_Eng_list))


def turkish():
    letters_lang_select("tr", random.choice(constants.letters_tr_list))


def russian():
    letters_lang_select("ru", random.choice(constants.letter_ru_list))


def deutsch():
    letters_lang_select("de", random.choice(constants.letters_de_list))

def uzbek():
    pass



def lang():
    ui_setup.new_window()
    my_label = Label(image=ui_setup.lang_select_bg_image)
    my_label.place(x=0, y=0, relheight=1, relwidth=1)
    select_language.select_lang(english, turkish, russian, deutsch, uzbek)
