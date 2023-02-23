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


class Fruits:
    # def __init__(self):
    #     ui_setup.new_window()
        # ui_setup.start_timer()

    def fruits(self,letter_lang, fruit_list):
        ui_setup.new_window()
        ui_setup.stop_music()

        my_label = Label(image=ui_setup.letters_bg_image)
        my_label.place(x=0, y=0, relheight=1, relwidth=1)
        ui_setup.update_point()

        fruit_index = random.randint(0,22)
        canvas = Canvas(width=350, height=320, bg='white')
        screen_text = canvas.create_text(150, 200, text=fruit_list[fruit_index], width=340, font=("Arial", 25, "bold"),
                           fill="red")
        # print(one_to_twenty)
        canvas.grid(column=1, row=3, rowspan=5)
        canvas.create_image(175, 100, image=ui_setup.fruits_list_photo[fruit_index])
        canvas.grid(column=1, row=2, rowspan=5)




        def next_command():
            Fruits.fruits(self,letter_lang, fruit_list)

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
        main_buttons.prev_button(self.fruits_lang_selec)
        main_buttons.mic_button(lambda:my_speech_recognition.SpeechToText(canvas.itemcget(screen_text, 'text'),letter_lang))

    def fruits_eng(self):
        self.fruits("en", constants.fruits_list_eng)

    def fruits_tr(self):
        self.fruits("tr", constants.fruits_list_tr)

    def fruits_ru(self):
        self.fruits("ru", constants.fruits_list_ru)

    def fruits_de(self):
        self.fruits("de", constants.fruits_list_de)

    def fruits_uz(self):
        self.fruits("Uz", constants.fruits_list_uz)


    def fruits_lang_selec(self):
        ui_setup.new_window()

        select_language.select_lang(self.fruits_eng, self.fruits_tr, self.fruits_ru, self.fruits_de,
                                    self.fruits_uz)


