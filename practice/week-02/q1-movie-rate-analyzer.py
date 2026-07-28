# Question 1: 🎬 Movie Rating Analyzer

# A movie website wants to analyze user ratings.

# Requirements

# Create the following functions:

# 1. addRatings()
# Ask the user how many people rated the movie.
# Accept ratings between 1 and 10 only.
# Store them in a list.
# Return the list.
# 2. showStatistics(ratings)

# Display:

# Highest rating
# Lowest rating
# Average rating (2 decimal places)
# Total number of ratings
# 3. searchRating(ratings)

# Ask the user for a rating.

# Display:

# All positions where that rating occurs.

# Example:

# Ratings:
# 8 7 9 7 6 7

# Enter rating: 7

# Found at:
# 2
# 4
# 6

# If not found:

# Rating not found.
# 4. removeLowest(ratings)

# Remove only the first occurrence of the lowest rating.

# Example

# Before

# [7, 4, 9, 4, 8]

# After

# [7, 9, 4, 8]
# 5. Main Menu
# 1. Enter Ratings
# 2. Show Statistics
# 3. Search Rating
# 4. Remove Lowest Rating
# 5. Show Ratings
# 6. Exit

# Keep running until Exit.


def runProgram():
    print("\n\n1. Enter Ratings\n2. Show Statistics\n3. Search Rating\n4. Remove Lowest Rating\n5. Show Ratings\n6. Exit")
    menuNumber = int(input("Choose: "))
    finalInput = menuNumber

    if(menuNumber<1 or menuNumber>6):
        print("Choose correct option\n")
        finalInput = runProgram()

    return finalInput

def takeInput(list1):
    reviewersCnt = int(input("\nHow many reviews you widh to give?\n"))
    i=1
    while i <= reviewersCnt:
        rating = int(input("How would you rate this, on a scale of 1-10? "))
        if(rating<1 or rating>10):
            print("You can rate between 1 - 10 only")
            continue
        else:
            list1.append(rating)
            i += 1

    

def addRatings(reviewList):
    takeInput(reviewList)
    return reviewList
    

def highestRating(list1):
    highest = 0
    total = 0
    for i, val in enumerate(list1):
        total += val
        if(val > highest):
            highest = val

    print(f"highest rating is {highest}")
    return total

def lowestRating(list1):
    if len(list1)==0:
        print("list is empty")
        return
    lowest = 10
    for i, val in enumerate(list1):
        if(val < lowest):
            lowest = val

   
    return lowest

   
def statistics(db):
    if(len(db) == 0):
        print("Rate first")
        return
    print(f"rating-list: {db}\n")
    totalRating = highestRating(db)
    lowest = lowestRating(db)
    print(f"average: {(totalRating/len(db)):.2f}")
    print(f"total ratings made: {len(db)}")
    print(f"lowest rating is {lowest}")
    return lowest

def searchRating(list1):
    if(len(list1)==0):
        print("list is empty")
        return
    
    rating = int(input("Enter rating you wish to search: "))

    flag = False
    indexList = []
    for i, r in enumerate(list1):
        if(r == rating):
            indexList.append(i+1)
            flag = True

    if(flag):
        print(f"rating indeces: {indexList}")
    else:
        print("No such rating is found")


def removeLowest(list1):
    l = lowestRating(list1)
    if(l):
        for i, li in enumerate(list1):
            if(li==l):
                list1.pop(i)
                break

        print(list1)
    else:
        print("list is empty")


database = []

while True:
    finalInput = runProgram()

    

    match finalInput:
        case 1:
            addRatings(database)
        case 2:
            lowest = statistics(database)
            
        case 3:
            searchRating(database)
        case 4:
            removeLowest(database)
        case 5:
            print(f"ratings: {database}")
        case 6:
            break
