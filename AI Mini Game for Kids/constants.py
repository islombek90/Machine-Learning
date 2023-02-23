


point = 0
mic_text = ""
name = "Unknown"

LEVEL1_SCORE = 50
LEVEL2_SCORE = 100
LEVEL3_SCORE = 200
TURKISH_POINT = 1
ENGLISH_POINT = 2
RUSSIAN_POINT = 3
GERMAN_POINT = 4
ADDITION_POINT = 2
SUBTRACTION_POINT = 3

daily_plan = ['wake up', 'brush your teeth', 'breakfast', 'study', 'do sport', 'lunch time ', 'play game',
              'dinner time', 'brush your teeth', 'got to sleep']

# ---------------------------- LETTERS LISTS ------------------------------- #
letters_Eng = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k',
               'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v',
               'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
letters_Eng_capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters_Eng_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
letters_Eng_list = [letters_Eng_capital,letters_Eng_small]

letter_Uz = ['А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж',
             'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
             'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц',
             'Ч', 'ч', 'Ш', 'ш', "Щ","щ", 'Ъ', 'ъ', 'Ь', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я', 'Ў', 'ў',
             'Қ', 'қ', 'Ғ', 'ғ', 'Ҳ', 'ҳ']

letter_Uz_capital = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                     'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь', 'Э', 'Ю', 'Я', 'Ў', 'Қ', 'Ғ', 'Ҳ']
letter_Uz_small= ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                  'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'э', 'ю', 'я', 'ў', 'қ', 'ғ', 'ҳ']
letter_Uz_list = [letter_Uz_capital,letter_Uz_small]


letter_ru = ['А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё', 'Ж', 'ж',
             'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
             'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц',
             'Ч', 'ч', 'Ш', 'ш', "Щ","щ", 'Ъ', 'ъ', 'Ь', 'ь', 'Э', 'э', 'Ю', 'ю', 'Я', 'я'
             ]

letter_ru_capital= ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                    'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ь', 'Э', 'Ю', 'Я']
letter_ru_small = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                   'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ь', 'э', 'ю', 'я']
letter_ru_list = [letter_ru_small,letter_ru_capital]

letters_de = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i',
              'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r',
              'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', 'Ä', 'ä',
              'Ö', 'ö', 'Ü', 'ü', 'ẞ', 'ß']

letters_de_capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                      'U', 'V', 'W', 'X', 'Y', 'Z', 'Ä', 'Ö', 'Ü', 'ẞ']
letters_de_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü', 'ß']
letters_de_list = [letters_de_capital,letters_de_small]

letters_tr = ['A', 'a', 'B', 'b', 'C', 'c', 'Ç', 'ç', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g',
              'Ğ', 'ğ', 'H', 'h', 'İ', 'i', 'I', 'ı', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm',
              'N', 'n', 'O', 'o', 'Ö', 'ö', 'P', 'p', 'R', 'r', 'S', 's', 'Ş', 'ş', 'T', 't',
              'U', 'u', 'Ü', 'ü', 'V', 'v', 'Y', 'y', 'Z', 'z']

letters_tr_capital = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'İ', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
                     'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']
letters_tr_small = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'i', 'ı', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p',
                    'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
letters_tr_list = [letters_tr_capital,letters_tr_small]



# ---------------------------- COLORS LIST ------------------------------- #
color_list_eng = ["black", "gray", "white", "brown", "red", "purple", "green", "yellow", "blue"]
color_list_uz = ["qora", "kulrang", "oq", "jigarrang", "qizil", "binafsha", "yashil", "sariq", "ko'k"]
color_list_ru = ["черный", "серый", "белый", "коричневый", "красный", "фиолетовый", "зеленый", "желтый", "синий"]
color_list_tr = ["siyah", "gri", "beyaz", "kahverengi", "kırmızı", "mor", "yeşil", "sarı", "mavi"]
color_list_de = ["schwarz", "grau", "weiß", "braun", "rot", "lila", "grün", "gelb", "blau"]

# ---------------------------- FRUITS LIST ------------------------------- #

