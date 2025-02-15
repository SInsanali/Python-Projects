# #NOTE function
# def my_function():
#     #do this
#     #then do this
# my_function()

# #NOTE function with inputs
# def my_function(something):
#     #do this with something
#     #then do this
# my_function(123)

# #NOTE function with output
# def my_function():
#     result = 3 * 2
#     return result

# #NOTE practice using return

# def format_name(f_name, l_name):
#     #capitalize the first letter
#     f_name = f_name.title()
#     l_name = l_name.title()
#     #return the title case input
#     return f"{f_name} {l_name}"

# #user input
# first_name = str(input("What is your first name?\n"))
# last_name = str(input("What is your last name?\n"))

# #assign function to var
# formated_string = format_name(first_name, last_name)

# print(formated_string)


#NOTE practice using multiple returns

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "blank entry"
    #capitalize the first letter
    f_name = f_name.title()
    l_name = l_name.title()
    #return the title case input
    return f"{f_name} {l_name}"

#user input
first_name = str(input("What is your first name?\n"))
last_name = str(input("What is your last name?\n")) 

#assign function to var
formated_string = format_name(first_name, last_name)

print(formated_string)
