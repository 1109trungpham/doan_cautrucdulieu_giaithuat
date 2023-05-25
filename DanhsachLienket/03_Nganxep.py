# Stack theo mảng

stack = []

stack.append('A')  # sử dụng append() để thêm các phần tử theo thứ tự
stack.append('B')  # A thêm vào trước, đến B và cuối cùng là C
stack.append('C')
stack.append('D')

print("stack ban đầu:", stack)   # in list gồm 4 phần tử trên ra màn hình

print("phần tử bị xoá:", stack.pop())
print("phần tử bị xoá:", stack.pop())

# sử dụng pop() để xoá phần tử
# nếu không ghi vị trí cho pop()
# thì hàm này mặc định xoá phần tử cuối cùng của list

print("stack sau khi pop():", stack)
# in ra màn hình list sau khi pop()