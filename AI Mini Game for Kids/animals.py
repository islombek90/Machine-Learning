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


def animal_types_selection():
    ui_setup.new_window()

    my_label = Label(image=ui_setup.animals_bg_image)
    my_label.place(x=0, y=0, relheight=1, relwidth=1)
    main_buttons.home_button()

    birds_button = Button( width=350, height=100, bg="white", image=ui_setup.Eagle_image, command=birds.animal_lang_selec)
    birds_button.grid(column=1, row=2)

    domestic_animals_button = Button(width=350, height=100, bg="white", image=ui_setup.Hen_image, state=NORMAL,
                                     command=domestic_animals.animal_lang_selec)
    domestic_animals_button.grid(column=1, row=3)

    insects_button = Button(width=350, height=100,bg="white",  image=ui_setup.Ant_image, state=NORMAL,
                            command=insects.animal_lang_selec)
    insects_button.grid(column=1, row=4)

    mammals_button = Button(width=350, height=100, bg="white", image=ui_setup.Cow_image,
                           command=mammals.animal_lang_selec)
    mammals_button.grid(column=1, row=5)

    pet_animals_button = Button(width=350, height=100, bg="white", image=ui_setup.Dog_image, state=NORMAL,
                                command=pet_animals.animal_lang_selec)
    pet_animals_button.grid(column=1, row=6)

    sea_animals_button = Button(width=350, height=100, bg="white", image=ui_setup.Goldfish_image, state=NORMAL,
                                command=sea_animals.animal_lang_selec)
    sea_animals_button.grid(column=2, row=2)

    wild_animals_button = Button(width=350, height=100, bg="white", image=ui_setup.Tiger_image, state=NORMAL,
                                 command=wild_animals.animal_lang_selec)
    wild_animals_button.grid(column=2, row=3)


class Animals:
    def __init__(self, animal_list_dict, animal_photo):
        self.animal_type = animal_list_dict
        self.animal_type_photo = animal_photo
        # print(self.animal_type)

    def animal(self,letter_lang, animal_list, animal_type_photo):
        ui_setup.new_window()
        ui_setup.stop_music()

        my_label = Label(image=ui_setup.animals_bg_image)
        my_label.place(x=0, y=0, relheight=1, relwidth=1)
        ui_setup.update_point()
        # print(len(animal_list))
        animal_index = random.randint(0, (len(animal_list)-1))
        canvas = Canvas(width=350, height=320, bg='white')
        screen_text = canvas.create_text(150, 200, text=animal_list[animal_index], width=340, font=("Arial", 25, "bold"),
                           fill="red")
        # print(one_to_twenty)
        canvas.grid(column=1, row=3, rowspan=5)
        canvas.create_image(175, 100, image=animal_type_photo[animal_index])
        canvas.grid(column=1, row=2, rowspan=5)



        def next_command():
            Animals.animal(self,letter_lang, animal_list, animal_type_photo)

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
        main_buttons.prev_button(self.animal_lang_selec)
        main_buttons.mic_button(lambda:my_speech_recognition.SpeechToText(canvas.itemcget(screen_text, 'text'),letter_lang))

    def animal_eng(self):
        self.animal("en", self.animal_type["en"], self.animal_type_photo )

    def animal_tr(self):
        self.animal("tr", self.animal_type["tr"], self.animal_type_photo)

    def animal_ru(self):
        self.animal("ru", self.animal_type["ru"], self.animal_type_photo)

    def animal_de(self):
        self.animal("de", self.animal_type["de"], self.animal_type_photo)

    def animal_uz(self):
        pass

    def animal_lang_selec(self):
        ui_setup.new_window()

        select_language.select_lang(self.animal_eng, self.animal_tr, self.animal_ru, self.animal_de,
                                    self.animal_uz)


domestic_animals = Animals(constants.domestic_animal_list_dict, ui_setup.domestic_animal_photo)
birds = Animals(constants.birds_list_dict, ui_setup.birds_list_photo)
insects = Animals(constants.insects_animal_list_dict, ui_setup.insects_animal_photo)
pet_animals = Animals(constants.pet_animal_list_dict, ui_setup.pet_animal_photo)
mammals = Animals(constants.mammal_animal_list_dict, ui_setup.mammal_animal_photo)
sea_animals = Animals(constants.sea_animal_list_dict, ui_setup.sea_animal_photo)
wild_animals = Animals(constants.wild_animal_list_dict, ui_setup.wild_animal_photo)

