from searchAccount import searchAccount

def takeInput():
    AccountNo = int(input("Enter the account number you wish to delete: "))
    return AccountNo


def delete(db):
    accountNum = takeInput()
    index = searchAccount(accountNum, db)
    if(index<0):
            print("Account not found")
    else:
            db.pop(index)
            print("Account deleted successfully")
