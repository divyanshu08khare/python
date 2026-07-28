from searchAccount import searchAccount

def takeInput():
    AccountNo = int(input("Enter the account number you wish to get deatail for: "))
    return AccountNo

def search(db):
    accountNum = takeInput()
    index = searchAccount(accountNum, db)
    if(index<0):
        print("Account not found")
    else:
        print(db[index])
