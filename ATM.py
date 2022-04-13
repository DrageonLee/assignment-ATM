user = []

class Account:
    def __init__(self):
        self.name = input("What is your name : ")
        self.PIN = int(input("Please input your PIN number(4digits) : "))
        while len(str(self.PIN)) !=4:
            self.PIN = int(input("Please input your PIN number again(4digits): "))
        self.account = []
        if self.name not in list(i['name'] for i in user):
            user.append({'name' : self.name, 'PIN' : self.PIN})
        else : 
            print("Same user is enrolled")
    def checkAccount(self):
        self.account_list = list(i for i in filter(lambda x : x['name'] == self.name, user))
        if 'Account' not in self.account_list[0].keys():
            self.account_list[0]['Account'] = []
        if bool(self.account_list[0]['Account']) == False:
            print("There is not account.")
            answer = input("Do you want to resister? [Y/N]")
            if answer == 'Y':
                return self.addAccount()
            elif answer == 'N':
                return 'Good bye'
        else :
            return self.account_list
    def addAccount(self) :
        self.ID = 0

        if len(self.account_list[0]['Account']) != 0:
            self.ID = self.account_list[0]['Account'][-1]['ID'] + 1
        self.account_list[0]['Account'].append({'ID' : self.ID, 'Balance' : 0})
        return f'New account was added. Account list : {self.account_list[0]}'

class Operate:
    def __init__(self):
        self.user_list = user
    def insertCard(self):
        name = input("Input your name : ")
        self.name = name
        user_name_list = list(i['name'] for i in self.user_list)
        if name in user_name_list:
            PIN = int(input('Please input your PIN : '))
            print(PIN)
            print(name)
            if PIN == list(i['PIN'] for i in filter(lambda x : x['name'] == name, self.user_list))[0]:
                return self.selectAccount()
            else : 
                return 'Check PIN number again'
        else:
            answer = input("It is not enrolled name. Do you want to retry? [Y/N] : ")
            if answer == 'Y':
                return self.insertCard()
            else : 
                return "Good bye"
    def selectAccount(self):
        account_list = list(i['Account'] for i in filter(lambda x : x['name'] == self.name, self.user_list))[0]
        print(account_list)
        self.choice = int(input('Select the account : '))

        print(list(i['ID'] for i in account_list))
        if self.choice in list(i['ID'] for i in account_list):
            print(1111)
            print(list(filter(lambda x : x['ID'] == self.choice, account_list)))
            self.selected_account = list(filter(lambda x : x['ID'] == self.choice, account_list))[0]
            print(12345)
            print(self.selected_account)
        next = int(input("What is next? \n 1. Balance \n 2. Deposit \n 3. Withdraw \n 4. Done \n"))
        if next == 1 :
            return self.Balance()
        elif next == 2 :
            money = int(input("How much?"))
            return self.Deposit(money)
        elif next == 3 :
            money = int(input("How much?"))
            return self.Withdraw(money)
        elif next == 4 :
            return 'Thank you for using'

    def Balance(self) : 
        return self.selected_account
    
    def Deposit(self, money):
        name = self.name
        balance = self.selected_account
        result = balance['Balance'] + money
        for i in user:
            if i['name'] == name :
                for y in i['Account']:
                    if y['ID'] == self.choice:
                        y['Balance'] = result
        return result

    def Withdraw(self, money):
        name = self.name
        balance = self.selected_account
        result = balance['Balance'] - money
        if result < 0:
            print("Your account has not enough money. Check again")
            print(balance)
            money = int(input("Please check your balance : "))
            return self.Withdraw(money)
        else : 
            for i in user:
                if i['name'] == name :
                    for y in i['Account']:
                        if y['ID'] == self.choice:
                            y['Balance'] = result
        return f'Balance : {result}'