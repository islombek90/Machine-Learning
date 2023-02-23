from tkinter import *

import pygame

import constants
import fruits
import math_window
import letter
import colors
import my_data_analysis
import entertaiment
import tkinter.font as font
import datetime as dt
import math
from PIL import ImageTk, Image

from pygame import mixer
import shapes
import vegetables

# ---------------------------- UI SETUP ------------------------------- #

WIDTH = 1024
HEIGHT = 610
windows = Tk()
windows.title("Mini games for kids V1.0 2022")
windows.geometry(f'{WIDTH}x{HEIGHT}')
windows.resizable(0, 0)
windows.config( bg="cyan")


windows.iconbitmap("data/education_school_blocks_building_study_learn_numbers_icon_133453.ico")

bg_image = Image.open("data/ytD8s2.jpg")
resized_bg_image = bg_image.resize((WIDTH,HEIGHT), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(resized_bg_image)

math_bg_image = Image.open("data/E18N40.jpg")
resized_bg_image_math = math_bg_image.resize((WIDTH,HEIGHT), Image.ANTIALIAS)
math_background_image = ImageTk.PhotoImage(resized_bg_image_math)


def open_image_and_resize(image_path):
    image = Image.open(image_path)
    resized_image = image.resize((WIDTH,HEIGHT), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(resized_image)
    return background_image

count_background_image = open_image_and_resize("data/F6Lkj5.png")
lang_select_bg_image = open_image_and_resize("data/Nd8HOI.jpg")
colors_bg_image = open_image_and_resize("data/AwlbPc.jpg")
add_sub_bg_image = open_image_and_resize("data/F6Lkj5.png")
letters_bg_image = open_image_and_resize("data/KVHMBy.jpg")
games_bg_image = open_image_and_resize("data/D2fo4O.jpg")
animals_bg_image = open_image_and_resize("data/bg_image.jpg")
vegetables_bg_image = open_image_and_resize("data/peter_pan.png")


# # configure the grid
# windows.columnconfigure(0, weight=1)
# windows.columnconfigure(1, weight=2)



myFont = font.Font(family='Times', size='30')
myFont2 = font.Font(family='Helvetica', size='30')

math_button_photo = PhotoImage(file =r"data/math.png")
abc_button_photo = PhotoImage(file =r"data/abc.png")
colors_button_photo = PhotoImage(file =r"data/colors.png")
others_button_photo = PhotoImage(file =r"data/others.png")
games_button_photo = PhotoImage(file =r"data/game.png")


home_button_photo = PhotoImage(file =r"data/home.png")
next_button_photo = PhotoImage(file =r"data/next.png")
previous_button_photo = PhotoImage(file =r"data/previous.png")
sound_button_photo = PhotoImage(file =r"data/sound.png")
mic_button_photo = PhotoImage(file =r"data/mic_button.png")


gta_button_photo = PhotoImage(file =r"data/gta.png")
pacman_button_photo = PhotoImage(file =r"Pacman/player.png")
youtube_button_photo = PhotoImage(file =r"data/youtube.png")
scratch_button_photo = PhotoImage(file =r"data/scratch.png")
code_lab_button_photo = PhotoImage(file =r"data/codelab.png")
mblock_button_photo = PhotoImage(file =r"data/mblock.png")


eng_flag_button_photo = PhotoImage(file=r"data/eng_flag.png")
tr_flag_button_photo = PhotoImage(file=r"data/tr_flag.png")
ru_flag_button_photo = PhotoImage(file=r"data/ru_flag.png")
de_flag_button_photo = PhotoImage(file=r"data/de_flag.png")
uz_flag_button_photo = PhotoImage(file=r"data/uz_flag.png")


numbers_button_photo = PhotoImage(file=r"data/numbers.png")
addition_button_photo = PhotoImage(file=r"data/addition.png")
subtraction_button_photo = PhotoImage(file=r"data/subtraction.png")


arrow_image = PhotoImage(file="data/shapes/Arrow.png")
circle_image = PhotoImage(file="data/shapes/Circle.png")
heart_image = PhotoImage(file="data/shapes/Heart.png")
hexagon_image = PhotoImage(file="data/shapes/Hexagon.png")
oval_image = PhotoImage(file="data/shapes/Oval.png")
parallelogram_image = PhotoImage(file="data/shapes/Parallelogram.png")
pentagon_image = PhotoImage(file="data/shapes/Pentagon.png")
rectangle_image = PhotoImage(file="data/shapes/Rectangle.png")
rhombus_image = PhotoImage(file="data/shapes/Rhombus.png")
right_triangle_image = PhotoImage(file="data/shapes/Right Triangle.png")
square_image = PhotoImage(file="data/shapes/Square.png")
star_image = PhotoImage(file="data/shapes/Star.png")
trapezoid_image = PhotoImage(file="data/shapes/Trapezoid.png")
triangle_image = PhotoImage(file="data/shapes/Triangle.png")

shape_list_photo = [arrow_image, circle_image,heart_image,hexagon_image,oval_image,parallelogram_image,pentagon_image,
              rectangle_image, rhombus_image,right_triangle_image,square_image,star_image,trapezoid_image,triangle_image]
my_shapes = shapes.Shapes()


Apple_image = PhotoImage(file="data/fruits/apple-min.png")
Apricot_image = PhotoImage(file="data/fruits/Apricot-min.png")
Avocado_image = PhotoImage(file="data/fruits/Avocado-min.png")
Banana_image = PhotoImage(file="data/fruits/banana-min.png")
Blackberry_image = PhotoImage(file="data/fruits/Blackberry-min.png")
Blueberry_image = PhotoImage(file="data/fruits/Blueberry-min.png")
Cherry_image = PhotoImage(file="data/fruits/Cherry-min.png")
Coconut_image = PhotoImage(file="data/fruits/Coconut-min.png")
Fig_image = PhotoImage(file="data/fruits/Fig-min.png")
Grapes_image = PhotoImage(file="data/fruits/grapes-min.png")
Kiwifruit_image = PhotoImage(file="data/fruits/Kiwifruit-min.png")
Lime_image = PhotoImage(file="data/fruits/Lime-min.png")
Mango_image = PhotoImage(file="data/fruits/mango-min.png")
MuskMelon_image = PhotoImage(file="data/fruits/MuskMelon-min.png")
Olives_image = PhotoImage(file="data/fruits/Olives-min.png")
Orange_image = PhotoImage(file="data/fruits/orange-min.png")
Papaya_image = PhotoImage(file="data/fruits/papaya-min.png")
Peach_image = PhotoImage(file="data/fruits/Peach-min.png")
Pear_image = PhotoImage(file="data/fruits/Pear-min.png")
Pineapple_image = PhotoImage(file="data/fruits/Pineapple-min.png")
Pomegranate_image = PhotoImage(file="data/fruits/Pomegranate-min.png")
Strawberry_image = PhotoImage(file="data/fruits/Strawberry-min.png")
Watermelon_image = PhotoImage(file="data/fruits/Watermelon-min.png")

fruits_list_photo =[Apple_image, Avocado_image, Avocado_image, Banana_image, Blueberry_image,Blackberry_image,
                    Cherry_image,Coconut_image,Fig_image,Grapes_image,Kiwifruit_image,Lime_image,Mango_image,
                    MuskMelon_image,Olives_image,Orange_image,Papaya_image, Peach_image, Pear_image,
                    Pineapple_image, Pomegranate_image, Strawberry_image, Watermelon_image]
my_fruits = fruits.Fruits()
fruit_image = Image.open("data/fruits/apple-min.png")
resized_image_fruit = fruit_image.resize((100, 100), Image.ANTIALIAS)
fruit_button_image = ImageTk.PhotoImage(resized_image_fruit)


Broccoli_image = PhotoImage(file="data/vegetables/broccoli-min.png")
Cabbage_image = PhotoImage(file="data/vegetables/cabbage-min.png")
Carrot_image = PhotoImage(file="data/vegetables/carrot-min.png")
Cauliflower_image = PhotoImage(file="data/vegetables/cauliflower-min.png")
Corn_image = PhotoImage(file="data/vegetables/corn-min.png")
chili_image = PhotoImage(file="data/vegetables/chilli-min.png")
coriander_image = PhotoImage(file="data/vegetables/coriander-min.png")
Cucumber_image = PhotoImage(file="data/vegetables/cucumber-min.png")
Garlic_image = PhotoImage(file="data/vegetables/garlic-min.png")
Green_beans_image = PhotoImage(file="data/vegetables/green-bean-min.png")
Leek_image = PhotoImage(file="data/vegetables/leek-min.png")
Mushroom_image = PhotoImage(file="data/vegetables/mushroom-min.png")
Onion_image = PhotoImage(file="data/vegetables/onion-min.png")
Potato_image = PhotoImage(file="data/vegetables/potato-min.png")
Pumpkin_image = PhotoImage(file="data/vegetables/pumpkin-min.png")
Radish_image = PhotoImage(file="data/vegetables/radish-min.png")
Spinach_image = PhotoImage(file="data/vegetables/spinach-min.png")
Tomato_image = PhotoImage(file="data/vegetables/tomato-min.png")
turnip = PhotoImage(file="data/vegetables/Turnip-min.png")
Zucchini_image = PhotoImage(file="data/vegetables/zucchini-min.png")

vegetables_list_photo = [Broccoli_image,Cabbage_image,Carrot_image,Cauliflower_image,Corn_image,chili_image,
                         coriander_image,Cucumber_image,Garlic_image,Green_beans_image,Leek_image,Mushroom_image,
                         Onion_image, Potato_image, Pumpkin_image, Radish_image, Spinach_image,
                         Tomato_image, turnip, Zucchini_image]

my_vegetables = vegetables.Vegetables()
vegetable_image = Image.open("data/vegetables/broccoli-min.png")
resized_image_vegetable = vegetable_image.resize((100, 100), Image.ANTIALIAS)
vegetable_button_image = ImageTk.PhotoImage(resized_image_vegetable)


Bat_image = PhotoImage(file="data/animals/birds/Bat-min.png")
Chick_image = PhotoImage(file="data/animals/birds/Chick-min.png")
Cock_image = PhotoImage(file="data/animals/birds/Cock-min.png")
Crow_image = PhotoImage(file="data/animals/birds/Crow.png")
Duckling_image = PhotoImage(file="data/animals/birds/Duckling-min.png")
Duck_image = PhotoImage(file="data/animals/birds/Duck-min.png")
Eagle_image = PhotoImage(file="data/animals/birds/eagle-min.png")
Flamingo_image = PhotoImage(file="data/animals/birds/Flamingo-min.png")
Hen_image = PhotoImage(file="data/animals/birds/Hen-min.png")
Ostrich_image = PhotoImage(file="data/animals/birds/Ostrich-min.png")
Owl_image = PhotoImage(file="data/animals/birds/Owl-min.png")
Parrot_image = PhotoImage(file="data/animals/birds/Parrot-min.png")
Peacock_image = PhotoImage(file="data/animals/birds/Peacock-min.png")
Penguin_image = PhotoImage(file="data/animals/birds/Penguin-min.png")
Pigeon_image = PhotoImage(file="data/animals/birds/Pigeon-min.png")
Rooster_image = PhotoImage(file="data/animals/birds/Rooster-min.png")
Sparrow_image = PhotoImage(file="data/animals/birds/Sparrow-min.png")
Swan_image = PhotoImage(file="data/animals/birds/Swan-min.png")
Turkey_image = PhotoImage(file="data/animals/birds/Turkey-min.png")
Woodpecker_image = PhotoImage(file="data/animals/birds/Woodpecker-min.png")

birds_list_photo = [Bat_image,Chick_image,Cock_image,Crow_image,Duckling_image,Duck_image,Eagle_image,Flamingo_image,
                    Hen_image,Ostrich_image,Owl_image,Parrot_image,Peacock_image, Penguin_image, Pigeon_image,
                    Rooster_image, Sparrow_image,Swan_image,Turkey_image,Woodpecker_image]



Buffalo_image = PhotoImage(file="data/animals/domestic_animals/Buffalo-min.png")
Camel_image = PhotoImage(file="data/animals/domestic_animals/camel-min.png")
Chicken_image = PhotoImage(file="data/animals/domestic_animals/Chicken-min.png")
Cow_image = PhotoImage(file="data/animals/domestic_animals/cow-min.png")
Donkey_image = PhotoImage(file="data/animals/domestic_animals/Duck-min.png")
Duck_image = PhotoImage(file="data/animals/domestic_animals/Duck-min.png")
Fish_image = PhotoImage(file="data/animals/domestic_animals/fish-min.png")
Goat_image = PhotoImage(file="data/animals/domestic_animals/Goat-min.png")
Honeybee_image = PhotoImage(file="data/animals/domestic_animals/Honeybee-min.png")
Horse_image = PhotoImage(file="data/animals/domestic_animals/Horse-min.png")
Pig_image = PhotoImage(file="data/animals/domestic_animals/Pig-min.png")
Rabbit_image = PhotoImage(file="data/animals/domestic_animals/Rabbit-min.png")
Rooster_image = PhotoImage(file="data/animals/domestic_animals/Rooster-min.png")
Sheep_image = PhotoImage(file="data/animals/domestic_animals/Sheep-min.png")
Turkey_image = PhotoImage(file="data/animals/domestic_animals/Turkey-min.png")
Yak_image = PhotoImage(file="data/animals/domestic_animals/Yak-min.png")

domestic_animal_photo = [Buffalo_image,Camel_image,Chicken_image,Cow_image,Donkey_image,Duck_image,Fish_image,
                         Goat_image, Honeybee_image,Horse_image, Pig_image, Rabbit_image, Rooster_image, Sheep_image,
                         Turkey_image, Yak_image]


Ant_image = PhotoImage(file="data/animals/insects/Ant-min.png")
Beetle_image = PhotoImage(file="data/animals/insects/Beetle-min.png")
Bumblebee_image = PhotoImage(file="data/animals/insects/bumblebee-min.png")
Butterfly_image = PhotoImage(file="data/animals/insects/Butterfly-min.png")
Caterpillar_image = PhotoImage(file="data/animals/insects/Caterpillar-min.png")
Cockroach_image = PhotoImage(file="data/animals/insects/Cockroach-min.png")
Cricket_image = PhotoImage(file="data/animals/insects/Cricket-min.png")
Dragonfly_image = PhotoImage(file="data/animals/insects/dragonfly-min.png")
Firefly_image = PhotoImage(file="data/animals/insects/fireflies-min.png")
Fly_image = PhotoImage(file="data/animals/insects/fly-min.png")
Grasshopper_image = PhotoImage(file="data/animals/insects/Grasshopper-min.png")
Honeybee_image = PhotoImage(file="data/animals/insects/Honeybee-min.png")
Mosquito_image = PhotoImage(file="data/animals/insects/Mosquito-min.png")
Red_bug_image = PhotoImage(file="data/animals/insects/red-bug-min-1.png")
Scorpion_image = PhotoImage(file="data/animals/insects/Scorpion-min.png")
Silkworm_image = PhotoImage(file="data/animals/insects/silkworms-min.png")
Spider_image = PhotoImage(file="data/animals/insects/Spider-min.png")
Wasp_image = PhotoImage(file="data/animals/insects/wasp-min.png")

insects_animal_photo = [Ant_image,Beetle_image,Bumblebee_image,Butterfly_image,Caterpillar_image,Cockroach_image,
                        Cricket_image, Dragonfly_image,Firefly_image,Fly_image,Grasshopper_image,Honeybee_image,
                        Mosquito_image,Red_bug_image,Scorpion_image,Silkworm_image,Spider_image,Wasp_image]


Cat_image = PhotoImage(file="data/animals/pet_animals/cat-min.png")
Chameleon_image = PhotoImage(file="data/animals/pet_animals/Chameleon-min.png")
Dog_image = PhotoImage(file="data/animals/pet_animals/dog-min (1).png")
Fish_image = PhotoImage(file="data/animals/pet_animals/fish-min.png")
Hamster_image = PhotoImage(file="data/animals/pet_animals/Hamster-min.png")
Mouse_image = PhotoImage(file="data/animals/pet_animals/mouse-min.png")
Parrot_image = PhotoImage(file="data/animals/pet_animals/Parrot-1-min.png")
Pigeon_image = PhotoImage(file="data/animals/pet_animals/Pigeon-1-min.png")
Pig_image = PhotoImage(file="data/animals/pet_animals/Pig-min.png")
Rabbit_image = PhotoImage(file="data/animals/pet_animals/Rabbit-min.png")
Snake_image = PhotoImage(file="data/animals/pet_animals/Snake-min.png")
Turtle_image = PhotoImage(file="data/animals/pet_animals/turtle-min.png")

pet_animal_photo = [Cat_image, Chameleon_image, Dog_image, Fish_image, Hamster_image, Mouse_image, Parrot_image,
                    Pigeon_image, Pig_image, Rabbit_image, Snake_image, Turtle_image]


Bat_image = PhotoImage(file="data/animals/mamals/Bat-min.png")
Bear_image = PhotoImage(file="data/animals/mamals/Bear-min.png")
Blue_Whale_image = PhotoImage(file="data/animals/mamals/blue-whale-min.png")
Cat_image = PhotoImage(file="data/animals/mamals/cat-min.png")
Cow_image = PhotoImage(file="data/animals/mamals/cow-min.png")
Dog_image = PhotoImage(file="data/animals/mamals/dog-min.png")
Dolphin_image = PhotoImage(file="data/animals/mamals/dolphin-min.png")
Donkey_image = PhotoImage(file="data/animals/mamals/donkey-min.png")
Elephant_image = PhotoImage(file="data/animals/mamals/Elephant-min.png")
Fox_image = PhotoImage(file="data/animals/mamals/Fox-min.png")
Giraffe_image = PhotoImage(file="data/animals/mamals/Giraffe-min.png")
Gorilla_image = PhotoImage(file="data/animals/mamals/Gorilla-min.png")
Horse_image = PhotoImage(file="data/animals/mamals/Horse-min.png")
Kangaroo_image = PhotoImage(file="data/animals/mamals/Kangaroo-min.png")
Leopard_image = PhotoImage(file="data/animals/mamals/leapord-min.png")
Lion_image = PhotoImage(file="data/animals/mamals/lion-min.png")
Monkey_image = PhotoImage(file="data/animals/mamals/Monkey-min.png")
Panda_image = PhotoImage(file="data/animals/mamals/Panda-min.png")
Reindeer_image = PhotoImage(file="data/animals/mamals/Reindeer-min.png")
Tiger_image = PhotoImage(file="data/animals/mamals/Tiger-min.png")
Wolf_image = PhotoImage(file="data/animals/mamals/Wolf-min.png")

mammal_animal_photo = [Bat_image, Bear_image, Blue_Whale_image, Cat_image, Cow_image, Donkey_image, Dolphin_image,
                       Donkey_image, Elephant_image, Fox_image, Gorilla_image, Gorilla_image, Horse_image,
                       Kangaroo_image, Leopard_image, Lion_image, Monkey_image, Panda_image, Reindeer_image,
                       Tiger_image, Wolf_image]


Blue_whale_image = PhotoImage(file="data/animals/sea_animals/blue-whale-min.png")
Catfish_image = PhotoImage(file="data/animals/sea_animals/Catfish-min.png")
Crab_image = PhotoImage(file="data/animals/sea_animals/Crab-min.png")
Dolphin_image = PhotoImage(file="data/animals/sea_animals/dolphin-min.png")
Eels_image = PhotoImage(file="data/animals/sea_animals/eels-min.png")
Goldfish_image = PhotoImage(file="data/animals/sea_animals/Goldfish-min.png")
Jellyfish_image = PhotoImage(file="data/animals/sea_animals/Jellyfish-min.png")
Oyster_image = PhotoImage(file="data/animals/sea_animals/Oyster-min.png")
Penguin_image = PhotoImage(file="data/animals/sea_animals/Penguin-min.png")
Piranha_image = PhotoImage(file="data/animals/sea_animals/Piranha-min.png")
Prawns_image = PhotoImage(file="data/animals/sea_animals/Prawns-min.png")
Salmon_image = PhotoImage(file="data/animals/sea_animals/Salmon-min.png")
Sea_horse_image = PhotoImage(file="data/animals/sea_animals/Sea-horse-min.png")
Sea_lion_image = PhotoImage(file="data/animals/sea_animals/Sealion-min.png")
Seal_image = PhotoImage(file="data/animals/sea_animals/seal-min.png")
Shark_image = PhotoImage(file="data/animals/sea_animals/shark-min.png")
Tuna_image = PhotoImage(file="data/animals/sea_animals/Tuna-min.png")


sea_animal_photo = [Blue_whale_image, Catfish_image, Crab_image, Dolphin_image, Eels_image, Goldfish_image,
                    Jellyfish_image, Oyster_image, Penguin_image, Piranha_image, Prawns_image, Salmon_image,
                    Sea_horse_image, Sea_lion_image, Seal_image, Shark_image, Tuna_image]


Lion_image = PhotoImage(file="data/animals/wild_animals/lion-min.png")
Tiger_image = PhotoImage(file="data/animals/wild_animals/Tiger-min.png")
Elephant_image = PhotoImage(file="data/animals/wild_animals/Elephant-min.png")
Giraffe_image = PhotoImage(file="data/animals/wild_animals/Giraffe-min.png")
Bear_image = PhotoImage(file="data/animals/wild_animals/Bear-min.png")
Zebra_image = PhotoImage(file="data/animals/wild_animals/Zebra-min.png")
Panda_image = PhotoImage(file="data/animals/wild_animals/Panda-min.png")
Gorilla_image = PhotoImage(file="data/animals/wild_animals/Gorilla-min.png")
Monkey_image = PhotoImage(file="data/animals/wild_animals/Monkey-min.png")
Wolf_image = PhotoImage(file="data/animals/wild_animals/Wolf-min.png")
Kangaroo_image = PhotoImage(file="data/animals/wild_animals/Kangaroo-min.png")
Hippopotamus_image = PhotoImage(file="data/animals/wild_animals/Hippopotamus-min.png")
Deer_image = PhotoImage(file="data/animals/wild_animals/Deer-min.png")
Fox_image = PhotoImage(file="data/animals/wild_animals/Fox-min.png")
Koala_image = PhotoImage(file="data/animals/wild_animals/Koala-min.png")
Yak_image = PhotoImage(file="data/animals/wild_animals/Yak-min.png")
Chimpanzee_image = PhotoImage(file="data/animals/wild_animals/Chimpanzee-min.png")
Antelope_image = PhotoImage(file="data/animals/wild_animals/Antelope-min.png")
Squirrel_image = PhotoImage(file="data/animals/wild_animals/Squirrel-min.png")
Mole_image = PhotoImage(file="data/animals/wild_animals/Mole-min.png")
Reindeer_image = PhotoImage(file="data/animals/wild_animals/Reindeer-min.png")
Jaguar_image = PhotoImage(file="data/animals/wild_animals/Jaguar-min.png")
Jackal_image = PhotoImage(file="data/animals/wild_animals/Jackal-min.png")
Possum_image = PhotoImage(file="data/animals/wild_animals/Possum-min.png")
Rhinoceros_image = PhotoImage(file="data/animals/wild_animals/Rhinoceros-min.png")
Cougar_image = PhotoImage(file="data/animals/wild_animals/Cougar-min.png")
Hyena_image = PhotoImage(file="data/animals/wild_animals/Hyena-min.png")
Chipmunk_image = PhotoImage(file="data/animals/wild_animals/Chipmunk-min.png")
Wombat_image = PhotoImage(file="data/animals/wild_animals/Wombat-min.png")

wild_animal_photo = [Lion_image, Tiger_image, Elephant_image, Giraffe_image, Bear_image, Zebra_image, Panda_image,
                     Gorilla_image, Monkey_image, Wolf_image, Kangaroo_image, Hippopotamus_image, Deer_image, Fox_image,
                     Koala_image, Yak_image, Chimpanzee_image, Antelope_image, Squirrel_image, Mole_image,
                     Reindeer_image, Jaguar_image, Jackal_image, Possum_image, Rhinoceros_image, Cougar_image,
                     Hyena_image, Chipmunk_image, Wombat_image]


mixer.init()

def play_music(path, loop_numb):
    mixer.music.load(path)
    mixer.music.play(loops=loop_numb)
def stop_music():
    mixer.music.stop()

def volume_toggle():
    volume = mixer.music.get_volume()
    # print(volume)
    if volume == 0.0:
        mixer.music.set_volume(1.0)
    elif volume >= 0:
        mixer.music.set_volume(0)


def correct_answer_sound_effect():
    mixer.music.load("data/owin31.wav")
    mixer.music.play()


def wrong_answer_sound_effect():
    mixer.music.load("data/wah-wah-sad-trombone-6347.mp3")
    mixer.music.play()


def new_window():
    for widget in windows.winfo_children():
        widget.destroy()
        windows.after(10)


import animals

# ---------------------------- CLOCK SETUP ------------------------------- #
def my_clock():
    time_format = dt.datetime.now().strftime("%Y/%m/%D \n Time: %H:%M:%S")
    canvas = Canvas(width=200, height=100, highlightthickness=0, bg='yellow')
    canvas.create_text(100, 50, text=time_format, width=250, font=("Arial", 15, "bold"),
                       fill="black")
    canvas.grid(column=0, row=0)
    windows.after(100, my_clock)


def main_window():
    pygame.init()
    new_window()
    play_music("data/POL-hide-and-seek-preview.mp3", -1)

    my_label = Label(image=background_image)
    my_label.place(x=0, y=0, relheight=1, relwidth=1)

    if constants.name == "Samira":
        math_button_state = DISABLED
        lang_button_state = DISABLED
        other_button_sate = NORMAL
        fruit_button_state = NORMAL
        vegetable_button_sate = NORMAL
    else:
        math_button_state = NORMAL
        lang_button_state = NORMAL
        other_button_sate = NORMAL
        fruit_button_state = NORMAL
        vegetable_button_sate = NORMAL

    math_button = Button(text="123", width=350, height=100, bg="white", image=math_button_photo, font=myFont,
                         state=math_button_state,command=math_window.math)
    math_button.grid(column=1, row=3, padx=20,pady=0)
    #
    lang_button = Button(text="ABC", width=350, height=100, bg="white", image=abc_button_photo, font=myFont,
                         state=lang_button_state, command=letter.lang)
    lang_button.grid(column=1, row=4, pady=2)

    colors_button = Button(text="colors", width=350, height=100, bg="white", image=colors_button_photo, font=myFont, command=colors.color)
    colors_button.grid(column=1, row=5, pady=2)

    other_button = Button(text="........", width=350, height=100,  bg="white",image=others_button_photo, state=other_button_sate,
                          font=myFont, command=my_shapes.shapes_lang_selec)
    other_button.grid(column=1, row=6,pady=2)

    games_button = Button(text="Entertainment", width=350, height=100, bg="white", image=games_button_photo,
                          font=myFont, command=entertaiment.entertaiment)
    games_button.grid(column=1, row=7, pady=2)

    fruits_button = Button(text="........", width=350, height=100, bg="white", image=fruit_button_image, state=fruit_button_state,
                           font=myFont, command=my_fruits.fruits_lang_selec)
    fruits_button.grid(column=2, row=3, pady=2)

    vegetables_button = Button(text="........", width=350, height=100, bg="white", image=vegetable_button_image,
                               state=vegetable_button_sate, font=myFont,
                               command=my_vegetables.vegetables_lang_selec)
    vegetables_button.grid(column=2, row=4, pady=2)

    animals_button = Button(text="Animals", width=350, height=100, bg="white", image=Lion_image,
                               state=vegetable_button_sate, font=myFont,
                               command=animals.animal_types_selection)
    animals_button.grid(column=2, row=5, pady=2)

    vol_button = Button(text="Volume", width=100, height=100, image=sound_button_photo, bg='white',
                            command=volume_toggle)
    vol_button.grid(column=3, row=3, sticky=E)

    report_button = Button(text="Report", bg='white',
                        command= lambda : my_data_analysis.developper_widow())
    report_button.grid(column=1, row=10)

    name_label = Label(text=f"Hello {constants.name}",font=myFont2, bg="whitesmoke", fg="black")
    name_label.grid(column=3, row=10, sticky=W)

    # clock
    # threading.Thread(target=my_clock).start()


def update_point():
    canvas2 = Canvas(width=100, height=100, bg='white')

    point_text = canvas2.create_text(50, 50, text=f"{constants.point}", width=100, font=("Arial", 35, "bold"),
                                     fill="black")
    canvas2.grid(column=1, row=0, pady=10,sticky=N)
    canvas2.itemconfig(point_text, text=constants.point)


def countdown(counter):
    count_min = math.floor(counter / 60)
    count_sec = counter % 60
    # change text in label
    canvas3 = Canvas(width=100,height=50,highlightthickness=0, bg="yellow")
    timer_text = canvas3.create_text(50,25, text=counter, fill="black", font=("Arial",25,"bold" ))
    canvas3.grid(column=3,row=0)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if counter > 0:
        # call countdown again after 1000ms (1s)
        windows.after(1000, countdown, counter-1)
        canvas3.itemconfig(timer_text, text=f"{count_min}:{count_sec}")


# call countdown first time
# root.after(0, countdown, 5)












