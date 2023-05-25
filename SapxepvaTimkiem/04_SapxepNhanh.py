def Vach_ngan(array, low, high):
    pivot = array[high]  # chọn phần tử ngoài cùng bên phải làm trục

    i = low - 1

    for j in range(low, high):

        if array[j] <= pivot:
            # khi tìm ra được chỉ số j của phần tử nhỏ hơn (hoặc bằng) trục thì
            # hoán đổi vị trí phần tử [j] và phần tử [i]
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

        # sau khi j chạy hết vòng lặp sẽ tìm ra được một số
    # số này là chỉ số của phần tử có độ lớn nằm giữa của dãy (hiểu như vách ngăn)
    # bên phải nó là các phần tử lớn hơn nó
    # bên trái nó là các phần từ nhỏ hơn nó
    # dùng chỉ số này để đệ quy sắp xếp 2 khoảng bên trái và bên phải

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1


def quicksort(array, low, high):
    if low < high:
        pi = Vach_ngan(array, low, high)

        # Đệ quy phần bên trái vách ngăn
        quicksort(array, low, pi - 1)

        # Đệ quy phần bên phải vách ngăn
        quicksort(array, pi + 1, high)


if __name__ == '__main__':

    array = [8, 4, 3, 1, 9, 2, 5]
    N = len(array)

    quicksort(array, 0, N - 1)

    print('Dãy sau khi sắp xếp tăng dần \nbằng phương pháp sắp xếp nhanh',
          end=": ")
    for x in array:
        print(x, end=" ")