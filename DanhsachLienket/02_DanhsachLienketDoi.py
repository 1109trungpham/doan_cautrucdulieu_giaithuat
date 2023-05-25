# 02 Khởi tạo Danh sách liên kết Đôi

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None  # đại diện cho node tiếp theo trong danh sách
        self.prev = None  # đại diện cho node trước đó trong danh sách


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next


def main():
    danhsach_kep = DoublyLinkedList()

    node01 = Node("Bá Trung")
    node02 = Node("Thanh Đức")
    node03 = Node("Hoàng Việt")
    node04 = Node("Trọng Nghĩa")

    danhsach_kep.head = node01
    node01.next = node02
    node02.next = node03
    node03.next = node04

    danhsach_kep.display()


if __name__ == '__main__':
    main()