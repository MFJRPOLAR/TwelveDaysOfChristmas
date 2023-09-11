christmas = [
        "A partridge in a pear tree",
        "Two turtle doves",
        "Three French hens",
        "Four calling birds",
        "Five golden rings",
        "Six geese a-laying",
        "Seven swans a-swimming",
        "Eight maids a-milking",
        "Nine ladies dancing",
        "Ten lords a-leaping",
        "Eleven pipers piping",
        "Twelve drummers drumming"
]

days = [
        "First",
        "Second",
        "Third",
        "Fourth",
        "Fifth",
        "Sixth",
        "Seventh",
        "Eighth",
        "Ninth",
        "Tenth",
        "Eleventh",
        "Twelfth"]

number = int(input("Please enter a number between 1 and 12: "))
while (number < 1 or number > 12):
    print(f"Please enter a number (1-12): {number}")
    print("Invalid Number.")
    number = int(input("Please enter a number between 1 and 12: "))


print(f"On the {days[number-1]} a day of christmas my true love gave to me.... ")

for num in range(number-1,-1,-1):
    print(f"{christmas[num]}")