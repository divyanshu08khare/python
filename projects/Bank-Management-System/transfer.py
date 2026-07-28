from searchAccount import searchAccount

def takeInput():
    sourceAccount = int(input("Enter source account number: "))
    destinationAccount = int(input("Enter destination account number: "))
    amount = int(input("Enter amount to be transferred: "))

    return [sourceAccount, destinationAccount, amount]

def performTransfer(sourceIndex, destinationIndex, amt, db):
    if(db[sourceIndex]["balance"]<amt):
        print("Insufficient balance")
    else:
        db[sourceIndex]["balance"] -= amt
        db[destinationIndex]["balance"] += amt
        print("Transfer was successful")

def transfer(db):
    sourceAccountNo, destinationAccountNo, amount = takeInput()
    sourceAccountIndex = searchAccount(sourceAccountNo, db)
    destinationAccountIndex = searchAccount(destinationAccountNo, db)
    if(sourceAccountIndex!=False and destinationAccountIndex!=False and amount>0):
        performTransfer(sourceAccountIndex, destinationAccountIndex, amount, db,)
    else:
        if(sourceAccountIndex==False and sourceAccountIndex!=0):
            print("source account not found")
        else:
            print("destination account not found")