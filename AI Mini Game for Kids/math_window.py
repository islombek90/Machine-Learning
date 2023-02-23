import constants
import main_buttons
import select_language
import random
import os
from gtts import gTTS
import time
import datetime as dt
from playsound import playsound
from tkinter import *
import ui_setup
import my_speech_recognition
import csv

# with open("data.csv", 'a') as new_data:
# new_data = pd.DataFrame(columns=["Name", "Subject", "Question", "Correct Answers", "Selected Answers","Result"])
# new_data.to_csv("data.csv")




def write_to_csv(name, subject, question, correct_answer, selected_answer,result):
    date = dt.datetime.now().strftime("%D")
    time = dt.datetime.now().strftime("%H:%M:%S")


    with open("data/data.csv", 'a') as new_data:
        writer = csv.writer(new_data)
        writer.writerow([f"{date}",f"{time}",name, subject,question,correct_answer,selected_answer, result,f"{constants.point}"])

color_list_eng = ["black", "gray", "brown", "red", "purple", "green", "blue"]

def math():
    ui_setup.new_window()

    my_label = Label(image=ui_setup.math_background_image)
    my_label.place(x=1, y=1, relheight=1, relwidth=1)
    main_buttons.home_button()

    if constants.name == "Samira":
        button_state = DISABLED
    else:
        button_state = NORMAL

    counting_button = Button( width=350, height=100, image=ui_setup.numbers_button_photo, command=count.count_lang_selec)
    counting_button.grid(column=1, row=2)

    addition_button = Button(width=350, height=100, image=ui_setup.addition_button_photo, state=button_state,command=add.addition)
    addition_button.grid(column=1, row=3)

    subtraction_button = Button(width=350, height=100, image=ui_setup.subtraction_button_photo, state=button_state, command=subtract.subtraction)
    subtraction_button.grid(column=1, row=4)
# ---------------------------- MATH WINDOW OPERATIONAL BUTTONS ------------------------------- #

class Addition:

    # def __init__(self):
    #     ui_setup.new_window()


    def addition(self):
        ui_setup.new_window()
        ui_setup.stop_music()

        my_label = Label(image=ui_setup.add_sub_bg_image)
        my_label.place(x=0, y=0, relheight=1, relwidth=1)
        ui_setup.update_point()

        generate_random_number1 = random.randint(1, 10)
        generate_random_number2 = random.randint(1, 10)
        sum_of_two = generate_random_number1 + generate_random_number2

        answer_choices = random.sample(range(1, 21), 3)
        if sum_of_two not in answer_choices:
            answer_choices.append(sum_of_two)
        else:
            answer_choices = random.sample(range(1,21),3)
            answer_choices.append(sum_of_two)



            # print(answer_choices)
        random.shuffle(answer_choices)
        # print(answer_choices)

        canvas = Canvas(width=310, height=320, bg='white')
        canvas.create_text(150, 150, text=f'{generate_random_number1}+{generate_random_number2} =?', width=250,
                           font=("Arial", 40, "bold"),
                           fill=random.choice(color_list_eng))

        canvas.grid(column=1, row=1, rows=5)

        def check_answerA():
            if answer_choices[0] == sum_of_two:
                ui_setup.correct_answer_sound_effect()
                print('correct')
                constants.point +=2

                write_to_csv(f"{constants.name}", "addition", f"{generate_random_number1}+{generate_random_number2}",
                             f"{sum_of_two}",f"{answer_choices[0]}", "correct")

                time.sleep(1)
                self.addition()
            else:
                ui_setup.wrong_answer_sound_effect()
                print('wrong')
                write_to_csv(f"{constants.name}", "addition", f"{generate_random_number1}+{generate_random_number2}",
                             f"{sum_of_two}", f"{answer_choices[0]}","wrong")

                answer_buttonA.config(bg='red')

        def check_answerB():
            if answer_choices[1] == sum_of_two:
                ui_setup.correct_answer_sound_effect()
                print('correct')
                write_to_csv(f"{constants.name}", "addition", f"{generate_random_number1}+{generate_random_number2}",
                             f"{sum_of_two}",f"{answer_choices[1]}", "correct")

                constants.point +=2
                time.sleep(1)
                self.addition()

            else:
                ui_setup.wrong_answer_sound_effect()
                print('wrong')
                write_to_csv(f"{constants.name}", "addition", f"{generate_random_number1}+{generate_random_number2}",
                             f"{sum_of_two}",f"{answer_choices[1]}", "wrong")

                answer_buttonB.config(bg='red')

        def check_answerC():
            if answer_choices[2] == sum_of_two:
                ui_setup.correct_answer_sound_effect()
                print('correct')
                write_to_csv(f"{constants.name}", "addition", f"{generate_random_number1}+{generate_random_number2}",
                             f"{sum_of_two}",f"{answer_choices[2]}", "correct")

                constants.point +=2
                time.sleep(1)
                self.addition()
            else:
                ui_setup.wrong_answer_sound_effect()
                print('wrong')
                write_to_csv(f"{constants.name}", "addition", f"{generate_random_number1}+{generate_random_number2}",
                             f"{sum_of_two}", f"{answer_choices[2]}","wrong")

                answer_buttonC.config(bg='red')

        def check_answerD():
            if answer_choices[3] == sum_of_two:
                ui_setup.correct_answer_sound_effect()
                print('correct')
                write_to_csv(f"{constants.name}", "addition", f"{generate_random_number1}+{generate_random_number2}",
                             f"{sum_of_two}",f"{answer_choices[3]}", "correct")

                constants.point +=2
                time.sleep(1)
                self.addition()
            else:
                ui_setup.wrong_answer_sound_effect()
                print('wrong')
                write_to_csv(f"{constants.name}", "addition", f"{generate_random_number1}+{generate_random_number2}",
                             f"{sum_of_two}",f"{answer_choices[3]}", "wrong")

                answer_buttonD.config(bg='red')

        answer_buttonA = Button(text=f'A) {answer_choices[0]}', font=ui_setup.myFont, width=10, bg='white',
                                command=check_answerA)
        answer_buttonA.grid(column=2, row=2)
        answer_buttonB = Button(text=f'B) {answer_choices[1]}', font=ui_setup.myFont, width=10, bg='white',
                                command=check_answerB)
        answer_buttonB.grid(column=2, row=3)
        answer_buttonC = Button(text=f'C) {answer_choices[2]}', font=ui_setup.myFont, width=10, bg='white',
                                command=check_answerC)
        answer_buttonC.grid(column=2, row=4)
        answer_buttonD = Button(text=f'D) {answer_choices[3]}', font=ui_setup.myFont, width=10, bg='white',
                                command=check_answerD)
        answer_buttonD.grid(column=2, row=5)

        main_buttons.next_button(self.addition)
        main_buttons.home_button()
        main_buttons.prev_button(math)


