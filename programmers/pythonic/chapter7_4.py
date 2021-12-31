# 클래스의 string casting
# https://programmers.co.kr/learn/courses/4008/lessons/12837

# 파이썬 클래스에는 여러가지 내부 메소드를 지원한다.
# 그 중, __str__(self)를 사용하여 return 값에 대한 formatting을 설정할 수 있다.
class Coord(object):
    def __init__ (self, x, y):
        self.x, self.y = x, y
    def __str__ (self):
        return '({}, {})'.format(self.x, self.y)
      
print(Coord(1, 2))