# 01 Khởi tạo Danh sách liên kết Đơn

# Node class
class Node:

    def __init__(self, Data):
        self.data = Data  # khởi tạo phần chứa dữ liệu
        self.next = None  # khởi tạo phần chứa tham chiếu của node tiếp theo


# Linked List class
class LinkedList:

    def __init__(self):
        self.head = None  # khởi tạo node head là None (chưa có dữ liệu)

    def print(self):  # phương thức in ra màn hình của Class

        tui = self.head

        while (tui != None):
            print(tui.data)

            tui = tui.next

def main():
    danhsach = LinkedList()  # tạo danh sách trống

    node01 = Node("Bá Trung")  # tạo các node
    node02 = Node("Thanh Đức")
    node03 = Node("Hoàng Việt")
    node04 = Node("Trọng Nghĩa")

    danhsach.head = node01  # đưa node vào danh sách liên kết
    node01.next = node02
    node02.next = node03
    node03.next = node04
    danhsach.print()  # sử dụng phương thức print()
    # để in danh sách liên kết ra màn hình


if __name__ == '__main__':
    main()