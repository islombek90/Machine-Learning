import constants
import main_buttons
from tkinter import *
import ui_setup


def select_lang(eng_button_command, tr_button_command, ru_button_command, de_button_command, uz_button_command):
    my_label = Label(image=ui_setup.lang_select_bg_image)
    my_label.place(x=0, y=0, relheight=1, relwidth=1)
    main_buttons.home_button()
    eng_button = Button(text="English", width=350, height=140 ,image=ui_setup.eng_flag_button_photo, bg='blue',
                        command=eng_button_command)
    eng_button.grid(column=1, row=0,padx=2,pady=5)

    tr_button = Button(text="Türkçe", width=350, height=140,  image=ui_setup.tr_flag_button_photo, bg='red',
                       command=tr_button_command)
    tr_button.grid(column=1, row=1,pady=2)

    ru_button = Button(text="Русский", width=350, height=140,  image=ui_setup.ru_flag_button_photo, bg='blue',
                       command=ru_button_command)
    ru_button.grid(column=1, row=2, pady=2)

    de_button = Button(text="Deutsch", width=350, height=140,  image=ui_setup.de_flag_button_photo, bg='black',
                       command=de_button_command)
    de_button.grid(column=1, row=3, pady=2)

    uz_button = Button(text="Узбекча", width=350, height=140,  image=ui_setup.uz_flag_button_photo, bg='blue',
                       command=uz_button_command)
    uz_button.grid(column=2, row=0, pady=2)



