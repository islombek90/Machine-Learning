import pandas as pd
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox

import constants
import my_clock
import ui_setup


# WIDTH = 1024
# HEIGHT = 610
# root = Tk()
# root.title("Mini games for kids developer mode V1.0 2022")
# root.geometry(f'{WIDTH}x{HEIGHT}')
# root.resizable(0, 0)
# root.config(bg="cyan")

def developper_widow():
    ui_setup.new_window()


    rep_button = Button(text="Report", command=report)
    rep_button.grid(column=5, row=15, padx=20, pady=20)

    # Labels
    name_label = Label(text="NAME:", bg="cyan")
    name_label.grid(row=1, column=0, pady=2)
    lvl1_label = Label(text="LEVEL 1 POINT:", bg="cyan")
    lvl1_label.grid(row=2, column=0, pady=2)
    lvl2_label = Label(text="LEVEL 2 POINT:",bg="cyan")
    lvl2_label.grid(row=3, column=0, pady=2)
    lvl3_label = Label(text="LEVEL 3 POINT:", bg="cyan")
    lvl3_label.grid(row=4, column=0, pady=2)

    eng_label = Label(text="ENGLISH POINT:", bg="cyan")
    eng_label.grid(row=5, column=0, pady=2)
    rus_label = Label(text="RUSSIAN POINT:", bg="cyan")
    rus_label.grid(row=6, column=0, pady=2)
    tr_label = Label(text="TURKISH POINT:", bg="cyan")
    tr_label.grid(row=7, column=0, pady=2)
    de_label = Label(text="GERMAN POINT:", bg="cyan")
    de_label.grid(row=8, column=0, pady=2)

    addition_label = Label(text="ADDITION POINT:", bg="cyan")
    addition_label.grid(row=9, column=0, pady=2)
    subtraction_label = Label(text="SUBTRACTION POINT:", bg="cyan")
    subtraction_label.grid(row=10, column=0, pady=2)

    # Entries
    name_entry = Entry(width=10)
    name_entry.grid(row=1, column=2)
    lvl1_entry = Entry(width=10)
    lvl1_entry.grid(row=2, column=2)
    lvl2_entry = Entry(width=10)
    lvl2_entry.grid(row=3, column=2)
    lvl3_entry = Entry(width=10)
    lvl3_entry.grid(row=4, column=2)

    eng_entry = Entry(width=10)
    eng_entry.grid(row=5, column=2)
    rus_entry = Entry(width=10)
    rus_entry.grid(row=6, column=2)
    tr_entry = Entry(width=10)
    tr_entry.grid(row=7, column=2)
    dutch_entry = Entry(width=10)
    dutch_entry.grid(row=8, column=2)

    add_entry = Entry(width=10)
    add_entry.grid(row=9, column=2)
    sub_entry = Entry(width=10)
    sub_entry.grid(row=10, column=2)

    entries = [lvl1_entry, lvl2_entry, lvl3_entry,
               tr_entry, eng_entry, rus_entry, dutch_entry,
               add_entry, sub_entry]

    def save():
        constants.name = name_entry.get()

        try:
            constants.LEVEL1_SCORE = int(lvl1_entry.get())
        except ValueError:
            print("LEVEL1_SCORE  entry is empty ")
        try:
            constants.LEVEL2_SCORE = int(lvl2_entry.get())
        except ValueError:
            print("LEVEL2_SCORE entry is empty ")
        try:
            constants.LEVEL3_SCORE = int(lvl3_entry.get())
        except ValueError:
            print("LEVEL3_SCORE entry is empty ")
        try:
            constants.TURKISH_POINT = int(tr_entry.get())
        except ValueError:
            print("Turkish point entry is empty ")
        try:
            constants.ENGLISH_POINT = int(eng_entry.get())
        except ValueError:
            print("warning English point entry is empty  ")
        try:
            constants.RUSSIAN_POINT = int(rus_entry.get())
        except ValueError:
            print("warning Russian point entry is empty  ")
        try:
            constants.GERMAN_POINT = int(dutch_entry.get())
        except ValueError:
            print("warning German point entry is empty  ")
        try:
            constants.ADDITION_POINT = int(add_entry.get())
        except ValueError:
            print("warning Addition point entry is empty  ")
        try:
            constants.SUBTRACTION_POINT = int(sub_entry.get())
        except ValueError:
            print("warning Subtraction point entry is empty  ")

        finally:
            for entry in entries:
                if len(entry.get()) == 0:
                    messagebox.showinfo(title="Oops", message="some  entries are empty")
                    break

        # if type(lvl1) != int:
        #     messagebox.showinfo(title="Oops", message="Please make sure you entered integer.")
        # else:
        #     lvl1 = lvl1_entry.get()
        #     print(lvl1)

    save_button = Button(text="save", width=10, command=save)
    save_button.grid(row=14, column=5)

    def main_window():
        ui_setup.new_window()
        ui_setup.main_window()
        ui_setup.windows.mainloop()

    save_button = Button(text="MAIN", width=10, command=main_window)
    save_button.grid(row=14, column=6)

    ui_setup.windows.mainloop()


