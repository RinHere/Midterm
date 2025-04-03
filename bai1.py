import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        n = int(input("Nhập một số nguyên dương (nhập 0 để thoát): "))
        if n == 0:
            print("Kết thúc chương trình.")
            break
        if is_prime(n):
            print(f"{n} là số nguyên tố.")
        else:
            print(f"{n} không phải là số nguyên tố.")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
