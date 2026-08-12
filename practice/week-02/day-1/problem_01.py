

# ---

# ### **Problem 1: Temperature Unit Converter**

# Write a function `convert_temperature(temp_str)` that takes a string like `"100F"` or `"37C"`.

# * Extract the number and the unit (`'C'` or `'F'`).
# * Convert **Celsius to Fahrenheit** ($F = C \times \frac{9}{5} + 32$) or **Fahrenheit to Celsius** ($C = (F - 32) \times \frac{5}{9}$).
# * Return the converted value rounded to 1 decimal place with the new unit.
# * If unit is neither `'C'` nor `'F'`, return `"Invalid Unit"`.

# **Test Cases:**

# * Input: `"100F"` $\rightarrow$ Output: `"37.8C"`
# * Input: `"0C"` $\rightarrow$ Output: `"32.0F"`
# * Input: `"50K"` $\rightarrow$ Output: `"Invalid Unit"`

# ---

# ### **Problem 2: Smart Bill Splitter**

# Write a script or function `split_bill(total_str, tip_percent, people)`:

# * Cast `total_str` to float, `tip_percent` to int, `people` to int.
# * If `people <= 0`, return `"Number of people must be at least 1"`.
# * Calculate total amount including tip: $\text{Total} + (\text{Total} \times \frac{\text{Tip}}{100})$.
# * Calculate share per person and return it formatted as a string rounded to 2 decimal places (e.g., `"$28.75"`).

# **Test Cases:**

# * Input: `total_str="100.00", tip_percent=15, people=4` $\rightarrow$ Output: `"$28.75"`
# * Input: `total_str="50.0", tip_percent=10, people=0` $\rightarrow$ Output: `"Number of people must be at least 1"`

# ---

# ### **Problem 3: Username Sanitizer**

# Write a function `clean_username(raw_user)` that takes a messy input string and validates it:

# 1. Strip extra leading/trailing spaces.
# 2. Remove illegal characters `@`, `!`, `#`, `$`.
# 3. Check length: If the cleaned length is less than 5 or greater than 12 characters, return `"Invalid Length"`.
# 4. Check starting character: Must start with an alphabetical letter (`a-z` or `A-Z`). If not, return `"Must start with a letter"`.
# 5. If all checks pass, return the cleaned string in all **lowercase**.

# **Test Cases:**

# * Input: `"  @John_Doe99!  "` $\rightarrow$ Output: `"john_doe99"` (length 10, valid)
# * Input: `"123user"` $\rightarrow$ Output: `"Must start with a letter"`
# * Input: `"  #hi!  "` $\rightarrow$ Output: `"Invalid Length"`

# ---

# ### **Problem 4: Number Classifier Loop**

# Given a list of numbers, iterate through them using a `for` loop and print a classification string for each:

# * Check if it is `Zero`, `Positive Even`, `Positive Odd`, `Negative Even`, or `Negative Odd`.

# ```python
# # Sample Input List
# numbers = [0, 14, -7, 9, -22, 3.5]

# # Expected Printed Output:
# # 0 -> Zero
# # 14 -> Positive Even
# # -7 -> Negative Odd
# # 9 -> Positive Odd
# # -22 -> Negative Even
# # 3.5 -> Not an Integer

# ```

# ---

def checkNum(data):
    for i in range(len(data)):
        code = ord(data[i])
        if((code>47 and code<58) or code==46 or code==45):
            continue
        else:
            return False

    return True



def runInput():
    while(True):
        inputData = input("Enter the input temperature\n")
        inputString = inputData.lower()
        if(len(inputString)<2): 
            print("Enter correct input")
            continue

        n = len(inputString)
        endChar = inputString[n-1]

        if( (endChar != 'c' and endChar != 'f') or not checkNum(inputString[0:-1]) ):
            print("Enter correct input")
            continue
        

        return float(inputString[0:-1]), endChar
     

def convertToCelsius(stringInput):
    result = (stringInput - 32) * (5/9)
    print(f"{result:.2f}C")


def covertToFarheneit(stringInput):
    result = (stringInput * (9/5)) + 32
    print(f"{result:.2f}F")


inputData, endChar = runInput()

if(endChar == 'c'):
    covertToFarheneit(inputData)
else:
    convertToCelsius(inputData)


