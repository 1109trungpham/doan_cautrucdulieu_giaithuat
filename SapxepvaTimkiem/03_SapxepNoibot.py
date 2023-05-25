class Sapxep:

    def __init__(self, array):
        self.array = array

    # hàm __init__() để gán giá trị cho thuộc tính đối tượng

    def __str__(self):
        return " < ".join([str(x)
                           for x in self.array])

    # hàm __str__() để kiểm soát và cài đặt những gì sẽ xuất hiện ra màn hình

    def Sapxep_Noibot(self, n):

        count = 0
        # if n == 1:
        #     return

        for i in range(n - 1):

            if self.array[i] > self.array[i + 1]:
                self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                # nếu phần tử [i] lớn hơn phần tử liền kề bên phải nó [i+1],
                # thì hoán đổi vị trí của chúng

                count = count + 696969
            # count + 696969 hay gì cũng không làm thay đổi kết quả,
        # miễn là count phải khác 0 để bỏ qua lệnh if bên dưới mà tiếp tục đệ quy

        if (count == 0):
            return

        self.Sapxep_Noibot(n - 1)
    # khi đệ quy giảm n về 1, tức n = 1 thì:
# - count vẫn được gán = 0 như thường lệ
# - tuy nhiên vì n = 1, nên vòng for lúc này không được thực hiện
# - nên count vẫn = 0, dẫn đến kết thúc đệ quy vì điều kiện lệnh if là True


def main():
    array = [14, 4, 21, 9, 29, 10, 1]

    sort = Sapxep(array)

    sort.Sapxep_Noibot(len(array))
    print('Dãy sau khi sắp xếp tăng dần \nbằng phương pháp sắp xếp nổi bọt',
          end=": ")
    print(sort)


if __name__ == "__main__":
    main()