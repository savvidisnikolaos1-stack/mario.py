while True:
    try:
        height = int(input("შეიყვანეთ სიმაღლე (1-8): "))
    except ValueError:
        print("გთხოვთ შეიყვანოთ მთელი რიცხვი")
        continue

    if 1 <= height <= 8:
        break
    print("რიცხვი უნდა იყოს 1-დან 8-მდე")


for row in range(1, height + 1):
    
    for _ in range(height - row):
        print(" ", end="")
    
    for _ in range(row):
        print("#", end="")
    
    print()