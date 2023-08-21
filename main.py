# Import  random module
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#Count number of names
number=len(names)
#Pick random number from total number of names
payer_id=random.randint(0,number-1)
#Pick payer's name
payer_name=names[payer_id]
#Print output
print(f"{payer_name} is going to buy the meal today!")