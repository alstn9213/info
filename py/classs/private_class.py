# 비공개 클래스 속성은 클래스 안의 메서드에서만 접근할 수 있고 바깥에서 접근하면 에러가 발생한다.
class Knight:
  __item_limit = 10
  def print_item_limit(self):
    print(Knight.__item_limit)

x = Knight()
x.print_item_limit()
print(Knight.__item_limit)