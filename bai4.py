def fibonacci(n):
    if n < 0:
        return "Nhập số nguyên không âm."
    
    fib = [0, 1]  
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])  
    
    return fib[n]

while True:
    try:
        n = int(input("Nhập một số nguyên không âm n (nhập -1 để thoát): "))
        if n == -1:
            print("Kết thúc chương trình.")
            break
        if n < 0:
            print("Nhập số không âm!")
        else:
            print(f"F({n}) = {fibonacci(n)}")
    except ValueError:
        print("Nhập một số nguyên hợp lệ!")
