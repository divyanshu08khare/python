def searchAccount(accNum, db):
    for i in range(len(db)):
        if(db[i]["accountNumber"] == accNum):
            return i

    return False