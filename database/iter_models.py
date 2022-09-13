from models_sql import *


def iter_models():
    # my_list = (Ageless(), Aksessury_image())

    my_list = [Ageless, Aksessury_image, Bioslimming, Clear_cell, Ibeauty,
               Iluma, Image_md, Imask, Irescue, Itrial, Nabory_image,
               O2_lift, Ormedic, Prevention, The_max, Vital_c]

    for it in my_list:
        # print(it)
        return next(it)

# iter_models()