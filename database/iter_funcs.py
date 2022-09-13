from category import *


def iter_func():
    my_list = [array_ageless(), array_aksessury_image(), array_bioslimming(),
    array_clear_cell(), array_ibeauty(), array_iluma(), array_image_md(), array_imask(),
    array_irescue(), array_itrial(), array_nabory_image(), array_o2_lift(), array_ormedic(),
    array_prevention(), array_the_max(), array_vital_c()]

    # my_list = (array_ageless, array_aksessury_image, array_bioslimming,
    #            array_clear_cell, array_ibeauty, array_iluma, array_image_md, array_imask,
    #            array_irescue, array_itrial, array_nabory_image, array_o2_lift, array_ormedic,
    #            array_prevention, array_the_max, array_vital_c)



    for func in my_list:
        # print(func)
        return next(func)

# iter_func()

