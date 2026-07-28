def checkCreateAccInput(account):
    if account["age"]<18:
        return False, "You are underage"
    elif account["balance"]<500:
        return False, "You need to comply with minimum balance"
    else:
        return True, "You are eligible"

def createAccountInput(account):
    account["name"] = input("Enter Account Holder's Name: ")
    account["age"] = int(input("Enter Account Holder's Age: "))
    account["balance"] = int(input("Enter the amount with which you wish to open your account, minimum balanace = 500: " ))
    validity, message = checkCreateAccInput(account)
    return validity, message

def createAccount(db, rootAcNumber):
    
    account = {
    "accountNumber": None,
    "name": None,
    "age": None,
    "balance": None
    }
    validity, message = createAccountInput(account)

    if (validity):
        rootAcNumber += 1
        account["accountNumber"] = rootAcNumber
        db.append(account)
        for acc in range(len(db)):
            print(db[acc])
            
        
    else:
        print(message)

    return rootAcNumber
    
