class Menu:
    def __init__(self, converter):
        self.converter = converter

    def menu_interface(self):
        while True:
            choice = self.__get_menu_user_input()

            match choice:
                case 0:
                    break
                case 1:
                    self.__print_currencies()
                    continue
                case 2:
                    self.__convert_currencies()
                    continue
                case _:
                    print("No choice found")

    def __get_menu_user_input(self):
        print("[1] - print all currencies")
        print("[2] - convert currencies")
        print("[0] - quit")
        choice = input("Enter a number: ")

        try:
            choice = int(choice)
        except ValueError:
            return -1

        return choice

    def __print_currencies(self):
        currency_list = self.converter.get_currencies()

        for currency in currency_list:
            print(f"{currency['id']} - {currency['currencyName']}")

    def __convert_currencies(self):
        while True:
            currency_1_id = self.__get_currency_code("one")
            currency_2_id = self.__get_currency_code("two")
            amount = self.__get_amount()

            converted = self.converter.convert_currency(currency_1_id, currency_2_id, amount)

            if converted == -1:
                continue

            print(f"Converted {amount} {currency_1_id} to {converted} {currency_2_id}")
            break

    def __get_currency_code(self, currency_num):
        while True:
            currency_id = input(f"Enter a code for currency {currency_num}: ").upper()
            if not self.__is_currency_string(currency_id) or len(currency_id) != 3:
                print("Not a valid currency code")
                continue
            return currency_id

    def __is_currency_string(self, currency_id):
        if isinstance(currency_id, (int, float)):
            return False
        return True

    def __get_amount(self):
        while True:
            amount = input("Enter amount of currency one: ")

            try:
                amount = float(amount)
            except ValueError:
                print("Please enter a number")
                continue

            return amount