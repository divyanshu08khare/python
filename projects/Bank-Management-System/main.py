from create_account import createAccount
from deposit_withdrawl import deposit
from deposit_withdrawl import withdrawl
from transfer import transfer
from searchModule import search
from delete import delete
from statistics import statisticsFunc

accountDb = []
accountNumberStart = 1000


def runProgram():
    print("\n\n1. Create Account\n2. Deposit Money\n3. Withdraw Money\n4. Transfer Money\n5. Search Account\n6. Delete Account\n7. View All Accounts\n8. Bank Statistics\n9. Exit")
    serviceRequestNumber = int(input("Choose: "))
    if (serviceRequestNumber>9 or serviceRequestNumber<1):
        print("Please request a valid service\n")
        serviceRequestNumber = runProgram()

    return serviceRequestNumber



while True:
    serviceRequested = runProgram()

    match serviceRequested:
        case 1:
            accountNumberStart = createAccount(accountDb, accountNumberStart)
        case 2:
            deposit(accountDb)
        case 3:
            withdrawl(accountDb)
        case 4:
            transfer(accountDb)
        case 5:
            search(accountDb)
        case 6:
            delete(accountDb)
        case 7:
            print(accountDb)
        case 8:
            statisticsFunc(accountDb)
        case 9:
            break