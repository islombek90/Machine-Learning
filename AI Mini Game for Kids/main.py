# import pyperclip
import my_data_analysis

import constants
import my_face_recognition
import ui_setup



my_face_recognition.face_id()

if constants.name != "Islam":
    print(constants.name)
    ui_setup.main_window()
    ui_setup.windows.mainloop()
else:
    print(constants.name)

    my_data_analysis.developper_widow()


