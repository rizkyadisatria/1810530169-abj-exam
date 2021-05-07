file = open("db-inventory.txt", "a")
while True:
    newItem = input("Input data inventory baru (ya/tidak)? ")
    if newItem == "tidak":
        break
    file.write(newItem + "\n")
file.close()