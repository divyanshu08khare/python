# Part 2: Exact Math & Floating-Point Edge Cases
# Q4. The Accurate Bill Splitter (Decimal)
# A restaurant bill needs to be split among 3 friends.

# Bill amount: "$100.10"

# Tip percentage: "15%"

# Using Python's Decimal module, compute the exact total bill (bill + tip) and the exact share per person, rounded to 2 decimal places.

from decimal import Decimal

total_bill = "$100.10"
tip_percentage = "15%"

total_bill_sanitized = total_bill.removeprefix("$")
total_bill_sanitized = round((Decimal(total_bill_sanitized)),2)

tip_sanitized = tip_percentage.removesuffix("%")
tip_sanitized= round(Decimal(tip_sanitized),2)

final_tip = (tip_sanitized/round((Decimal(100)),2)) * total_bill_sanitized
grand_total = total_bill_sanitized + final_tip

each_split = grand_total/round((Decimal(3)),2)

print(f"{each_split:.2f}")