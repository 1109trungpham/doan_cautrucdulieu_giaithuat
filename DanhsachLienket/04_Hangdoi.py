import time

n = input("Nhập các phần tử cho queue: ").split()
m = int(input("Nhập số lượng phần tử muốn xoá: ") )

queue = []

for i in n:
  queue.append(i) # sử dụng hàm append(phần tử) để thêm phần tử vào list
print("Queue ban đầu: ", queue)

print("Các phần tử bị xoá lần lượt là: ", end = "")

time.sleep(1)

for j in range(m):
  print(queue.pop(0), end = " >>> ")
  time.sleep(1)
# sử dụng hàm pop(chỉ số) để xoá phần tử mang chỉ số được chỉ định
# chỉ số = 0 để xoá phần tử đầu danh sách

print("\nQueue sau khi xoá: ", queue)