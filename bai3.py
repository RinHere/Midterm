def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

while True:
    try:
 
        input_str = input("Nhập dãy số nguyên, cách nhau bởi dấu cách (nhập 'exit' để thoát): ")
        if input_str.lower() == 'exit':
            print("Kết thúc chương trình.")
            break
        
        arr = list(map(int, input_str.split()))
        print("Mảng ban đầu:", arr)

    
        bubble_sort(arr)
        print("Mảng sau khi sắp xếp:", arr)

    except ValueError:
        print("Nhập một dãy số nguyên hợp lệ!")
