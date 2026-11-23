# # exe .1
# num1 = 25
# num2 = 7
# print(F"""
# Addition: {num1} + {num2} = {num1 + num2}
# Subtraction {num1} - {num2} = {num1 - num2}
# Multiplication {num1} * {num2} = {num1 * num2}
# Division {num1} / {num2} = {num1 / num2}
# Integer division {num1} // {num2} = {num1 // num2}
# Remainder {num1} % {num2} = {num1 % num2}
# Exponentiation {num1} ** {num2} = {num1 ** num2}
# """)


# # exe .2
# balance = 1000
# print(balance)
# balance += 250
# print(balance)
# balance -= 100
# print(balance)
# balance *= 2
# print(balance)
# balance /= 4
# print(balance)


# # exe .3
# price = int(input("please enter a price "))
# descount = int(input("please enter descount in precent "))
# print(f"descount = {(price/100*descount)} total price apter descount {price-(price/100*descount)} ")


# # exe .4
# count = int(input("please enter the original of Loan "))
# Annual_interest_rate = int(input("please enter Annual interest rate "))
# print(f"the rate after 1 year {count/100*Annual_interest_rate} the loan after yaer {count+(count/100*Annual_interest_rate)}")


# # exe .5
# greads = []
# for i in range(3):
#     gread = float(input("please enter a gread "))
#     greads.append(gread)
# print(f"the avrage of your tree grades is {sum(greads)/len(greads)}")

# # exe .6
# first_name = "David"
# last_name = "Cohen"
# city = "Tel Aviv"
# print(f"Hello, my name is {first_name} {last_name} and I live in {city} ")
# print("Hello, my name is " + first_name ,last_name ,"and I live in " + city)

# # exe .7
# name = input("please enter your name ")
# print(f"""
# name: {name}
# douration: = {len(name)}
# upper name: {name.upper()}
# lower name: {name.lower()}
# """)

# # exe .8 
# sinte = input("please enter a sinte ")
# print(f"""
# upper sinte: {sinte.upper()}
# lower sinte: {sinte.lower()}
# capitalize: {sinte.capitalize()}
# title: {sinte.title()}
# """)

# # exe .9
# sinte = input("please enter a sinte ")
# print(f"""
# sinte: {sinte}
# sinte whitout {sinte.strip()}
# len sinte: {len(sinte)}
# len sinte whitout {len(sinte.strip())}
# """)


# exe .10
# sentence = "I love Java programming"
# sentence = sentence.replace("Java","python")
# print(sentence)
# love = sentence.count("love")
# print(love)
# i = sentence.startswith("I")
# print(i)
# programming = sentence.endswith("programming")
# print(programming)


# # exe .11
# word = "Programming"
# first = word[0]
# last = word[-1]
# threth = word[2]
# tree = word[:3]
# four = word[-4:]
# revers = word[::-1]
# print(word,first,last,threth,tree,four,revers)

# # exe .12
# a = "100"
# b = "25"
# c = 10
# d = 5.5
# print(int(a))
# print(float(b))
# print(str(c))
# print("d cnot convert to int")



# # exe .13
# age = input("Enter your age: ")
# print("print(age + 10) לא יצליח משום שלא ניתן לחבר סטרינג עם מספר")
# print(int(age) + 10)

# # exe .14

# price = input("please enter a price ")
# price = int(price)
# VAT = 0.18
# print(f"price after vat = {price*(1+VAT)}")

# exe .15

# first_name = input("please enter your first name ")
# last_name = input("please enter your last name ")
# age = int(input("please enter your age "))
# salary = int(input("please enter your salary "))
# seniority = int(input("please enter your seniority "))
# print(f"Annual salary {salary*12}")
# print(f"Salary after 5%: {salary*1.05}")
# print(f"Number of characters in full name {len(first_name+last_name)}")

# exe .16
# usd_rate = 3.25
# price = int(input("please enter a price "))
# print(f"your price in dolar is: {price*usd_rate}")
# euro = 3.75
# print(f"your price in euro is: {price*euro} ")
# print(f"""
# your price in dolar after comition is: {price*usd_rate*0.98}
# your price in euro comition is: {price*euro*0.98}
# """)

# exe .17
# first_name = input("please enter your first name ").lower()
# last_name = input("please enter your last name ").lower()
# birth_year = int(input("please enter your birth year "))
# print (f"{first_name}.{last_name}.{birth_year}@gmail.com")


# exe .18
name = input("please enter your name ")
product = input("please enter product ").upper()
price = float(input("please enter a price "))
quantity = int(input("please enter quantity "))
descount_precent = float(input("please enter descount "))
vat = float(input("please enter vat "))
subtotal1 = price*quantity
discount = subtotal1/100*descount_precent
subtotal2 = subtotal1-discount
VAT_Amount = (subtotal2)*(vat/100)
total = subtotal2+VAT_Amount

print(f"""
Customer: {name}
product: {product}
Unit Price: {price}
quantity: {quantity}
Subtotal: {subtotal1}
discount: {discount}
After Discount: {subtotal1-discount}
VAT: {vat}%
VAT Amount {VAT_Amount}
Total: {total}
""")
