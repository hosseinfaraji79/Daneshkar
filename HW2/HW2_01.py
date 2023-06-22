def postalcode_check(code: str) -> bool:

    if len(code) != 11 or code[5] != "-":
        return False
    for char in code:
        if char not in "0123456789-":
            return False
    return True

codes = ["alieotehdkf", "12345-67890", "34987-89325", "r46522-79879234", "2875345235738", "49812-02784", "7989f-38542"]
res = [item for item in codes if postalcode_check(item)]
print(res)