def report():
    with open("data/data.csv", "r") as data_file:
        my_data = pd.read_csv(data_file)
        print("will report soon")
        print(my_data.head())
        classification = my_data["Result"]
        le = preprocessing.LabelEncoder()
        le.fit(classification)
        print("Classes found:", le.classes_)
        # Convert classes to integers for use with ML
        int_classes = le.transform(classification)
        print("\nClasses converted to integers :", int_classes)
        my_data["classes"] = int_classes
        my_data.info
        my_data.head()

        my_data.Name.isnull().sum()
        my_data.Name.isnull().values.any()
        my_data[my_data.isna().any(axis=1)]
        my_data['Name'] = my_data['Name'].fillna("Unknown")
        my_data.Name.isnull().values.any()

        ax = my_data.Subject.value_counts().plot(kind='bar', figsize=(12, 8))
        ax.set_xlabel("Subject")
        ax.set_ylabel("Total Number of Solved questions by All")
        plt.show()
        sns.countplot(x='Subject', data=my_data, hue='Name')
        plt.show()
        ax=my_data.Subject.value_counts().plot(kind='pie')
        ax.set_xlabel("subjects solved by All")
        plt.show()
        ax = my_data.Date.value_counts().sort_index().plot(figsize=(12, 8))
        ax.set_xlabel("Dates m/d/y")
        ax.set_ylabel("Total Number of Solved questions by all")
        plt.show()

        ax=my_data["Result"].value_counts().plot(kind='pie')
        ax.set_xlabel("Total Result bu All")
        plt.show()

        names = my_data.Name.unique()
        print(names)

        for name in names:
            fig, ax = plt.subplots(1, figsize=(6, 4))
            my_data[my_data.Name == name].Date.value_counts().sort_index().plot(title=name)
            ax.set_xlabel("Dates m/d/y")
            ax.set_ylabel("Total Number of Solved questions")
        plt.show()

        # plt.pie(values, labels=labels, autopct='%.2f')

        for name in names:
            fig, ax = plt.subplots(1, figsize=(6, 4))
            my_data[my_data.Name == name].Subject.value_counts().plot(kind="pie", title=name,

                                                                      autopct='%.2f')
        plt.show()

        wrong_results = my_data[my_data["Result"] == "wrong"]
        ax = wrong_results.Name.value_counts().plot(kind="bar", title='Wrong results')
        ax.set_xlabel("Names")
        ax.set_ylabel("Total Number of wrong questions")
        plt.show()


        names = wrong_results.Name.unique()
        print(names)
        for name in names:
            fig, ax = plt.subplots(1, figsize=(6, 4))

            wrong_results[wrong_results.Name == name].Subject.value_counts().plot(kind="bar", title=name)
            ax.set_ylabel("Total Number of wrong questions")
            ax.set_xlabel("Subject")
        plt.show()

# report()
# root.mainloop()
