import constants
import main_buttons
import my_clock
import os
import webbrowser
from tkinter import *
import ui_setup


# ---------------------------- GAME SETUP ------------------------------- #
from Pacman import pacman

constants.LEVEL1_SCORE = 50
constants.LEVEL2_SCORE = 200
constants.LEVEL3_SCORE = 200


def entertaiment():
    ui_setup.new_window()
    my_label = Label(image=ui_setup.games_bg_image)
    my_label.place(x=0, y=0, relheight=1, relwidth=1)
    main_buttons.home_button()
    # if my_clock.get_counter() > 3600 or  LEVEL1_SCORE <= constants.point < LEVEL2_SCORE:

    if constants.LEVEL1_SCORE <= constants.point < constants.LEVEL2_SCORE:
        button_state_lvl1 = NORMAL
        button_state_lvl2 = DISABLED
        button_state_lvl3 = DISABLED
    elif constants.LEVEL2_SCORE <= constants.point < constants.LEVEL3_SCORE:
        button_state_lvl1 = NORMAL
        button_state_lvl2 = NORMAL
        button_state_lvl3 = DISABLED
    elif constants.LEVEL3_SCORE <= constants.point:
        button_state_lvl1 = NORMAL
        button_state_lvl2 = NORMAL
        button_state_lvl3 = NORMAL

    else:
        button_state_lvl1 = DISABLED
        button_state_lvl2 = DISABLED
        button_state_lvl3 = DISABLED

    canvas = Canvas(width=100, height=50, highlightthickness=0)
    canvas2 = Canvas(width=100, height=50, highlightthickness=0)
    canvas3 = Canvas(width=100, height=50, highlightthickness=0)
    canvas4 = Canvas(width=100, height=50, highlightthickness=0)
    canvas5 = Canvas(width=100, height=50, highlightthickness=0)
    canvas6 = Canvas(width=100, height=50, highlightthickness=0)


    game_button = Button(text="........", width=150, height=120, image=ui_setup.gta_button_photo, state=button_state_lvl3, command=game)
    game_button.grid(column=3, row=1, sticky=W)
    canvas.create_text(50, 25, text=f'{constants.point}:{constants.LEVEL3_SCORE}', width=100, font=("Arial", 20, "bold"),
                       fill="black")
    canvas.grid(column=4, row=1)

    pacman_button = Button(text="........", width=150, height=120, image=ui_setup.pacman_button_photo, state=button_state_lvl1, command=pacman.main)
    pacman_button.grid(column=3, row=2, sticky=W)
    canvas6.create_text(50, 25, text=f'{constants.point}:{constants.LEVEL1_SCORE}', width=100, font=("Arial", 20, "bold"),
                       fill="black")
    canvas6.grid(column=4, row=2)

    youtube_button = Button(text="........", width=150, height=120, image=ui_setup.youtube_button_photo,state=button_state_lvl2,   command=youtube)
    youtube_button.grid(column=1, row=4, sticky=W)
    canvas2.create_text(50, 25, text=f'{constants.point}:{constants.LEVEL2_SCORE}', width=100, font=("Arial", 20, "bold"),
                       fill="black")
    canvas2.grid(column=2, row=4)

    scratch_button = Button(text="........", width=150, height=120, image=ui_setup.scratch_button_photo,state=button_state_lvl1,   command=scratch)
    scratch_button.grid(column=1, row=1, sticky=W)
    canvas3.create_text(50, 25, text=f'{constants.point}:{constants.LEVEL1_SCORE}', width=100, font=("Arial", 20, "bold"),
                       fill="black")
    canvas3.grid(column=2, row=1)


    code_lab_button = Button(text="........", width=150, height=120, image=ui_setup.code_lab_button_photo,state=button_state_lvl1,   command=code_lab)
    code_lab_button.grid(column=1, row=2, sticky=W)
    canvas4.create_text(50, 25, text=f'{constants.point}:{constants.LEVEL1_SCORE}', width=70, font=("Arial", 20, "bold"),
                       fill="black")
    canvas4.grid(column=2, row=2)

    mblock_button = Button(text="........", width=150, height=120, image=ui_setup.mblock_button_photo,state=button_state_lvl1,   command=m_block)
    mblock_button.grid(column=1, row=3, sticky=W)
    canvas5.create_text(50, 25, text=f'{constants.point}:{constants.LEVEL1_SCORE}', width=70, font=("Arial", 20, "bold"),
                       fill="black")
    canvas5.grid(column=2, row=3)


def game():

        print(my_clock.get_counter())
        ui_setup.stop_music()

        # os.startfile("D:\Games\GTAV\PlayGTAV.exe")
        url = "com.epicgames.launcher://apps/9d2d0eb64d5c44529cece33fe2a46482?action=launch&silent=true"
        webbrowser.open(url)
        # os.system("taskkill /f /im  Your_Process_Name.exe")


def youtube():

        print(my_clock.get_counter())
        ui_setup.stop_music()

        url = "https://www.youtube.com/results?search_query=hot+wheels"
        webbrowser.open(url)


def scratch():

        print(my_clock.get_counter())
        ui_setup.stop_music()

        url = "https://scratch.mit.edu/projects/editor/?tutorial=getStarted"
        webbrowser.open(url)


def code_lab():
    ui_setup.stop_music()

    url ="https://santatracker.google.com/"
    webbrowser.open(url)


def m_block():
    ui_setup.stop_music()

    url = "https://ide.mblock.cc/"
    webbrowser.open(url)