import threading
from tkinter import *
import ui_setup

# event object for stopping thread
stop_event = threading.Event()


# ---------------------------- KEY BUTTONS------------------------------- #
def home_button():
    home_button = Button(text="home", width=100, height=100, image=ui_setup.home_button_photo,
                         command=ui_setup.main_window)
    home_button.grid(column=0, row=1, rows=3, sticky=NE)


def next_button(command_func):
    next_button = Button(text="Next", width=100, height=100, image=ui_setup.next_button_photo, bg='blue',
                         command=command_func)
    next_button.grid(column=3, row=1, rowspan=3, sticky=NE)


def prev_button(command_func):
    previous_button = Button(text="Previous", width=100, height=100, image=ui_setup.previous_button_photo, bg='blue',
                             command=command_func)
    previous_button.grid(column=0, row=3, rowspan=2, sticky=SE)


def sound_button(command_func):
    sound_button = Button(text="Sound", width=100, height=100, image=ui_setup.sound_button_photo, bg='blue',
                          command=lambda: threading.Thread(target=command_func).start())
    sound_button.grid(column=3, row=4)


def mic_button(command_func):
    mic_button = Button(text="Sound", width=100, height=100, image=ui_setup.mic_button_photo, bg='blue',
                        command=lambda: threading.Thread(target=command_func).start())
    mic_button.grid(column=3, row=5)



def stop_threads():
    stop_event.set()