fruits_list_eng =["Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry", "Cherry", "Coconut",   "Fig", "Grapes",  "Kiwifruit", "Lime",
                   "Mango","MuskMelon", "Olives", "Orange", "Papaya", "Peach", "Pear", "Pineapple", "Pomegranate", "Strawberry",
                    "Watermelon"]
fruits_list_ru = ["Яблоко", "Абрикос", "Авокадо", "Банан", "Ежевика", "Черника", "Вишня", "Кокос", "Инжир", "Виноград", "Киви", "Лайм",
                    "Манго", "Мускусная дыня", "Оливки", "Апельсин", "Папайя", "Персик", "Груша", "Ананас", "Гранат", "Клубника",
                     "Арбуз"]

fruits_list_tr = ["Elma", "Kayısı", "Avokado", "Muz", "Böğürtlen", "Yabanmersini", "Kiraz", "Hindistan Cevizi", "İncir", "Üzüm", "Kivi", "Lime",
                    "Mango", "MiskKavun", "Zeytin", "Portakal", "Papaya", "Şeftali", "Armut", "Ananas", "Nar", "Çilek",
                     "Karpuz"]

fruits_list_de = ["Apfel", "Aprikose", "Avocado", "Banane", "Brombeere", "Heidelbeere", "Kirsche", "Kokosnuss", "Feige", "Trauben", "Kiwifrucht", "Limette",
                    "Mango", "Moschusmelone", "Oliven", "Orange", "Papaya", "Pfirsich", "Birne", "Ananas", "Granatapfel", "Erdbeere",
                     "Wassermelone"]
fruits_list_uz = ["Olma", "O'rik", "Avokado", "Banan", "Blackberry", "Ko'k", "Gilos", "Kokos", "Anjir", "Uzum", "Kivi", "Ohak",
                    "Mango", "Muskqovun", "Zaytun", "Apelsin", "Papayya", "Shaftoli", "Nok", "Ananas", "Anor", "Qulupnay",
                     "Tarvuz"]

# ---------------------------- VEGETABLE LIST ------------------------------- #
vegetables_list_eng = ["Broccoli", "Cabbage", "Carrot", "Cauliflower" , "Corn", "Chili","Coriander", "Cucumber",
                        "Garlic", "Green beans",  "Leek",  "Mushroom", "Onion",
                        "Potato", "Pumpkin", "Radish", "Spinach", "Tomato", "Turnip", "Zucchini"]

vegetables_list_tr = ["Brokoli", "Lahana", "Havuç", "Karnabahar" , "Mısır", "Biber", "Kişniş", "Salatalık",
                         "Sarımsak", "Yeşil fasulye",  "Pırasa", "Mantar", "Soğan",
                         "Patates", "Kabak", "Turp", "Ispanak", "Domates", "Şalgam", "Kabak"]

vegetables_list_de = ["Brokkoli", "Kohl", "Karotte", "Blumenkohl", "Mais", "Chili", "Koriander", "Gurke",
                         "Knoblauch", "Grüne Bohnen", "Lauch", "Pilz", "Zwiebel",
                         "Kartoffel", "Kürbis", "Rettich", "Spinat", "Tomate", "Rübe", "Zucchini"]

vegetables_list_ru = ["Брокколи", "Капуста", "Морковь", "Цветная капуста", "Кукуруза", "Чили", "Кориандр", "Огурец",
                         "Чеснок", "Фасоль стручковая", "Лук порей", "Гриб", "Лук репчатый",
                         "Картофель", "Тыква", "Редис", "Шпинат", "Помидор", "Репа", "Кабачок"]

vegetables_list_uz = ["Brokkoli", "karam", "sabzi", "gulkaram", "makkajo'xori", "chili", "koriander", "bodring",
                         "Sarimsoq", "Yashil loviya","Piyoz", "Qo'ziqorin", "Piyoz",
                         "Kartoshka", "Qovoq", "Turp", "Imaloq", "Pomidor", "Sholg'om", "Qovoq"]
# ---------------------------- SHAPES LIST ------------------------------- #

