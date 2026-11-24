# exe .1
# nums =[10,20,30,40,50]
# print(nums)
# print(nums[0])
# print(nums[-1])
# print(nums[2])

# exe .2
# names = ["shay","avi","kobi","beni"] 
# print(names)
# print(len(names))
# print(names[0],names[-1])
# names[1] = "dani"
# print(names)


# exe .3
# grads = [95,48,69,47,85]
# print(grads)
# grads.append(68)
# grads.insert(0,84)
# grads[2] = 85
# print(grads)

# exe .4
# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums)
# nums.pop(0)
# print(nums)
# nums.pop()
# print(nums)
# nums.pop(2)
# print(nums)


# exe .5
# products = ["laptop", "mouse", "keyboard", "monitor", "headphones"]
# if "laptop" in products:
#     print('yes')
# if not "fd" in products:
#     print("no")

# exe .6
# nums = [1,2,3,4,5,6,7,8,9,10]
# for num in nums:
#     print(num)

# exe .7
# nums = [1,2,3,4,5,6,7,8,9,10]
# for num in nums:
#     if num %2 == 0:
#         print(num)


# exe .8
# grads = [95,48,69,47,85]
# total = 0
# for grad in grads:
#     total += grad
# print(total)

# exe .9
# grads = [95,48,69,47,85]
# highest  = 0
# for grad in grads:
#     if grad > big:
#         big = grad
# print(big)

# exe .10
# products = ["laptop", "mouse", "keyboard", "monitor", "headphones"]
# u_product = input("please enter a product ")
# for product in products:
#     if product == u_product:
#         print("Found")
#         break
# else:
#     print("Not Found")

# exe .11
# nums = [1,2,3,4,5,6,7,8,9,10]
# u_num = int(input("please enter a number "))
# for i in range(len(nums)):
#     if nums[i] == u_num:
#         print(f"your num {u_num} in index {i}")

# exe .12
# nums = [10,50,40,60,80,70,90,20,30,51]
# count = 0
# for num in nums:
#     if num > 50:
#         count += 1
# print(count)


# exe .13
# nums = [1,2,3,4,5,6,7,8,9,10]
# even = []
# for num in nums:
#     if num %2 == 0:
#         even.append(num)
# print(even)


# exe .14
# products = ["laptop", "mouse", "keyboard", "monitor", "headphones"]
# index = 0
# is_run = True
# while is_run:
#     print(products[index],index)
#     if index == len(products)-1:
#         is_run = False
#     else:
#         index += 1

# exe .15
# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums[:3])
# print(nums[-3:])
# print(nums[2:6])
# print(nums[::-1])

# exe .16
# names = ["Liam","Olivia","Noah","Emma","Oliver","Charlotte","James","Amelia","Elijah","Sophia"]
# print(names[::2])
# print(names[1::2])
# print(names[::-1])

# exe .17
# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# first_nams = nums[:10]
# last_nums = nums[10:]
# i_5_14 = nums[5:14]
# print(first_nams)
# print(last_nums)
# print(i_5_14)

# exe .18
# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# first_nams = nums[:10]
# last_nums = nums[10:]
# print(first_nams)
# print(last_nums)

# exe .19
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# duble_nums = [num*2 for num in nums]
# print(duble_nums)
# times_nums = [num**2 for num in nums] 
# print(times_nums)
# even_nums = [num for num in nums if num %2 == 0]
# print(even_nums)
# big_5 = [num for num in nums if num > 5]
# print(big_5)

# exe .20
# grades = [55, 90, 67, 100, 45, 82, 73, 30]
# big_60 = [grad for grad in grades if grad > 60]
# print(big_60)
# low_60 = [grad for grad in grades if grad < 60]
# print(low_60)
# grad_plus_5 = [grad+5 for grad in grades]
# print(grad_plus_5)

# exe .21
# names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]
# long_names = [name for name in names if len(name) > 4]
# print(long_names)
# upper_names = [name.upper() for name in names]
# print(upper_names)
# d_names = [name for name in names if name.startswith("D")]
# print(d_names)

# exe .22
# nums = [12, 7, 25, 30, 9, 44, 18, 3]
# new_nuns = [num for num in nums if num %3 == 0 and num > 10]
# print(new_nuns)

# exe .23
# count = 1
# nums = []
# biger = 0
# while count <= 10:
#     num = int(input("please enter a number "))
#     nums.append(num)
#     count += 1
# for num in nums:
#     if num > biger:
#         biger = num
# lower = biger
# for num in nums:
#     if num < lower:
#         lower = num
# avrage = sum(nums) / len(nums)
# print(nums)
# print(biger)
# print(lower)
# print(avrage)

# exe .24
# names = ["Moshe", "David", "Dana", "Noa", "Michael"]
# u_name = input("lease enter a name ").capitalize()
# if u_name in names:
#     names.remove(u_name)
# else:
#     print("the name not in list")
# print(names)

# exe .25
# nums = [1,5,9,4,6,8,12,75,19,34,68,64,15,8784,3449]
# even_nums = [num for num in nums if num %2 == 0] 
# odd_nums = [num for num in nums if num %2 != 0]
# biger_20 = [num for num in nums if num > 20]
# print(even_nums)
# print(odd_nums)
# print(biger_20)

# exe .26
# nums = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3]
# u_num  =int(input("please enter a number "))
# indexes =[]
# for i,num in enumerate(nums):
#     if num == u_num:
#         indexes.append(i)
# if len(indexes) == 0:
#     print("number not found")
# else:
#     print(f"location: {indexes} count: {len(indexes)}")

# exe .27
# nums = [1,2,3,4,5,6]
# n_nums = [7,8,9,10,11,12]
# for num in n_nums:
#     nums.append(num)
# print(nums)
# print(nums[:5])
# print(nums[-5::])
# print(nums[::-1])

# exe .28
# nums = [1,2,3,4,5,6]
# u_num = int(input("please enter a number "))
# for num in nums:
#     if num == u_num:
#         break
# else:
#     nums.append(u_num)
# print(nums)

# mini project
grades = [85, 72, 90, 55, 100, 63, 48, 77]
is_run = True
while is_run:
    print("""
===== Grades Management =====
1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
0. Exit
""")
    chooise = input("please emter an option ")
    if chooise == "1":
        for grade in grades:
            print(grade)
    elif chooise == "2":
        u_grade = int(input("please emter a grade "))
        grades.append(u_grade)
    elif chooise == "3":
        u_grade = int(input("please emter a grade "))
        indexes =[]
        for i,grade in enumerate(grades):
            if grade == u_grade:
                indexes.append(i)
        if len(indexes) == 0:
            print("number not found")
        else:
            print(f"location: {indexes}")
    elif chooise == "4":
        u_grade = int(input("please emter a grade "))
        for grade in grades:
            if grade == u_grade:
                grades.remove(grade)
                print(grades)
                break
        else:
            print(f"grade {u_grade} is not found")
    elif chooise == "5":
        big_60 = [grade for grade in grades if grade > 60]
        print(big_60)
    elif chooise == "6":
        low_60 = [grade for grade in grades if grade < 60]
        print(low_60)
    elif chooise =="7":
        highest = 0
        lowest = 100
        for grade in grades:
            if grade > highest:
                highest = grade
            if grade < lowest:
                lowest = grade
        print(f"the highest: {highest} the lowest: {lowest}")
    elif chooise == "8":
        if len(grades) == 0:
            print("no grades")
        else:
            print(sum(grades) / len(grades))    
    elif chooise == "9":
        print(grades[:3])
    elif chooise == "10":
        print(grades[::-1])
    elif chooise == "0":
        break
    else:
        continue




