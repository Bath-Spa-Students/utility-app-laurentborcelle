class TColor:
    cyan = '\033[96m'
    green = '\033[92m'
    magenta = '\033[95m'
    purple = '\033[0;35m'
    light_purple = '\033[1;35m'
    red = '\033[0;31m'
    light_red = '\033[1;31m'
    yellow = '\033[93m'
    end = '\033[0m'

class SushiVendingMachine:
    def __init__(self):
        self.menu = {
            "S1": {"name": "Salmon Nigiri", "price": 15.00, "stock": 20},
            "S2": {"name": "California Roll", "price": 17.50, "stock": 20},
            "S3": {"name": "Tuna Sashimi", "price": 18.00, "stock": 20},
            "S4": {"name": "Dynamite Roll", "price": 15.00, "stock": 20},
            "S5": {"name": "Marukonouchi Bento", "price": 36.00, "stock": 10},
            "S6": {"name": "Spicy Salmon", "price": 16.00, "stock": 15},
            "S7": {"name": "Water", "price": 01.00, "stock": 60},
            "S8": {"name": "Coca-Cola", "price": 01.00, "stock": 50},
            "S9": {"name": "Sprite", "price": 01.00, "stock": 50},
            "S10": {"name": "Fanta", "price": 01.00, "stock": 50},

        }
        self.total_amount = 0.0
        self.order = []
        self.card_balance = 0.0
        self.remaining_card_balance = 0.0

    def center_text(self, text):
        terminal_width = 120
        return text.center(terminal_width)


    def display_menu(self):
        print("╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗")
        print("║ ︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿୨♡୧‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵  ║")
        print("                                                                                                                                               ")

        print("                      ░██████╗██╗░░░██╗░██████╗██╗░░██╗██╗  ██████╗░███████╗███╗░░██╗████████╗░█████╗░ ")
        print("                      ██╔════╝██║░░░██║██╔════╝██║░░██║██║  ██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔══██╗ ")
        print("                      ╚█████╗░██║░░░██║╚█████╗░███████║██║  ██████╦╝█████╗░░██╔██╗██║░░░██║░░░██║░░██║ ")
        print("                      ░╚═══██╗██║░░░██║░╚═══██╗██╔══██║██║  ██╔══██╗██╔══╝░░██║╚████║░░░██║░░░██║░░██║ ")
        print("                      ██████╔╝╚██████╔╝██████╔╝██║░░██║██║  ██████╦╝███████╗██║░╚███║░░░██║░░░╚█████╔╝ ")
        print("                      ╚═════╝░░╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝  ╚═════╝░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░ ")
        print("║ ︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿୨♡୧‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵‿︵  ║")                 
        print("╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")

        print("║        Code    |                  Item                     |      Price              |              Stock              ║")
        print("╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")
        for code, item in self.menu.items():
            code_column = f"║        {code}:      ┊"
            item_column = f"\t{item['name']}"
            price_column = f"┊      AED {item['price']:.2f}"
            stock_column = f"      ┊  \t{item['stock']}                       ║"

            print("{:<25}{:<30}{:<20}{:<40}".format(code_column, item_column, price_column, stock_column))
            print("╠════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╣")

        print("\n")

    def select_menu(self):
        while True:
            print("══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══")
            ent_itemcode = f"                                        \033[1mENTER ITEM {TColor.yellow}CODE{TColor.end} OF YOUR ORDER:\033[0m "
            product_code = input("\n" + ent_itemcode)
            print("\n══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══ ══")

            if product_code.lower() == 'done':
                return None  # 

            product = self.menu.get(product_code)
            if product is not None and product['stock'] > 0:
                return product
            elif product is not None and product['stock'] == 0:
                print(f"{TColor.red}Sorry,{TColor.end} {TColor.magenta}{product['name']}{TColor.end} {TColor.red}is out of stock.{TColor.end}")
            else:
                print("Invalid product code. Please try again.")
                
    def insert_money(self):
        money = float(input("Insert money: "))
        self.total_amount += money
        print("═════════════════════════════════════════════════════════════════════════════════")

    def process_order(self):
        while True:
            self.display_menu()  # Display the menu with remaining stocks
            selected_product = self.select_menu()
            if selected_product is None:
                break

            quantity = int(input("\n" + f"                                  ENTER THE \033[1m{TColor.magenta}QUANTITY{TColor.end}\033[0m OF YOUR CHOSEN ITEM '\033[3m{TColor.cyan}{selected_product['name']}{TColor.end}\033[0m': "))
            print("\n꒷꒦꒷꒦꒷꒦꒷꒦︶꒷꒦︶꒷꒦꒷꒷꒦꒷꒦꒷꒦︶꒷꒦︶꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷︶꒷꒦︶꒦꒷꒦꒷꒦꒷꒦꒷꒦︶꒷꒦︶꒷꒦꒷꒦꒷︶꒷꒦︶ ๋࣭ ⭑")
            if selected_product["stock"] >= quantity:
                item_name = selected_product["name"]
                item_price = selected_product["price"]
                total_price = item_price * quantity
                self.order.append({"name": item_name, "quantity": quantity, "total_price": total_price})
                self.total_amount += total_price
                selected_product["stock"] -= quantity
                print(f"\n                                        Added \033[1m{TColor.magenta}{quantity}{TColor.end}\033[0m \033[3m{TColor.cyan}{item_name}(s){TColor.end}\033[0m to your order.")
            else:
                print(f"\n{TColor.red}Insufficient stock. Please choose a different item.{TColor.end}\n")
                continue 

            underline_yes = "\033[4;32mYES\033[0m"
            underline_no = "\033[4;31mNO\033[0m"
            more_items = input(f"\n                                    Do you want to order more items? [{TColor.green}{underline_yes}{TColor.end}/{TColor.red}{underline_no}{TColor.end}]: ")
            if more_items.lower() != 'yes':
                break

    def print_receipt(self):
        print("\n꒷꒦꒷꒦꒷꒦꒷꒦︶꒷꒦︶꒷꒦꒷꒷꒦꒷꒦꒷꒦︶꒷꒦︶꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷︶꒷꒦︶꒦꒷꒦꒷꒦꒷꒦꒷꒦︶꒷꒦︶꒷꒦꒷꒦꒷︶꒷꒦︶ ๋࣭ ⭑")
        receipt_title = "«̶ ̶̶̶ ̶ «̶ ̶̶̶  R̳E̳C̳E̳I̳P̳T̳ ̶ ̶»̶ ̶̶̶ ̶ »̶--"
        print("\n" + self.center_text(receipt_title))
        for item in self.order:
            qnit = f"\n{TColor.magenta}{item['quantity']}{TColor.end} {TColor.cyan}{item['name']}{TColor.end} - {TColor.yellow}AED {item['total_price']:.2f}{TColor.end}"
            print(self.center_text(qnit))
        total_a = f"\nTotal: {TColor.yellow} AED {self.total_amount:.2f}{TColor.end}"
        print("\n«̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ «̶ ̶̶̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶»̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ »̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ »")
        print(self.center_text(total_a))
        print("\n«̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ «̶ ̶̶̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶»̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ »̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ »")

    def choose_payment_method(self):
        while True:
            payment_method = input(f"\nChoose payment method: ({TColor.green}CASH{TColor.end}/{TColor.red}CARD{TColor.end}): ").casefold()
            if payment_method in ['cash', 'card']:
                return payment_method
            else:
                print(f"{TColor.red}𝗜𝗻𝘃𝗮𝗹𝗶𝗱 𝗽𝗮𝘆𝗺𝗲𝗻𝘁 𝗺𝗲𝘁𝗵𝗼𝗱. 𝗘𝗻𝘁𝗲𝗿{TColor.end} [\033[3m{TColor.green}CASH{TColor.end}\033[0m/\033[3m{TColor.red}CARD{TColor.end}\033[0m]")

    def process_payment(self, payment_method):
        if payment_method == 'cash':
            cash_amount = float(input(f"\nEnter the amount of {TColor.green}cash{TColor.end}: "))
            change = cash_amount - self.total_amount
            if change >= 0:
                print(f"\n{TColor.green}Payment successful.{TColor.end}")
                print("\n꒷꒦꒷꒦꒷꒦꒷꒦︶꒷꒦︶꒷꒦꒷꒷꒦꒷꒦꒷꒦︶꒷꒦︶꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷︶꒷꒦︶꒦꒷꒦꒷꒦꒷꒦꒷꒦︶꒷꒦︶ ๋࣭ ⭑")
                print(f"\nAmount paid: {TColor.yellow}AED {cash_amount:.2f}{TColor.end} \nChange: {TColor.yellow}AED {change:.2f}{TColor.end}")
                self.total_amount = 0.0  
            else:
                print("\n«̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ «̶ ̶̶̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶»̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ »̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ »")
                print(f"\n{TColor.red}Insufficient cash. Please try again.{TColor.end}")
                print("\n«̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ «̶ ̶̶̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶»̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ »̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ »")
                self.process_payment(payment_method)

        elif payment_method == 'card':
            while True:
                if self.remaining_card_balance == 0.0:
                    card_balance = float(input(f"\nEnter the balance on your {TColor.red}card{TColor.end}: "))
                    self.remaining_card_balance = card_balance

                if self.remaining_card_balance >= self.total_amount:
                    self.remaining_card_balance -= self.total_amount
                    print(f"\n{TColor.green}Card payment successful.{TColor.end}")
                    print("\n«̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶ «̶ ̶̶̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶»̶ ̶ ̶ ̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ »̶ ̶̶̶ ̶ ̶ ̶ ̶ ̶ ̶ ̶̶̶ »")
                    print(f"\nAmount paid: {TColor.yellow}AED {self.total_amount:.2f}{TColor.end} \nRemaining balance: {TColor.yellow}AED {self.remaining_card_balance:.2f}{TColor.end}")
                    self.total_amount = 0.0  
                    break
                else:
                    print(f"\n{TColor.red}Insufficient balance on the card. Please try again.{TColor.end}")

    def order_again(self):
        underline_yes = "\033[4;32mYES\033[0m"
        underline_no = "\033[4;31mNO\033[0m"
        response = input(f"\nDo you want to order again? [{TColor.green}{underline_yes}{TColor.end}/{TColor.red}{underline_no}{TColor.end}]: ")
        return response.lower() == 'yes'

    def run(self):
        while True:
            self.display_menu()
            self.process_order()
            self.print_receipt()

            payment_method = self.choose_payment_method()
            if payment_method == 'card':
                self.process_payment(payment_method)
            else:
                self.process_payment(payment_method)

            print("\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
            print("\nThank you for ordering!")
            print("""\n─────────▄▀────
────█▀▀▀█▀█────
─────▀▄░▄▀─────
───────█───────
─────▄▄█▄▄─────
""")

            if not self.order_again():
                break

# Indicators
if __name__ == "__main__":
    vending_machine = SushiVendingMachine()
    vending_machine.run()

