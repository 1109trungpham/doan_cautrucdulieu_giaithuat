def Sapxep_Chon(array, chieudai):
    for a in range(chieudai):
        index = a

        for b in range(a + 1, chieudai):
            if array[b] < array[index]:
                index = b
                # ở mỗi lần lặp của câu lệnh for trên,
        # sẽ tìm ra chỉ số của phần tử nhỏ nhất (là b)

        # dùng chỉ số b này để đưa phần tử nhỏ nhất vừa tìm được
        # về vị trí đúng của nó
        (array[a], array[index]) = (array[index], array[a])


arr = [4, 13, 6, 9, 77, 3, 62, 1]
length = len(arr)
Sapxep_Chon(arr, length)
print('Dãy sau khi sắp xếp tăng dần \nbằng phương pháp sắp xếp chọn',
      end=": ")
print(arr)