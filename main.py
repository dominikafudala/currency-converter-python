from Converter import Converter
from Menu import Menu

BASE_URL = "https://free.currconv.com"

if __name__ == '__main__':
    converter = Converter(BASE_URL)
    menu = Menu(converter)

    menu.menu_interface()
