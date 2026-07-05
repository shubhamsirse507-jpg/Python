ptr = ""

for i in range(1, 8):
    for j in range(1, 6):
        if i == 1 or i == 4 or i == 7 or (j == 1 and i <= 4) or (j == 5 and i >= 4):
            ptr += "*"
        else:
            ptr += " "
    ptr += "\n"

print(ptr)