def temp_conv(temp: (int, float)) -> (int, float):
    res = temp * 1.8 + 32
    return res
temps = [32, 45, 64, 72, 100, 110, 200, 250]
print(list(map(temp_conv, temps)))

