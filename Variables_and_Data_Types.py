# exe .1

first_name = "shay"
last_name = "deree"
age = 26
city = "Petah Tikva"
email = "ahsr4562@gmail.com"


print(f"""
===========================
      User Details
===========================
First Name: {first_name}
Last Name: {last_name}
Age: {age}
City: {city}
Email: {email}
""")


# exe .2
birth_year = 2000
current_year =2026
print(f"Age: {current_year-birth_year}")


# exe .3
width = 10
height = 20
print(f"Area: {width*height}")
print(f"Perimeter: {width*2 + height*2}")

# exe .4 
name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500
print(f"""
Name: {name}       Type: {type(name)}
Age: {age}           Type: {type(age)}
Height: {height}      Type: {type(height)}
Is_student: {is_student}  Type: {type(is_student)}
Salary: {salary}      Type: {type(salary)}
""")

# exe .5
first_name = input("please enter your name ")
last_name = input("please enter your last name ")
city = input("please enter your city ") 
age = int(input("please enter your age "))
print(f"""
Name: {first_name} {last_name}
City: {city}
Age: {age}
""")

# exe .6
num_1 = int(input("please enter a number "))
num_2 = int(input("please enter a number "))
print(f"""
Addition {num_1} + {num_2} = {num_1 + num_2}
Subtraction {num_1} - {num_2} = {num_1 - num_2}
Multiplication {num_1} * {num_2} = {num_1 * num_2}
Division {num_1} / {num_2} = {num_1 / num_2}
 """)


# exe .7
product = input("please enter product name ")
cost = int(input("please enter the product cost "))
quantity = int(input("please enter quantity "))
print(f"""
====== Purchase Receipt ======
Product: {product}
Price: {cost}
Quantity: {quantity}
Total: {cost*quantity}
""")

# exe .9
name = input("please enter the employee name ")
hours = int(input("please enter how mach hours "))
price_for_hour = int(input("please enter prise for hour "))
print(f"""
=======salary======
name: {name}
hours: {hours}
price for hour: {price_for_hour}
salary: {price_for_hour*hours}
""")

# exe .10
pay = int(input("please enter price to pay "))
tip = int(input("please enter the tip precent "))
pepole = int(input("please enter how many pepole "))
print(f"""
========Bill========
Tip: {pay/100*tip}
Total: {pay-(pay/100*tip)}
Price per diner: {(pay-(pay/100*tip))/pepole}
""")

# exe .12
a = 10
b = 20
c = a
a = b
b = c
print(a,b)


# exe: final_practic
first_name = input("please enter your name ")
last_name = input("please enter your last name ")
age = int(input("please enter your age "))
school_name = input("please enter the school name ")
course_name =  input("please enter the course name ")
month = int(input("please enter how long the course"))
price_for_month = int(input("please enter price for month "))

print(f"""
================================
       STUDENT REGISTRATION
================================

Student: {first_name} {last_name}
Age: {age}
Institution: {school_name}
Course: {course_name}
Duration: {month} month
Monthly Price: {price_for_month}

Total Course Price: {price_for_month*month}

================================
    Registration completed!
================================
""")