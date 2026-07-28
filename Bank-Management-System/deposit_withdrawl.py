from searchAccount import searchAccount

def takeInput():
    accountNum = int(input("Enter account number: "))
    amount = int(input("How much amount do you wish to deposit/withdraw?: "))
    return [accountNum, amount]


def deposit(db):
    accountNum, amount = takeInput()
    if(amount<0):
            print("Enter valid amount")
            return
    
    index = searchAccount(accountNum, db)
    if index!=False:
        db[index]["balance"] += amount
        for acc in range(len(db)):
            print(db[acc])
    else: 
        print("Sorry! No such account found.")


def withdrawl(db):
    accountNum, amount = takeInput()
    if(amount<0):
        print("Enter valid amount")
        return
    
    index = searchAccount(accountNum, db)
    if index!=False:
        if(db[index]["balance"]>=amount):
            db[index]["balance"] -= amount
            for acc in range(len(db)):
                print(db[acc])
        else:
            print(f"You do not have sufficient funds, balance left:{db[index]["balance"]}")
    else: 
        print("Sorry! No such account found.")