import random
import constants
import main_buttons
import select_language
import os
from gtts import gTTS
import time
from playsound import playsound
from tkinter import *
from my_speech_recognition import SpeechToText
import ui_setup


def color():
    ui_setup.new_window()
    select_language.select_lang(english_colors,turkish_colors, russian_colors, deutsch_colors, uzbek_colors)

# ---------------------------- COLORS WINDOW OPERATIONAL BUTTONS ------------------------------- #

def color_lang_select(lang,colors_list, next_func, prev_func ):
    ui_setup.new_window()
    ui_setup.stop_music()

    my_label = Label(image=ui_setup.colors_bg_image)
    my_label.place(x=0, y=0, relheight=1, relwidth=1)

    ui_setup.update_point()
    color = random.randint(0,8)
    canvas = Canvas(width=310, height=220, bg=constants.color_list_eng[color])
    screen_text=canvas.create_text(150, 100, text=f'{colors_list[color]}', width=250, font=("Arial", 35, "bold"),
                       fill="black")
    canvas.grid(column=1, rowspan=4)

    main_buttons.home_button()

    main_buttons.next_button(next_func)

    main_buttons.prev_button(prev_func)

    def text_to_speech():
        mytext = canvas.itemcget(screen_text, 'text')
        language = lang
        myobj = gTTS(text=mytext, lang=language, slow=True)
        try:
            os.remove("data/welcome1.mp3")
        except FileNotFoundError:
            print("file not created yet")
        myobj.save("data/welcome1.mp3")
        time.sleep(1)
        playsound("data/welcome1.mp3")

    main_buttons.sound_button(text_to_speech)
    main_buttons.mic_button(lambda: SpeechToText(canvas.itemcget(screen_text, 'text'), lang))


def english_colors():
    color_lang_select("en", constants.color_list_eng, english_colors,color)


def turkish_colors():
    color_lang_select("tr", constants.color_list_tr, turkish_colors, color)


def russian_colors():
    color_lang_select("ru", constants.color_list_ru, russian_colors, color)


def deutsch_colors():
    color_lang_select("de", constants.color_list_de, deutsch_colors, color)


def uzbek_colors():
    pass

