# exe .1
# num = 10
# while num > 0:
#     print(num)
#     num-=1

# exe .2
# num = 10
# while num >0:
#     print(num)
#     num -= 1
# print("START!")

# exe .3
# num = 0
# while num <= 50:
#     if num %2 == 0:
#         print(num)
#     num += 1

# exe .4
# num = int(input("please enter a number "))
# range = 1
# while range <=5:
#     print(num*range)
#     range += 1
    
# exe .5
# num = 0
# range = 0
# while range <= 100:
#     num += range
#     range += 1
# print(num)
""
# exe .6
# corrent_password = "python123"
# corect = False
# while corect == False:
#     password = input("please enter your password ")
#     if password == corrent_password:
#         corect = True
# print("Welcome!")    

# exe .7
# secret_number = 27
# corect = False
# while corect == False:
#     num = int(input("please enter a number "))
#     if num == secret_number:
#         corect = True
# print(num)


# exe .8
# is_run = True
# total = 0
# while is_run:
#     num = int(input("please enter a number "))
#     if num == 0:
#         is_run = False
#     else:
#         total += num
# print(total)    


# exe .9
# count = 0
# total = 0
# is_run = True
# while is_run:
#     graed = int(input("please enter a gread "))

#     if graed < 999:
#         total += graed
#         count += 1
#     elif graed == 999:
#         is_run = False
#     else:
#         print("out of range")
# print(f"""
# count: {count}
# total: {total}
# avrage: {total/count}
# """)

# exe .10
# is_run = True
# count = 0
# total = 0
# while is_run:
#     num = int(input("please enter a number "))
#     if num < 0:
#         is_run = False
#     else:
#         count += 1
#         total += num
# print(f"""
# count: {count}
# total: {total}
# """)

# exe .11
# num = int(input("please enter a number "))
# range = 1
# while range <= 10:
#     print(f"{num}x{range} = {num*range}")
#     range += 1

# exe .12
# num = int(input("please enter a number "))
# count = 0
# while num > 0:
#     num = num //10
#     count += 1
# print(f"{count} digits")

# exe .13
# num = int(input("please enter a number "))
# new_num = 0
# while num > 0:
#     digit = num%10
#     new_num = new_num * 10 + digit
#     num = num // 10
# print(new_num)

# exe .14
# num = int(input("please enter a number "))
# range = 2
# while range < num:
#     if num % range == 0:
#         print(f"number {num} is divisible by {range}")
#         break
#     else:
#         range += 1
# else:
#     print(f"number {num} is Prime number")

# exe .15
# balance = 5000
# is_run = True
# while is_run:
#     print("""
# 1. Check balance
# 2. Deposit money
# 3. Withdraw money
# 4. exit
# """)
#     action = input("chooce un option ")
#     if action == "1":
#         print(f"Balance: {balance}")
#     elif action == "2":
#         amount = float(input("please enter how mach yoy wont to deposit "))
#         if amount < 0:
#             print("con't be a negativ number")
#             continue
#         balance += amount
#     elif action == "3":
#         amount = float(input("please enter how mach yoy wont to withdraw "))
#         if amount < 0:
#             print("con't be a negativ number")
#             continue
#         if balance - amount <0:
#             print("withdraw to high")
#         else:
#             balance -= amount
#             print(f"Balance: {balance}")
#     elif action == "4":
#         break
# print(f"Balance {balance}")

# exe .16
# range = 0
# while range <= 200:
#     if range <= 15:
#         print(range)
#         range += 1
#     else:
#         break

# exe .17
# range = 0
# while range <= 200:
#     range += 1
#     if range == 30:
#             break
#     elif range %3 == 0:
#         continue
#     else:
#         print(range)
        

# exe .18
# is_run = True
# while is_run:
#     num = int(input("please enter a number "))
#     if num == 100:
#         print("stop")
#         break


# exe .19
# for i in range(1,21):
#     print(i)

# exe .20
# for i in range(0,100,5):
#     print(i)

# exe .21
# total = 0
# for i in range(101):
#     total += i
# print(total)

# exe .22
# num = int(input("please enter a number "))
# for i in range(1,11):
#     print(i*num)

# exe .23
# num1 = int(input("please enter a number "))
# num2 = int(input("please enter a number "))
# total = 0
# for num in range(num1,num2+1):
#     total += num
# print(f"""
# Start: {num1}
# End: {num2}
# Result: {total}
# """)

# exe .24
# for i in range(101):
#     if i %3 == 0 and i %5 == 0:
#         print(i)

# exe .25
# num1 = int(input("please enter a number "))
# num2 = int(input("please enter a number "))
# for i in range(num1):
#     for j in range(num2):
#         print("*", end="")
#     print()

# exe .26
# for i in range(6):
#     for j in range(i):
#         print("*",end="")
#     print()

# exe .27
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()

# exe .28
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)

# mini project
print("""
===== MATH GAME =====
1. Start Game
2. Exit
""")
corect = 0
while True:
    choose = input("Choose un option ")
    if choose == "1":
        score = 0
        for i in range(1, 11):
            if i == 1:
                Q = "12 + 8"
                correct_answer = 20
            elif i == 2:
                Q = "25 - 9"
                correct_answer = 16
            elif i == 3:
                Q = "6 * 7"
                correct_answer = 42
            elif i == 4:
                Q = "48 / 6"
                correct_answer = 8
            elif i == 5:
                Q = "15 + 27"
                correct_answer = 42
            elif i == 6:
                Q = "100 - 34"
                correct_answer = 66
            elif i == 7:
                Q = "9 * 8"
                correct_answer = 72
            elif i == 8:
                Q = "81 / 9"
                correct_answer = 9
            elif i == 9:
                Q = "19 + 14"
                correct_answer = 33
            else:
                Q = "50 - 23"
                correct_answer = 27
            user_input = int(input(f"Question {i}: {Q} = "))
            if user_input == correct_answer:
                print("correct")
                score += 1
            else:
                print("uncorrect")
        print(score)
    elif choose =="2":
        break        

        