class Subtraction:
    # def __init__(self):
    #     ui_setup.new_window()

    def subtraction(self):
        ui_setup.new_window()
        ui_setup.stop_music()

        my_label = Label(image=ui_setup.add_sub_bg_image)
        my_label.place(x=0, y=0, relheight=1, relwidth=1)
        ui_setup.update_point()


        generate_random_number1 = random.randint(1, 10)
        generate_random_number2 = random.randint(1, 10)
        if generate_random_number1 > generate_random_number2:
            subtrc = generate_random_number1 - generate_random_number2
        else:
            subtrc = generate_random_number2 - generate_random_number1

        answer_choices = random.sample(range(1, 21), 3)
        if subtrc not in answer_choices:
            answer_choices.append(subtrc)
        else:
            answer_choices = random.sample(range(1, 21), 3)
            answer_choices.append(subtrc)

        # print(answer_choices)
        random.shuffle(answer_choices)
        # print(answer_choices)
        #
        subtrc_string= ""
        canvas = Canvas(width=310, height=320, bg='white')
        if generate_random_number1 > generate_random_number2:
            canvas.create_text(150, 150, text=f'{generate_random_number1}-{generate_random_number2} =?', width=250,
                               font=("Arial", 40, "bold"),
                               fill=random.choice(color_list_eng))
            subtrc_string = f'{generate_random_number1}-{generate_random_number2}'

        else:
            canvas.create_text(150, 150, text=f'{generate_random_number2}-{generate_random_number1} =?', width=250,
                               font=("Arial", 40, "bold"),
                               fill=random.choice(color_list_eng))
            subtrc_string = f'{generate_random_number2}-{generate_random_number1}'


        print(generate_random_number1, generate_random_number2)
        canvas.grid(column=1, row=1, rowspan=5)

        def check_answerA():
            if answer_choices[0] == subtrc:
                ui_setup.correct_answer_sound_effect()
                print('correct')
                write_to_csv(f"{constants.name}", "Subtraction", subtrc_string,
                             f"{subtrc}", f"{answer_choices[0]}", "correct")
                answer_buttonA.config(activebackground='green')
                constants.point +=3
                time.sleep(1)
                self.subtraction()
            else:
                ui_setup.wrong_answer_sound_effect()
                print('wrong')
                write_to_csv(f"{constants.name}", "Subtraction", subtrc_string,
                             f"{subtrc}", f"{answer_choices[0]}", "wrong")
                answer_buttonA.config(bg='red')

        def check_answerB():
            if answer_choices[1] == subtrc:
                ui_setup.correct_answer_sound_effect()
                print('correct')
                write_to_csv(f"{constants.name}", "Subtraction", subtrc_string,
                             f"{subtrc}", f"{answer_choices[1]}", "correct")
                constants.point +=3
                answer_buttonB.config(activebackground='green')
                time.sleep(1)

                self.subtraction()

            else:
                ui_setup.wrong_answer_sound_effect()
                print('wrong')
                write_to_csv(f"{constants.name}", "Subtraction", subtrc_string,
                             f"{subtrc}", f"{answer_choices[1]}", "wrong")
                answer_buttonB.config(bg='red')

        def check_answerC():
            if answer_choices[2] == subtrc:
                ui_setup.correct_answer_sound_effect()
                print('correct')
                write_to_csv(f"{constants.name}", "Subtraction", subtrc_string,
                             f"{subtrc}", f"{answer_choices[2]}", "correct")
                constants.point +=3
                answer_buttonC.config(activebackground='green')
                time.sleep(1)

                self.subtraction()
            else:
                ui_setup.wrong_answer_sound_effect()
                print('wrong')
                write_to_csv(f"{constants.name}", "Subtraction", subtrc_string,
                             f"{subtrc}", f"{answer_choices[2]}", "wrong")
                answer_buttonC.config(bg='red')

        def check_answerD():
            if answer_choices[3] == subtrc:
                ui_setup.correct_answer_sound_effect()
                print('correct')
                write_to_csv(f"{constants.name}", "Subtraction", subtrc_string,
                             f"{subtrc}", f"{answer_choices[3]}", "correct")
                constants.point +=3
                answer_buttonD.config(activebackground='green')
                time.sleep(1)


                self.subtraction()
            else:
                ui_setup.wrong_answer_sound_effect()
                print('wrong')
                write_to_csv(f"{constants.name}", "Subtraction", subtrc_string,
                             f"{subtrc}", f"{answer_choices[3]}", "wrong")
                answer_buttonD.config(bg='red')

        answer_buttonA = Button(text=f'A) {answer_choices[0]}', font=ui_setup.myFont, width=10, bg='white',
                                command=check_answerA)
        answer_buttonA.grid(column=2, row=2, sticky=W)
        answer_buttonB = Button(text=f'B) {answer_choices[1]}', font=ui_setup.myFont, width=10, bg='white',
                                command=check_answerB)
        answer_buttonB.grid(column=2, row=3, sticky=W)
        answer_buttonC = Button(text=f'C) {answer_choices[2]}', font=ui_setup.myFont, width=10, bg='white',
                                command=check_answerC)
        answer_buttonC.grid(column=2, row=4, sticky=W)
        answer_buttonD = Button(text=f'D) {answer_choices[3]}', font=ui_setup.myFont, width=10, bg='white',
                                command=check_answerD)
        answer_buttonD.grid(column=2, row=5, sticky=W)

        main_buttons.next_button(self.subtraction)
        main_buttons.home_button()
        main_buttons.prev_button(math)