shapes_list_eng = ["Arrow", "Circle", "Heart", "Hexagon", "Oval", "Parallelogram", "Pentagon", "Rectangle", "Rhombus",
                   "Right Triangle", "Square", "Star", "Trapezoid", "Triangle"]

shapes_list_tr = ["Ok", "Daire", "Kalp", "Altıgen", "Oval", "Paralelkenar", "Pentagon", "Dikdörtgen", "Eşkenar Dörtgen",
                  "Sağ Üçgen", "Kare", "Yıldız", "Yamuk", "Üçgen"]

shapes_list_ru = ["Стрелка", "Круг", "Сердце", "Шестиугольник", "Овал", "Параллелограмм", "Пятиугольник",
                  "Прямоугольник", "Ромб", "Прямоугольный треугольник", "Квадрат", "Звезда", "Трапеция", "Треугольник"]

shapes_list_de = ["Pfeil", "Kreis", "Herz", "Hexagon", "Oval", "Parallelogramm", "Pentagon", "Rechteck", "Rhombus",
                    "Rechtes Dreieck", "Quadrat", "Stern", "Trapez", "Dreieck"]

shapes_list_uz = ["O'q", "Doira", "Yurak", "Olti burchakli", "Oval", "Parallelogram", "Pentagon", "To'rtburchak", "Romb",
                    "To'g'ri uchburchak", "Kvadrat", "Yulduz", "Trapezoid", "Uchburchak"]


# ---------------------------- BIRDS LIST ------------------------------- #

birds_list_en = ["Bat", "Chick", "Cock", "Crow", "Duckling", "Duck", "Eagle", "Flamingo", "Hen", "Ostrich", "Owl",
                  "Parrot", "Peacock", "Penguin", "Pigeon", "Rooster", "Sparrow", "Swan", "Turkey", "Woodpecker"]

birds_list_tr = ["Yarasa", "Civciv", "Horoz", "Karga", "Ördek Yavrusu", "Ördek", "Kartal", "Flamingo", "Tavuk",
                 "Devekuşu", "Baykuş", "Papağan", "Tavus Kuşu", "Penguen", "Güvercin", "Horoz", "Serçe", "Kuğu",
                 "Hindi", "Ağaçkakan"]
birds_list_de = ["Fledermaus", "Küken", "Hahn", "Krähe", "Entlein", "Ente", "Adler", "Flamingo", "Henne", "Strauß",
                 "Eule", "Papagei", "Pfau", "Pinguin", "Taube", "Hahn", "Spatz", "Schwan", "Truthahn", "Specht"]
birds_list_ru = ["Летучая мышь", "Цыпленок", "Петух", "Ворона", "Утенок", "Утка", "Орел", "Фламинго", "Курочка",
                 "Страус", "Сова", "Попугай", "Павлин", "Пингвин", "Голубь", "Петух", "Воробей", "Лебедь", "Индюк",
                 "Дятел"]
birds_list_uz = ["Ko'rshapalaklar", "Jo'ja", "Xo'roz", "Qarga", "O'rdak", "O'rdak", "Burgut", "Flamingo", "Tovuq",
                 "Tuyaqush", "Boyo'g'li", "To'tiqush", "Tovus", "Pingvin", "Kabutar", "Xo'roz", "Chumchuq", "Oqqush",
                 "Kurka", "Tovuq"]

birds_list_dict = {"en": birds_list_en, "tr":birds_list_tr, "de": birds_list_de, "ru": birds_list_ru,
                   "uz": birds_list_uz}

# ---------------------------- DOMESTIC ANIMAL LIST ------------------------------- #
domestic_animal_list_en = ["Buffalo", "Camel", "Chicken", "Cow", "Donkey", "Duck", "Fish", "Goat", "Honey bee",
                            "Horse", "Pig", "Rabbit", "Rooster", "Sheep", "Turkey", "Yak"]
domestic_animal_list_tr = ["Bufalo", "Deve", "Tavuk", "İnek", "Eşek", "Ördek", "Balık", "Keçi", "Bal Arısı", "At",
                           "Domuz", "Tavşan", "Horoz", "Koyun", "Türkiye", "Yak"]
