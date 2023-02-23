import random
import constants
import main_buttons
import select_language
import os
from gtts import gTTS
import time
from playsound import playsound
from tkinter import *
import tkinter
import my_speech_recognition
import ui_setup
from PIL import ImageTk, Image



# arrow_image = PhotoImage(file="data/shapes/Arrow.png")
# circle_image = PhotoImage(file="data/shapes/Circle.png")
# heart_image = PhotoImage(file="data/shapes/Heart.png")
# hexagon_image = PhotoImage(file="data/shapes/Hexagon.png")
# oval_image = PhotoImage(file="data/shapes/Oval.png")
# parallelogram_image = PhotoImage(file="data/shapes/Parallelogram.png")
# pentagon_image = PhotoImage(file="data/shapes/Pentagon.png")
# rectangle_image = PhotoImage(file="data/shapes/Rectangle.png")
# rhombus_image = PhotoImage(file="data/shapes/Rhombus.png")
# right_triangle_image = PhotoImage(file="data/shapes/Right Triangle.png")
# square_image = PhotoImage(file="data/shapes/Square.png")
# star_image = PhotoImage(file="data/shapes/Star.png")
# trapezoid_image = PhotoImage(file="data/shapes/Trapezoid.png")
# triangle_image = PhotoImage(file="data/shapes/Triangle.png")



class Shapes:
    # def __init__(self):
    #     ui_setup.new_window()
        # ui_setup.start_timer()

    def shapes(self,letter_lang, shape_list):
        ui_setup.new_window()
        ui_setup.stop_music()

        my_label = Label(image=ui_setup.letters_bg_image)
        my_label.place(x=0, y=0, relheight=1, relwidth=1)
        ui_setup.update_point()

        shape_index = random.randint(0,13)
        canvas = Canvas(width=350, height=320, bg='white')
        screen_text = canvas.create_text(150, 200, text=shape_list[shape_index], width=340, font=("Arial", 25, "bold"),
                           fill="red")
        # print(one_to_twenty)
        canvas.grid(column=1, row=3, rowspan=5)
        canvas.create_image(175, 100, image=ui_setup.shape_list_photo[shape_index])
        canvas.grid(column=1, row=2, rowspan=5)




        def next_command():
            Shapes.shapes(self,letter_lang, shape_list)

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
        main_buttons.prev_button(self.shapes_lang_selec)
        main_buttons.mic_button(lambda:my_speech_recognition.SpeechToText(canvas.itemcget(screen_text, 'text'),letter_lang))

    def shapes_eng(self):
        self.shapes("en", constants.shapes_list_eng)

    def shapes_tr(self):
        self.shapes("tr", constants.shapes_list_tr)

    def shapes_ru(self):
        self.shapes("ru", constants.shapes_list_ru)

    def shapes_de(self):
        self.shapes("de", constants.shapes_list_de)

    def shapes_uz(self):
        pass

    def shapes_lang_selec(self):
        ui_setup.new_window()

        select_language.select_lang(self.shapes_eng, self.shapes_tr, self.shapes_ru, self.shapes_de,
                                    self.shapes_uz)


