# 04 Đệ quy Hành trình quân Mã

n = 8
# hàm Kiemtra - Nó kiểm tra xem nước đi có nằm trong bàn cờ hay không?
def Kiemtra(x, y, board):
    # x, y là toạ độ của quân Mã trong bàn cờ ma trận n x n (xét bàn cờ 8 x 8)
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False

# hàm tính nước đi của quân Mã
def NuocdiTieptheo(board, curr_x, curr_y, move_x, move_y, pos):
    if (pos == n ** 2):
        return True

    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        # toạ độ mới = toạ độ hiện tại + cách di chuyển
        # toạ độ mới sẽ được thay xuống hàm Kiemtra phía dưới,
        # để kiểm tra xem có hợp lệ,
        # tức có nằm trong bàn cờ hay không?

        if (Kiemtra(new_x, new_y, board)):

            board[new_x][new_y] = pos  # đánh dấu vị trí đã đến (new) = pos
            # pos này được hiểu là thứ tự nước đi,
            # nên nó sẽ +1 sau mỗi lần lặp

            if (NuocdiTieptheo(board, new_x, new_y, move_x, move_y, pos + 1)):
                return True
            board[new_x][new_y] = -1
    return False

# hàm xuất ra màn hình hành trình (hay thứ tự nước đi) của quân Mã
def Giaiphap(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

def main():  # Chương trình chính

    # tạo bàn cờ ma trận tỉ lệ n x n,
    # với các phần tử ma trận đều mang giá trị là -1
    board = [[-1 for i in range(n)] for i in range(n)]

    board[4][0] = 0  # Mã ở vị trí (4,0) trong ma trận,
    # gán cho nó = 0 vì đây là vị trí xuất phát

    pos = 1  # pos đánh dấu thứ tự của nước đi của Mã

    # toạ độ di chuyển (cách di chuyển) của quân Mã
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    if (not NuocdiTieptheo(board, 4, 0, move_x, move_y, pos)):
        print("Giải pháp không tồn tại")
    else:
        Giaiphap(board)

if __name__ == "__main__":
    main()