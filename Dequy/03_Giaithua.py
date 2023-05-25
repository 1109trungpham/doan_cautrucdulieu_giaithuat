# 03 Đệ quy Giai thừa của một số

def Giaithua(n):
  if n == 0:
    return 1
  else:
    return n * Giaithua(n-1)

print("5! =", Giaithua(5) )
