# Total Customers

# Total Money

# Richest Customer

# Average Balance

def customerLength(db):
    print(f"total number of customers: {len(db)}")
    return len(db)


def totalMoney(db):
    total = 0
    richest = db[0]
    for i in range(len(db)):
        total += db[i]["balance"]
        if(db[i]["balance"]>richest["balance"]):
            richest = db[i]

    print(f"total money: {total}")
    return total, richest


def average(total,length):
    return total/length

def statisticsFunc(db):

    if(len(db)==0):
        print("No customers yet in bank")
        return

    totalCustomers = customerLength(db)
    totalFunds, richest = totalMoney(db)
    averageBalance = average(totalFunds, totalCustomers)
    print(f"total customers: {totalCustomers}")
    print(f"total money: {totalFunds}")
    print(f"average balance: {averageBalance}")
    print(f"Richest customer is {richest["name"]}")