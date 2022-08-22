import xlsxwriter
from main import array_nabory_image

def writer(parametr):
    book = xlsxwriter.Workbook(r"/Users/santa/Desktop/Cosmetics compain/Image/Image(test).xlsx")
    page = book.add_worksheet('Product')
    bold = book.add_format({'bold': True})

    headers = ['Наименование', "Цена", " Описание", "Ссылка на фото товара", 'Наличие', "Примечание"]
    for col, h in enumerate(headers):
        page.write_string(0, col, h, cell_format = bold)
    # for row, item in enumerate(start=1):

    row = 1
    column = 0

    page.set_column('A:A', 40)
    page.set_column('B:B', 10)
    page.set_column('C:C', 100)
    page.set_column('D:D', 40)
    page.set_column('E:E', 15)
    page.set_column('F:F', 40)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        row += 1

    book.close()

writer(array_nabory_image)