domestic_animal_list_de = ["Büffel", "Kamel", "Huhn", "Kuh", "Esel", "Ente", "Fisch", "Ziege", "Honigbiene", "Pferd",
                           "Schwein", "Kaninchen", "Hahn", "Schaf", "Truthahn", "Yak"]
domestic_animal_list_ru = ["Буйвол", "Верблюд", "Курица", "Корова", "Осел", "Утка", "Рыба", "Коза", "Медоносица",
                           "Лошадь", "Свинья", "Кролик", "Петух", "Овца", "Индюк", "Як"]
domestic_animal_list_uz = ["Buffalo", "Tuya", "Tovuq", "Sigir", "Eshak", "O'rdak", "Baliq", "Echki", "Asal ari", "Ot",
                           "To'ng'iz", "Quyon", "Xo'roz", "Qo'y", "Turkiya", "Yak"]

domestic_animal_list_dict = {"en":domestic_animal_list_en, "tr":domestic_animal_list_tr, "de":domestic_animal_list_de,
                             "ru":domestic_animal_list_ru, "uz": domestic_animal_list_uz}
# ---------------------------- INSECTS ANIMAL LIST ------------------------------- #
insects_animal_list_en =["Ant", "Beetle", "Bumblebee", "Butterfly", "Caterpillar", "Cockroach", "Cricket", "Dragonfly",
                         "Firefly", "Fly", "Grasshopper", "Honeybee", "Mosquito", "Red-bug", "Scorpion", "Silkworm",
                         "Spider", "Wasp"]
insects_animal_list_tr = ["Karınca", "Böcek", "Yaban Arısı", "Kelebek", "Tırtıl", "Hamamböceği", "Kriket", "Yusufçuk",
                   "Ateş Böceği", "Sinek", "Çekirge", "Bal Arısı", "Sivrisinek", "Kırmızı Böcek", "Akrep",
                   "İpekböceği", "Örümcek", "Eşek Arısı"]
insects_animal_list_de = ["Ameise", "Käfer", "Hummel", "Schmetterling", "Raupe", "Schabe", "Grille", "Libelle",
                   "Firefly", "Fly", "Grasshopper", "Honeybee", "Mosquito", "Red-Bug", "Scorpion", "Seidenraupe",
                   "Spinne", "Wespe"]
insects_animal_list_ru = ["Муравей", "Жук", "Шмель", "Бабочка", "Гусеница", "Таракан", "Сверчок", "Стрекоза",
                   "Светлячок", "Муха", "Кузнечик", "Пчелка", "Комар", "Красный жук", "Скорпион", "Шелкопряд",
                   "Паук", "Оса"]
insects_animal_list_uz = ["Chumoli", "Qo'ng'iz", "Bambli", "Kapalak", "Tırtıl", "Tarakan", "Kriket", "Ninachi",
                   "Olovli", "Pashsha", "Chigirtka", "Asal ari", "Chivin", "Qizil hasharot", "Chayon",
                   "Ipak qurti", "O'rgimchak", "Ara"]

insects_animal_list_dict = {"en":insects_animal_list_en, "tr":insects_animal_list_tr, "de":insects_animal_list_de,
                             "ru":insects_animal_list_ru, "uz": insects_animal_list_uz}

# ---------------------------- PET  ANIMAL LIST ------------------------------- #
pet_animal_list_en = ["Cat","Chameleon", "Dog", "Fish", "Hamster", "Mouse", "Parrot", "Pigeon", "Pig", "Rabbit",
                       "Snake", "Turtle"]

pet_animal_list_tr = ["Kedi", "Bukalemun", "Köpek", "Balık", "Hamster", "Fare", "Papağan", "Güvercin", "Domuz", "Tavşan",
                      "Yılan", "Kaplumbağa"]

pet_animal_list_de = ["Katze", "Chamäleon", "Hund", "Fisch", "Hamster", "Maus", "Papagei", "Taube", "Schwein", "Kaninchen",
                        "Schlange", "Schildkröte"]
pet_animal_list_ru = ["Кошка", "Хамелеон", "Собака", "Рыбка", "Хомяк", "Мышь", "Попугай", "Голубь", "Свинья", "Кролик",
                      "Змея", "Черепаха"]
