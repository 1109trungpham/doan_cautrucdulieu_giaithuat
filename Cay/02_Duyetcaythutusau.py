class Node:
  def __init__(self, father):
    self.father = father  # Tạo node cha
    self.left = None      # Tạo node con bên trái node cha (trống dữ liệu)
    self.right = None     # Tạo node con bên phải node cha (trống dữ liệu)


def Post_order(root):  # HÀM DUYỆT CÂY THỨ TỰ SAU

    if root:  # root là node gốc,
        # bước này kiểm tra xem node này có tồn tại hay không?

        Post_order(root.left)  # Đầu tiên đệ quy trên Con trái

        Post_order(root.right)  # Sau đó đệ quy trên Con phải

        print(root.father)  # Cuối cùng in dữ liệu của node gốc

# Chương trình chính duyệt cây nhị phân

if __name__ == "__main__":

  # Tạo node Trường
  A = Node("Khoa Kỹ thuật và Công nghệ")

  # Tạo các node Ngành
  B = Node("Khoa học dữ liệu và Trí tuệ nhân tạo")
  C = Node("Kỹ thuật điều khiển và Tự dộng hoá")

  # Tạo các node Chuyên ngành
  D = Node("Phân tích dữ liệu kinh doanh")
  E = Node("Trí tuệ nhân tạo")
  F = Node("Điện gió - Điện mặt trời")
  G = Node("Robot công nghiệp")

  A.left = B
  A.right = C

  B.left = D
  B.right = E

  C.left = F
  C.right = G

  print("Duyệt cây \"Khoa Kỹ thuật và Công nghệ\" theo thứ tự sau:\n")
  Post_order(A)