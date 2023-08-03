# ----------- Q1 -----------
name = input("Enter your name: ")
age = int(input("Enter your age: "))
street = input("Enter your street address: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

# ----------- Q2 -----------
print(f''' 
"Name: {name}"
"Age: {age}"
"Address: {street}, {city}, {country}"
\n''')

# ----------- Q3 -----------
print(f''' "Hello {name} Your age is {age} Years Old, Your Address is {street}, {city}, {country}." \n''')

# ----------- Q4 -----------
print(f"{type(name)} {type(age)} \n{type(street)} {type(city)}\n\t{type(country)}")

# ----------- Q5 -----------
print(f''' "Hello '{name}', How Are You? \ """ Your Age Is "{age}"" + And Your Country Is: {country}''')

# ----------- Q6 -----------
print(f''' "Hello '{name}', How Are You? \ \n """ Your Age Is "{age}"" + And \nYour Country Is: {country}''')

# ----------- Q7 -----------
name_ = 'Doaa Reem'
print(name_[0])  # D
print(name_[2])  # a
print(name_[len(name_) - 1])  # or name_[-1] #m

# ----------- Q8 -----------
print(name_[6:])  # eem
print(name_[:4])  # Doaa
print(f"{name_[2:4].capitalize()}{name_[4:7]}")  # Aa Re
print(name_[:4:-1])  # meeR
print(name_.split()[0][::2], name_.split()[1][::2])  # Da Re

# ----------- Q9 -----------
print("$&$&Mohammed$&$&".strip('$&'))  # Mohammed

# ----------- Q10 -----------
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7', 'Love'))  # I Love Python And Although I Love  GSG with Zakaria

# ----------- Q11 Bonus (+2 Marks)-----------
print('''\nWhat is the difference between (title) and (capitalize) methods? (give me 2 examples to clarify the point)

                                                =========== title() ===========
function is used to convert an input string to a title case That Mean converting the first alphabet of each word to uppercase and the rest into lowercase.
    FX: txt = 'DoAa loVe PYthon' : txt.title() ==> txt = 'Doaa love Python
    Hint:^_^
        1- The initial letter following any number or special character (such as an apostrophe) is changed to an upper-case letter because are treated as a word boundary
        2- Ignore Numbers.
            FX: txt = 'What's YOur NAMe ? 22 Year' : txt.title() ==> tx= 'What'S Your Name ? 22 Year ''')

ex_1 = "#upSkilling"
print(ex_1.capitalize(), '         capitalize()')  # If The First Index was a Symbol Or Number Not Ignore So Ignore
# Make Upper The Letter In Next Index
print(ex_1.title())  # Make Upper For First Letter and Symbol Or Number before it is ignored

ex_2 = "What'S Your Name ? 22 Year "
print(ex_2.capitalize())  # Just Make upper for First Letter for first word in Statement
print(ex_2.title())  # make upper for first letter for any word in Statement

# ----------- Q12 Bonus (+2 Marks)-----------
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))

# ----------- Q13 Bonus (+2 Marks)-----------
first_name = "Doaa"
print('{:*^26}'.format(first_name))
print('{:*>15}'.format(first_name))
print('{:*<15}'.format(first_name))

# ----------- Q14 Bonus (+2 Marks)-----------
name_one = "HaLA"
name_two = "shaHD"
print(name_one.swapcase())  # hAla
print(name_two.swapcase())  # SHAhd
print(name_one.lower())  # hala
print(name_two.upper())  # SHAHD

# ----------- Q15 Bonus (+2 Marks)-----------
print('''How can we Check if name_one contains Only Upper Case letters, and name_two contains Only Lower Case letters? 
            by islower(), isupper() Functions 
                FX: print('doaa'.islower())''', 'doaa'.islower(),
      '''\n print('doaa'.isupper())''', 'doaa'.isupper(),
      '''\n print('Doaa'.islower())''', 'Doaa'.islower(),
      '''\n print('Doaa'.islower())''', 'Doaa'.islower())

# ----------- Q16 Bonus (+2 Marks)-----------
name_one = "HaLA"
name_two = "shaHD"
print(name_one[0] == 'S')
print(name_two[3:5] == 'HD')
# bBut of course there are more sophisticated ways than this ^_*

# ----------- Q17 Bonus (+2 Marks)-----------
msg_ = "I Love Python And Although I Love GSG with Zakaria"
# lst_msg = msg_.split()
print(f' (Love) ==> appears {msg_.split().count("Love")} times')
print(f' (Love) ==> appears {msg_.count("t")} times')

# ----------- Q18 Bonus (+2 Marks)-----------
name_18 = "Zakaria"
print(name_18.index("r"))

# ----------- Q19 Bonus (+2 Marks)-----------
msg = "I %7 Python And Although I %7 GSG with Zakaria"
msg = msg.split()  # Convert To List
msg[1] = 'Love'  # Replace The First %7 To 'Love'
msg = ' '.join(msg)  # Return msg To String After Replacing
print(msg)

