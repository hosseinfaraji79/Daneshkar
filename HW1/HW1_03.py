user_string = input("please enter something: ")
new_string = ""
vowels = ["a", "e", "i", "u", "o" , "A" , "E" , "I" , "U" , "O"]

for item in user_string:
    if new_string:
        if item in vowels:
            new_string = new_string.replace(item, '.')
        if item.isupper():
            new_string = new_string.replace(item, item.lower())
        if item.islower():
            new_string = new_string.replace(item, item.upper())
    else:
        if item in vowels:
            new_string = user_string.replace(item, '.')
        if item.isupper():
            new_string = user_string.replace(item, item.lower())
        if item.islower():
            new_string = user_string.replace(item, item.upper())


newest_string = new_string.replace(" ", "")

print(newest_string)