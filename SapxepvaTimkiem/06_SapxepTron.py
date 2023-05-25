def Sapxep_Tron(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # tìm phần giữa của mảng
        L = arr[:mid]  # để chia thành 2 nửa
        R = arr[mid:]
        Sapxep_Tron(L)  # sắp xếp nửa bên trái
        Sapxep_Tron(R)  # sắp xếp nửa bên phải

        i = j = k = 0

        # sao chép dữ liệu vào các mảng tạm thời L[], R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # kiểm tra xem còn phần tử nào không
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]

    Sapxep_Tron(arr)
    print('Dãy sau khi sắp xếp tăng dần \nbằng phương pháp sắp xếp trộn',
          end=": ")
    printList(arr)