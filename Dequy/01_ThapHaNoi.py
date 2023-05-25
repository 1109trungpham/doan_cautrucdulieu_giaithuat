# 01 Đệ quy Tháp Hà Nội

def ThapHaNoi(n, nguon, dich, trunggian):
    if n == 1:
        print("Di chuyển đĩa 0 từ cột nguồn", nguon, "đến cột nhận", dich)
        return

    ThapHaNoi(n - 1, nguon, trunggian, dich)

    print("Di chuyển đĩa", n, "từ cột nguồn", nguon, "đến cột nhận", dich)

    ThapHaNoi(n - 1, trunggian, dich, nguon)


n = 4
ThapHaNoi(n, 'A', 'B', 'C')