class Count:
    # def __init__(self):
    #     ui_setup.new_window()
        # ui_setup.start_timer()

    def count(self,letter_lang):
        ui_setup.new_window()
        ui_setup.stop_music()

        my_label = Label(image=ui_setup.count_background_image)
        my_label.place(x=1, y=1, relheight=1, relwidth=1)
        ui_setup.update_point()

        one_to_twenty = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

        canvas = Canvas(width=350, height=320, bg='white')
        screen_text = canvas.create_text(175, 125, text=one_to_twenty, width=340, font=("Arial", 25, "bold"),
                           fill=random.choice(color_list_eng))
        # print(one_to_twenty)
        canvas.grid(column=1, row=2, rowspan=5)


        def next_command():
            letter_to_sound = random.randint(1, 20)
            canvas.itemconfig(screen_text, text=letter_to_sound, font=("Arial", 100, "bold"))

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
            canvas.itemconfig(screen_text, fill="red")

        main_buttons.sound_button(text_to_speech)
        main_buttons.home_button()
        main_buttons.next_button(next_command)
        main_buttons.prev_button(self.count_lang_selec)
        main_buttons.mic_button(lambda:my_speech_recognition.SpeechToText(canvas.itemcget(screen_text, 'text'),letter_lang))

    def counting_eng(self):
        self.count("en")

    def counting_tr(self):
        self.count("tr")

    def counting_ru(self):
        self.count("ru")

    def counting_de(self):
        self.count("de")

    def counting_uz(self):
        pass

    def count_lang_selec(self):
        ui_setup.new_window()

        select_language.select_lang(self.counting_eng, self.counting_tr, self.counting_ru, self.counting_de,
                                    self.counting_uz)


add = Addition()
subtract = Subtraction()
count =Count()

# data = pd.read_csv("data\data.csv")
# print(data.head())