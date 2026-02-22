# Part 1: Input & Output Functions (print & input)


# Question no 1
"""1. Write a program to print "Hello, World!" and your name on two separate lines."""

print("Hello World")
print("Hussnain Saifi")



# Question no 2
"""2. Ask the user for their favorite color using input() and print
"Your favorite color is [color]"."""

Color = input("Please Enter your Favorite color: ")
print(Color)



# Question no 3
"""3. Use a single print() statement to display three different words separated by a hyphen (-)."""

print("Muhammad","Hussnain","Saifi", sep="-")



# Question no 4
"""4. Prompt the user for their birth year and print their age"""

a = int(input("Enter your birth year: "))
b = 2026 - a
print(b)



# Question no 5
"""5. Print the result of 5 + 5 such that the output is:
The sum of 5 and 5 is 10."""

sum = 5 + 5
print("The sum of 5 + 5 = ", sum)



# Question no 6
"""6. Use the end parameter in print() to join two separate print statements with a space."""

print("I am a programmer." ,end =" ")
print("I am learning python")



# Question no 7
"""7. Write a program that takes two strings from the user and prints them joined together."""

s1 = input("Please enter your string 1: ")
s2 = input("Please enter your string 2: ")
print("Your strings are joined: ", s1 + s2)



# Question no 8
"""8. Create a greeting that takes a user's name and prints
"Welcome, [Name]!" in all uppercase."""

Greeting = input("Please enter your name: ")
print("welcome ",Greeting.upper())



# Question no 9
"""9. Ask for a user's city and country, then print them in the format:
"City, Country"""

city = input("Please enter your city: ")
country = input("Please enter your country: ")
print("Your city is:",city , "and Your country is:", country)
 


# Question no 10
"""10. Experiment: What happens if you try to add a string and an integer in a print statement?
Write a code snippet that fixes this using str()."""

ex = str(input("hussnain""1234"))
print(ex)