pet_animal_list_uz = ["Mushuk", "Xameleon", "It", "Baliq", "Hamster", "Sichqoncha", "To'tiqush", "Kabutar", "Cho'chqa", "Quyon",
                        "Ilon", "Toshbaqa"]

pet_animal_list_dict = {"en":pet_animal_list_en, "tr":pet_animal_list_tr, "de":pet_animal_list_de,
                             "ru":pet_animal_list_ru, "uz": pet_animal_list_uz}
# ---------------------------- MAMMAL ANIMAL LIST ------------------------------- #
mammal_animal_list_en = ["Bat","Bear", "Blue-Whale", "Cat","Cow", "Dog", "Dolphin", "Donkey", "Elephant", "Fox",
                        "Giraffe", "Gorilla", "Horse", "Kangaroo","Leopard", "Lion", "Monkey","Panda", "Reindeer",
                        "Tiger", "Wolf"]

mammal_animal_list_tr = ["Yarasa", "Ayı", "Mavi Balina", "Kedi", "İnek", "Köpek", "Yunus", "Eşek", "Fil", "Tilki",
                         "Zürafa", "Gorilla", "At", "Kanguru", "Leopar", "Aslan", "Maymun", "Panda", "Ren geyiği",
                         "Kaplan", "Kurt"]

mammal_animal_list_de = ["Fledermaus", "Bär", "Blauwal", "Katze", "Kuh", "Hund", "Delfin", "Esel", "Elefant", "Fuchs",
                         "Giraffe", "Gorilla", "Pferd", "Känguru", "Leopard", "Löwe", "Affe", "Panda", "Rentier",
                         "Tiger", "Wolf"]

mammal_animal_list_ru = ["Летучая мышь", "Медведь", "Синий кит", "Кошка", "Корова", "Собака", "Дельфин", "Осел", "Слон",
                         "Лисица",
                         "Жираф", "Горилла", "Лошадь", "Кенгуру", "Леопард", "Лев", "Обезьяна", "Панда", "Северный олень",
                         "Тигр", "Волк"]

mammal_animal_list_uz = ["Ko'rshapalaklar", "Ayiq", "Ko'k kit", "Mushuk", "Sigir", "It", "Delfin", "Eshak", "Fil", "Tulki",
                         "Jirafa", "Gorilla", "Ot", "Kanguru", "Leopard", "Arslon", "Maymun", "Panda", "Shimol bug'usi",
                         "Yo'lbars", "Bo'ri"]
mammal_animal_list_dict = {"en":mammal_animal_list_en, "tr":mammal_animal_list_tr, "de":mammal_animal_list_de,
                             "ru":mammal_animal_list_ru, "uz": mammal_animal_list_uz}
# ---------------------------- SEA ANIMAL LIST ------------------------------- #
sea_animal_list_en = ["Blue-whale", "Catfish", "Crab", "Dolphin", "Eels", "Goldfish", "Jellyfish", "Oyster", "Penguin",
                      "Piranha", "Prawns", "Salmon", "Sea-horse", "Sea-lion", "Seal", "Shark", "Tuna"]
sea_animal_list_tr = ["Mavi Balina", "Yayın Balığı", "Yengeç", "Yunus", "Yılan Balığı", "Japon Balığı", "Denizanası",
                      "İstiridye", "Penguen"
                      "Piranha", "Karides", "Somon", "Deniz atı", "Deniz aslanı", "Mühür", "Köpekbalığı", "Ton Balığı"]
sea_animal_list_de = ["Blauwal", "Wels", "Krabbe", "Delfin", "Aal", "Goldfisch", "Qualle", "Auster", "Pinguin"
                      "Piranha", "Garnelen", "Lachs", "Seepferdchen", "Seelöwe", "Seehund", "Hai", "Thunfisch"]
sea_animal_list_ru = ["Синий кит", "Сом", "Краб", "Дельфин", "Угри", "Золотая рыбка", "Медуза", "Устрица", "Пингвин"
                      "Пираньи", "Креветки", "Лосось", "Морской конек", "Морской лев", "Тюлень", "Акула", "Тунец"]
