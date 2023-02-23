import random
import constants
import main_buttons
import select_language
import os
from gtts import gTTS
import time
from playsound import playsound
from tkinter import *
import my_speech_recognition
import ui_setup


class Vegetables:
    # def __init__(self):
    #     ui_setup.new_window()
        # ui_setup.start_timer()

    def vegetables(self,letter_lang, vegetables_list):
        ui_setup.new_window()
        ui_setup.stop_music()

        my_label = Label(image=ui_setup.vegetables_bg_image)
        my_label.place(x=0, y=0, relheight=1, relwidth=1)
        ui_setup.update_point()

        vegetable_index = random.randint(0,19)
        canvas = Canvas(width=350, height=320, bg='white')
        screen_text = canvas.create_text(150, 200, text=vegetables_list[vegetable_index], width=340, font=("Arial", 25, "bold"),
                           fill="red")
        # print(one_to_twenty)
        canvas.grid(column=1, row=3, rowspan=5)
        canvas.create_image(175, 100, image=ui_setup.vegetables_list_photo[vegetable_index])
        canvas.grid(column=1, row=2, rowspan=5)




        def next_command():
            Vegetables.vegetables(self,letter_lang, vegetables_list)

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
        main_buttons.home_button()
        main_buttons.next_button(next_command)
        main_buttons.prev_button(self.vegetables_lang_selec)
        main_buttons.mic_button(lambda:my_speech_recognition.SpeechToText(canvas.itemcget(screen_text, 'text'),letter_lang))

    def vegetables_eng(self):
        self.vegetables("en", constants.vegetables_list_eng)

    def vegetables_tr(self):
        self.vegetables("tr", constants.vegetables_list_tr)

    def vegetables_ru(self):
        self.vegetables("ru", constants.vegetables_list_ru)

    def vegetables_de(self):
        self.vegetables("de", constants.vegetables_list_de)

    def vegetables_uz(self):
        pass

    def vegetables_lang_selec(self):
        ui_setup.new_window()

        select_language.select_lang(self.vegetables_eng, self.vegetables_tr, self.vegetables_ru, self.vegetables_de,
                                    self.vegetables_uz)


