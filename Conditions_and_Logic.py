# exe .1
# age = int(input("please enter your age "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# exe .2
# num = int(input("please enter a number "))
# if num == 0:
#     print("Zero ")
# elif num > 0:
#     print("Positive ")
# elif num < 0:
#     print("Negative ")

# exe .3
# num = int(input("please enter a number "))
# if num % 2 == 0:
#     print("Even")
# elif num %2 != 0:
#     print("odd")

# exe .4
# num1 = int(input("please enter a number "))
# num2 = int(input("please enter a number "))
# if num1 > num2:
#     print(num1)
# elif num1 < num2:
#     print(num2)
# elif num1 == num2:
#     print("the nums is eqwal")

# exe .5
# password = "Python123"
# u_password = input("please enter your password ")
# if u_password == password:
#     print("Access Granted")
# else:
#     print("Access Denied")

# exe .6
# num = int(input("please enter a number "))
# if num ==0 or num > 100:
#     print("מחוץ לטווחים שהוגדרו")
# elif 1 < num <= 10:
#     print("בין 1 ל-10")
# elif num <= 50:
#     print("בין 11 ל-50")
# elif num <= 100:
#     print("בין 51 ל-100")

# exe .7
# gread = int(input("please enter a gread "))
# if 0 > gread or gread > 100:
#     print("Invalid Grade")
# elif gread < 60:
#     print("Failed")
# elif gread < 70:
#     print("Passed")
# elif gread < 80:
#     print("Good")
# elif gread < 90:
#     print("Very Good")
# elif gread <=100:
#     print("Excellent")

# exe .8
# correct_username = "admin"
# correct_password = "123456"
# username = input("please enter username ")
# password = input("please enter password ")
# if username == correct_username and password == correct_password:
#     print("Login Successful")
# elif username == correct_username:
#     print("Wrong Password")
# elif password == correct_password:
#     print("Unknown User")
# else:
#     print("you absulutly wrong")

# exe .9
# age = int(input("please enter your age "))
# price = int(input("please enter the price "))
# if 18 <= age < 60:
#     print(price)
# elif age >= 60:
#     print(price*0.8)
# elif age < 18:
#     print(price*0.9)

# exe .10
# num = int(input("please enter a number "))
# if num %3 != 0 and num %5 != 0:
#     print("לא מתחלק לא ב3 ולא ב5")
# elif num %3 == 0 and num %5 == 0:
#     print("מתחלק גם ב3 וגם ב5")
# elif num % 3 == 0:
#     print("מתחלק ב3")
# elif num %5 == 0:
#     print("מתחלק ב5")


# exe .11
# age = int(input("please enter your age "))
# addolt = input("האם יש איתך מבוגר? True/False ").capitalize()
# if age < 18:
#     if age >= 16 and addolt == True:
#         print("Access Granted")
#     else:
#         print("Access Denied")
# else:
#     print("Access Granted")


# exe .12
# gread = float(input("please enter your gread"))
# salary = float(input("please enter your salary "))
# if gread >= 90:
#     print("זכאי")
# else:
#     if gread >= 85 and salary < 5000:
#         print("זכאי")
#     else:
#         print("לא זכאי")


# exe .13
# correct_username = "admin"
# correct_password = "123456"
# is_active = True
# username = input("please enter username ")
# password = input("please enter password ")
# if password == correct_password and password == correct_password and is_active == True:
#     print("Access Granted")
# else:
#     print("Access Denied")


# exe .14
# num = int(input("please enter a number "))
# if 20 <= num <= 80:
#     print("בטווח")
# else:
#     print("לא בטווח")

# num = int(input("please enter a number "))
# if not 80 >= num >=20:
#     print("לא בטווח")
# else:
#     print("בטווח")


# exe .15
# balance = 5000
# amount = float(input("please enter amount for withdrawal "))

# if amount >= 0:
#     if balance-amount >= 0:
#         balance -= amount
#         print(f"balance = {balance}")
#     else:
#         print(f"amount > balance")
# else:
#     print("amount < 0")


# exe .16
# age = int(input("please enter your age "))
# club_card = input("ההאם יש כרטיס מועדון? True/False ").capitalize()
# if age < 12:
#     if club_card == True:
#         print("child: 22.5")
#     else:
#         print("child: 25")
# elif age <18:
#     if club_card == True:
#         print("youngster: 31.5")
#     else:
#         print("youngster: 35")
# else:
#     if club_card == True:
#         print("adult : 45")
#     else:
#         print("adult : 50")


# exe .17
# age = int(input("please enter your age "))
# salary = int(input("please enter your salary "))
# seniority_month = int(input("please enter your seniority "))
# if age < 21:
#     print("to yang")
# else:
#     if salary >= 7000:
#         print("rich")
#     else:
#         if seniority_month < 12:
#             print("junior")
#         else:
#             print("זכאי")


# exe .18
# kind = input("please enter your kind of vehicle ")
# if kind == "motorsicle":
#     price = 10
# elif kind == "car":
#     price = 20
# elif kind == "truck":
#     price = 30
# hours = int(input("plrase enter hours "))
# if hours <= 1:
#     print(price*hours*0.9)
# elif hours <5:
#     print(price*hours)
# else:
#     print(price*hours*0.85)

# exe .19
# action = input("please enter an action ")
# if not action in ["+","-","*","/"]:
#     print(f"action {action} is not recninaze")
# num1 = int(input("please enter a number "))
# num2 = int(input("please enter a number "))
# if action == "+":
#     print(num1+num2)
# elif action == "-":
#     print(num1-num2)
# elif action == "*":
#     print(num1*num2)
# elif action == "/":
#     if num2 == 0:
#         print("ZeroDivisionError")
#     else:
#         print(num1/num2)


# exe .20
# yaer = int(input("please enter an year "))
# if yaer %400 == 0:
#     print("Leap year")
# else:
#     if yaer %4 == 4 and not yaer %100 == 0:
#         print("Leap year")
#     else:
#         print("Non-leap year")

# exe .21
# hours = int(input("please enter hours"))
# if hours <= 182:
#     salary = hours*50
#     print(salary)
# elif hours <= 184:
#     salary = 182*50
#     hours-=182
#     salary += hours*62.5
#     print(salary)
# else:
#     salary = 182*50
#     salary += 2*62.5
#     hours-=184
#     salary += hours*75
#     print(salary)


# mini_project
age = int(input("please enter your age "))
price = int(input("please enter a price "))
club_card = input("האם יש כרטיס מועדון) yes/no ")
is_it_open = input("האם המוצר נפתח? yes/no ")
reception = input("האם יש קבלה? yes/no ")
days = int(input("please enter how long from the sale "))
if reception == "no":
    print("אין החלפה בלי קבלה")
if is_it_open == "yes":
    print("אין החלפה למוצר פתוח")
if price <= 0:
    print("סכןם רכישה חייב להיות גדול מ0")
if days > 14:
    if club_card == "yes" and days <= 30:
        print(f"זכאי להחזר בסכום: {price}")
    else:
        print("to far from sale day")