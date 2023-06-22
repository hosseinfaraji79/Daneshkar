user_input = input("please enter something: ")
uniq_chars = set(user_input)
result = {}
for i in uniq_chars:
    result[i] = user_input.count(i)

print(result)