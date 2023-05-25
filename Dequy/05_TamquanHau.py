# 05 Đệ quy Tám quân Hậu

SL = int(input("Nhập số lượng quân Hậu: "))

# tạo bàn cờ Vua ma trận size (SLxSL)
# với tất cả phần tử có giá trị = 0
board = [[0] * SL for m in range(SL)]

def attack(i, j):
    # kiểm tra hàng ngang và hàng dọc
    for k in range(0, SL):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # kiểm tra đường chéo
    for k in range(0, SL):
        for g in range(0, SL):
            if (k + g == i + j) or (k - g == i - j):
                if board[k][g] == 1:
                    return True

    # True được trả về khi
    # có quân Hậu khác nằm trên đường đi của ta
    return False
# False được trả về khi
# vị trí (i,j) đã hợp lệ

def N_queens(n):  # n = SL = số lượng quân hậu cần sắp xếp
    if n == 0:
        return True

    for i in range(0, SL):
        for j in range(0, SL):

            if (not (attack(i, j))) and (board[i][j] != 1):
                # not(attack(i,j)) = attack(i,j) return False,
                # tức là vị trí (i,j) hợp lệ

                # board[i][j] khác 1, để kiểm tra xem vị trí (i,j)
                # có bị trùng với các vị trí trước đó không

                # nếu 2 điều kiện trên đều đúng,
                # thì đánh dấu vị trí (i,j) = 1
                board[i][j] = 1

                if N_queens(n - 1) == True:
                    return True

                board[i][j] = 0
    return False

N_queens(SL)
for b in board:  # in kết quả ra màn hình
    print(b)