sea_animal_list_uz = ["Ko'k kit", "Mushuk", "Qisqichbaqa", "Delfin", "Yilan baliqlari", "Oltin baliq", "Meduza", "Oyster", "Pingvin"
                      "Piranha", "Qisqichbaqalar", "Salmon", "Dengiz oti", "Dengiz sher", "Muhr", "Akula", "Tuna"]

sea_animal_list_dict = {"en":sea_animal_list_en, "tr":sea_animal_list_tr, "de":sea_animal_list_de,
                             "ru":sea_animal_list_ru, "uz": sea_animal_list_uz}
# ---------------------------- WILD ANIMAL LIST ------------------------------- #
wild_animal_list_en = ["Lion", "Tiger", "Elephant", "Giraffe", "Bear", "Zebra", "Panda", "Gorilla", "Monkey", "Wolf",
                      "Kangaroo", "Hippopotamus", "Deer", "Fox", "Koala", "Yak", "Chimpanzee",  "Antelope",
                      "Squirrel", "Mole", "Reindeer", "Jaguar", "Jackal", "Possum", "Rhinoceros",
                      "Cougar", "Hyena",  "Chipmunk", "Wombat"]
wild_animal_list_tr = ["Aslan", "Kaplan", "Fil", "Zürafa", "Ayı", "Zebra", "Panda", "Gorilla", "Maymun", "Kurt",
                       "Kanguru", "Su aygırı", "Geyik", "Tilki", "Koala", "Yak", "Şempanze", "Antilop",
                       "Sincap", "Köstebek", "Ren geyiği", "Jaguar", "Çakal", "Possum", "Gergedan",
                       "Puma", "Sırlan", "Sincap", "Wombat"]
wild_animal_list_de = ["Löwe", "Tiger", "Elefant", "Giraffe", "Bär", "Zebra", "Panda", "Gorilla", "Affe", "Wolf",
                       "Känguru", "Nilpferd", "Hirsch", "Fuchs", "Koala", "Yak", "Schimpanse", "Antilope",
                       "Eichhörnchen", "Maulwurf", "Rentier", "Jaguar", "Schakal", "Opossum", "Nashorn",
                       "Puma", "Hyäne", "Streifenhörnchen", "Wombat"]
wild_animal_list_ru = ["Лев", "Тигр", "Слон", "Жираф", "Медведь", "Зебра", "Панда", "Горилла", "Обезьяна", "Волк",
                       "Кенгуру", "Бегемот", "Олень", "Лисица", "Коала", "Як", "Шимпанзе", "Антилопа",
                       "Белка", "Крот", "Северный олень", "Ягуар", "Шакал", "Опоссум", "Носорог",
                       "Пума", "Гиена", "Бурундук", "Вомбат"]
wild_animal_list_uz = ["Arslon", "Yo'lbars", "Fil", "Jirafa", "Ayiq", "Zebra", "Panda", "Gorilla", "Maymun", "Bo'ri",
                       "Kanguru", "Begemot", "Kiyik", "Tulki", "Koala", "Yak", "Şimpanze", "Antilopa",
                       "Sincap", "Mole", "Shimol bug'usi", "Yaguar", "Shaqqal", "Possum", "Karkidon",
                       "Cougar", "Gyena", "Chipmunk", "Wombat"]

wild_animal_list_dict = {"en":wild_animal_list_en, "tr":wild_animal_list_tr, "de":wild_animal_list_de,
                             "ru":wild_animal_list_ru, "uz": wild_animal_list_uz}


def list_re_order(list):
    first_slice = int(len(list)/2)
    print(first_slice)
    list1 = list[0:first_slice]
    print(list1)
    list2 = list[first_slice:int(len(list)+1)]
    print(list2)
    result = [None]*(len(list1)+len(list2))
    result[::2] = list1
    result[1::2] = list2
    print(result)
    print(len(result))
    print(len(list))

# list_re_order(letters_tr)

# print(letters_tr[::2])
# print(letters_tr[1::2])