def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    giai_thua = 1
    for i in range(2, n + 1):
        giai_thua *= i
    return giai_thua

while True:
    try:
        n = int(input("Nhập một số nguyên không âm (nhập -1 để thoát): "))
        if n == -1:
            print("Kết thúc chương trình.")
            break
        if n < 0:
            print("Nhập một số **không âm**.")
        else:
            print(f"{n}! = {tinh_giai_thua(n)}")
    except ValueError:
        print("Nhập một số nguyên hợp lệ!")
