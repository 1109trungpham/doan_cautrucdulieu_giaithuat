def Sapxep_Chen(arr):
    for i in range(1, len(arr)):  # i là chỉ số của phần tử
        # chúng ta bắt đầu thuật toán với
        # phần tử thứ 2 của dãy nên i chạy từ 1
        # chứ không phải từ 0

        key = arr[i]  # key là giá trị của phần tử cần sắp xếp
        # lấy key so sánh với các phần tử bên trái nó
        j = i - 1

        while j >= 0 and arr[j] > key:
            # arr[j] là phần tử liền kề bên trái của key
            # j sẽ giảm dần khi điều kiện while đúng để
            # so sánh key với các phần tử bên trái nó

            arr[j + 1] = arr[j]
            # [j+1] hiểu là vị trí tạm thời của key
            # nếu arr[j] > key thì key sẽ nhường chỗ

            j -= 1

        arr[j + 1] = key  # khi điều kiện while sai
        # tức là lúc arr[j] < key
        # thì key sẽ được chèn vào vị trí liền kề bên phải arr[j]
        # tức arr[j+1] = key


# ghi chú: key sẽ di động và nhường chỗ cho các phần tử khác
# cho đến khi nó tìm được vị trí thích hợp để chèn vào


arr = [14, 5, 6, 1, 0, 28, 12]
Sapxep_Chen(arr)
print('Dãy sau khi sắp xếp tăng dần \nbằng phương pháp sắp xếp chèn',
      end=": ")
print(arr)