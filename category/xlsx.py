import xlsxwriter
from category import array_ageless, array_aksessury_image, array_bioslimming,\
    array_clear_cell, array_ibeauty, array_iluma, array_image_md, array_imask,\
    array_irescue, array_itrial, array_nabory_image, array_o2_lift, array_ormedic, \
    array_prevention, array_the_max, array_vital_c


def writer(ageless, aksessur, bioslimming, clear, ibeauty, iluma, image_md, imask, irescue, itrial, nabory, o2, ormedic, prevention, the_max, vital_c):
    book = xlsxwriter.Workbook(r"/Users/bujikuh/Desktop/Cosmetics compain/Image/Image.xlsx")

    page_1 = book.add_worksheet('Ageless')
    page_2 = book.add_worksheet('Aksessury')
    page_3 = book.add_worksheet('Bioslimming')
    page_4 = book.add_worksheet('Clear cell')
    page_5 = book.add_worksheet('iBeauty')
    page_6 = book.add_worksheet('iLuma')
    page_7 = book.add_worksheet('Image md')
    page_8 = book.add_worksheet('iMask')
    page_9 = book.add_worksheet('iRescue')
    page_10 = book.add_worksheet('iTrial')
    page_11 = book.add_worksheet('Nabory image')
    page_12 = book.add_worksheet('o2 lift')
    page_13 = book.add_worksheet('Ormedic')
    page_14 = book.add_worksheet('Prevention+')
    page_15 = book.add_worksheet('The Max')
    page_16 = book.add_worksheet('Vital c')
    bold = book.add_format({'bold': True})

    headers = ['Наименование', "Цена", " Описание", "Ссылка на фото товара", "Наличие товара", "Примечание"]
    for col, h in enumerate(headers):
        page_1.write_string(0, col, h, cell_format=bold)
        page_2.write_string(0, col, h, cell_format=bold)
        page_3.write_string(0, col, h, cell_format=bold)
        page_4.write_string(0, col, h, cell_format=bold)
        page_5.write_string(0, col, h, cell_format=bold)
        page_6.write_string(0, col, h, cell_format=bold)
        page_7.write_string(0, col, h, cell_format=bold)
        page_8.write_string(0, col, h, cell_format=bold)
        page_9.write_string(0, col, h, cell_format=bold)
        page_10.write_string(0, col, h, cell_format=bold)
        page_11.write_string(0, col, h, cell_format=bold)
        page_12.write_string(0, col, h, cell_format=bold)
        page_13.write_string(0, col, h, cell_format=bold)
        page_14.write_string(0, col, h, cell_format=bold)
        page_15.write_string(0, col, h, cell_format=bold)
        page_16.write_string(0, col, h, cell_format=bold)


    page_1.set_column('A:A', 20)
    page_1.set_column('B:B', 10)
    page_1.set_column('C:C', 100)
    page_1.set_column('D:D', 25)
    page_1.set_column('E:E', 30)
    page_1.set_column('F:F', 40)

    page_2.set_column('A:A', 20)
    page_2.set_column('B:B', 10)
    page_2.set_column('C:C', 100)
    page_2.set_column('D:D', 25)
    page_2.set_column('E:E', 25)
    page_2.set_column('F:F', 40)

    page_3.set_column('A:A', 20)
    page_3.set_column('B:B', 10)
    page_3.set_column('C:C', 100)
    page_3.set_column('D:D', 25)
    page_3.set_column('E:E', 25)
    page_3.set_column('F:F', 40)

    page_4.set_column('A:A', 20)
    page_4.set_column('B:B', 10)
    page_4.set_column('C:C', 100)
    page_4.set_column('D:D', 25)
    page_4.set_column('E:E', 25)
    page_4.set_column('F:F', 40)

    page_5.set_column('A:A', 20)
    page_5.set_column('B:B', 10)
    page_5.set_column('C:C', 100)
    page_5.set_column('D:D', 25)
    page_5.set_column('E:E', 25)
    page_5.set_column('F:F', 40)

    page_6.set_column('A:A', 20)
    page_6.set_column('B:B', 10)
    page_6.set_column('C:C', 100)
    page_6.set_column('D:D', 25)
    page_6.set_column('E:E', 25)
    page_6.set_column('F:F', 40)

    page_7.set_column('A:A', 20)
    page_7.set_column('B:B', 10)
    page_7.set_column('C:C', 100)
    page_7.set_column('D:D', 25)
    page_7.set_column('E:E', 25)
    page_7.set_column('F:F', 40)

    page_8.set_column('A:A', 20)
    page_8.set_column('B:B', 10)
    page_8.set_column('C:C', 100)
    page_8.set_column('D:D', 25)
    page_8.set_column('E:E', 25)
    page_8.set_column('F:F', 40)

    page_9.set_column('A:A', 20)
    page_9.set_column('B:B', 10)
    page_9.set_column('C:C', 100)
    page_9.set_column('D:D', 25)
    page_9.set_column('E:E', 25)
    page_9.set_column('F:F', 40)

    page_10.set_column('A:A', 20)
    page_10.set_column('B:B', 10)
    page_10.set_column('C:C', 100)
    page_10.set_column('D:D', 25)
    page_10.set_column('E:E', 25)
    page_10.set_column('F:F', 40)

    page_11.set_column('A:A', 20)
    page_11.set_column('B:B', 10)
    page_11.set_column('C:C', 100)
    page_11.set_column('D:D', 25)
    page_11.set_column('E:E', 25)
    page_11.set_column('F:F', 40)

    page_12.set_column('A:A', 20)
    page_12.set_column('B:B', 10)
    page_12.set_column('C:C', 100)
    page_12.set_column('D:D', 25)
    page_12.set_column('E:E', 25)
    page_12.set_column('F:F', 40)

    page_13.set_column('A:A', 20)
    page_13.set_column('B:B', 10)
    page_13.set_column('C:C', 100)
    page_13.set_column('D:D', 25)
    page_13.set_column('E:E', 25)
    page_13.set_column('F:F', 40)

    page_14.set_column('A:A', 20)
    page_14.set_column('B:B', 10)
    page_14.set_column('C:C', 100)
    page_14.set_column('D:D', 25)
    page_14.set_column('E:E', 25)
    page_14.set_column('F:F', 40)

    page_15.set_column('A:A', 20)
    page_15.set_column('B:B', 10)
    page_15.set_column('C:C', 100)
    page_15.set_column('D:D', 25)
    page_15.set_column('E:E', 25)
    page_15.set_column('F:F', 40)

    page_16.set_column('A:A', 20)
    page_16.set_column('B:B', 10)
    page_16.set_column('C:C', 100)
    page_16.set_column('D:D', 25)
    page_16.set_column('E:E', 25)
    page_16.set_column('F:F', 40)

    row = 1
    column = 0

    for item in ageless():

        page_1.write(row, column, item[0])
        page_1.write(row, column+1, item[1])
        page_1.write(row, column+2, item[2])
        page_1.write(row, column+3, item[3])
        page_1.write(row, column+4, item[4])
        row += 1
    row = 1

    for item in aksessur():

        page_2.write(row, column, item[0])
        page_2.write(row, column + 1, item[1])
        page_2.write(row, column + 2, item[2])
        page_2.write(row, column + 3, item[3])
        page_2.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in bioslimming():

        page_3.write(row, column, item[0])
        page_3.write(row, column + 1, item[1])
        page_3.write(row, column + 2, item[2])
        page_3.write(row, column + 3, item[3])
        page_3.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in clear():

        page_4.write(row, column, item[0])
        page_4.write(row, column + 1, item[1])
        page_4.write(row, column + 2, item[2])
        page_4.write(row, column + 3, item[3])
        page_4.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in ibeauty():

        page_5.write(row, column, item[0])
        page_5.write(row, column + 1, item[1])
        page_5.write(row, column + 2, item[2])
        page_5.write(row, column + 3, item[3])
        page_5.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in iluma():

        page_6.write(row, column, item[0])
        page_6.write(row, column + 1, item[1])
        page_6.write(row, column + 2, item[2])
        page_6.write(row, column + 3, item[3])
        page_6.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in image_md():

        page_7.write(row, column, item[0])
        page_7.write(row, column + 1, item[1])
        page_7.write(row, column + 2, item[2])
        page_7.write(row, column + 3, item[3])
        page_7.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in imask():

        page_8.write(row, column, item[0])
        page_8.write(row, column + 1, item[1])
        page_8.write(row, column + 2, item[2])
        page_8.write(row, column + 3, item[3])
        page_8.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in irescue():

        page_9.write(row, column, item[0])
        page_9.write(row, column + 1, item[1])
        page_9.write(row, column + 2, item[2])
        page_9.write(row, column + 3, item[3])
        page_9.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in itrial():

        page_10.write(row, column, item[0])
        page_10.write(row, column + 1, item[1])
        page_10.write(row, column + 2, item[2])
        page_10.write(row, column + 3, item[3])
        page_10.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in nabory():

        page_11.write(row, column, item[0])
        page_11.write(row, column + 1, item[1])
        page_11.write(row, column + 2, item[2])
        page_11.write(row, column + 3, item[3])
        page_11.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in o2():

        page_12.write(row, column, item[0])
        page_12.write(row, column + 1, item[1])
        page_12.write(row, column + 2, item[2])
        page_12.write(row, column + 3, item[3])
        page_12.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in ormedic():

        page_13.write(row, column, item[0])
        page_13.write(row, column + 1, item[1])
        page_13.write(row, column + 2, item[2])
        page_13.write(row, column + 3, item[3])
        page_13.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in prevention():

        page_14.write(row, column, item[0])
        page_14.write(row, column + 1, item[1])
        page_14.write(row, column + 2, item[2])
        page_14.write(row, column + 3, item[3])
        page_14.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in the_max():

        page_15.write(row, column, item[0])
        page_15.write(row, column + 1, item[1])
        page_15.write(row, column + 2, item[2])
        page_15.write(row, column + 3, item[3])
        page_15.write(row, column + 4, item[4])
        row += 1
    row = 1

    for item in vital_c():

        page_16.write(row, column, item[0])
        page_16.write(row, column + 1, item[1])
        page_16.write(row, column + 2, item[2])
        page_16.write(row, column + 3, item[3])
        page_16.write(row, column + 4, item[4])
        row += 1

    book.close()

writer(array_ageless, array_aksessury_image, array_bioslimming, array_clear_cell, array_ibeauty, array_iluma, array_image_md, array_imask, array_irescue, array_itrial, array_nabory_image, array_o2_lift, array_ormedic, array_prevention, array_the_max, array_vital_c)
