# Xây dựng Đồ thị có hướng

# thêm một đỉnh vào dictionary
def them_dinh(v):

  global graph
  global vertices_no

  if v in graph:
    print("đỉnh ", v, "đã tồn tại")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []

# thêm một cạnh giữa đỉnh 1 và đỉnh 2, trọng số cạnh là e
def them_canh(v1, v2, e):

  global graph

  # kiểm tra đỉnh v1 xem có phải là đỉnh hợp lệ không ?
  if v1 not in graph:
    print("đỉnh ", v1, "không tồn tại")

  # kiểm tra đỉnh v2 xem có phải là đỉnh hợp lệ không ?
  elif v2 not in graph:
    print("đỉnh ", v2, "không tồn tại")

  else:
    temp = [v2, e]
    graph[v1].append(temp)

# In đồ thị ra màn hình
def print_graph():
  global graph

  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " với trọng số cạnh là: ", edges[1])


graph = {}

vertices_no = 0
them_dinh(1)
them_dinh(2)
them_dinh(3)
them_dinh(4)

# thêm cạnh giữa hai đỉnh bằng cách
# ghi vào hàm them_canh ba tham số (đỉnh thứ nhất, đỉnh thứ hai, trọng số cạnh)
them_canh(1, 2, 1)
them_canh(1, 3, 2)
them_canh(2, 3, 3)
them_canh(3, 4, 4)
them_canh(4, 1, 5)

print_graph()


print ("Đồ thị được biểu diễn bằng Dictionary: ")
print(graph)

# Ở phần kết quả Đồ thị được biểu diễn bằng Dictionary,
# { 1: [2,1] } nghĩa là { đỉnh thứ nhất: [ đỉnh thứ hai, trọng số cạnh]  }Đ