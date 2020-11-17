class Circle : 
  def __init__(self, r):
    self.R=r
  def enffp(self):
    self.m=2*self.R*3.14
    return self.m
  def sjfqdl(self):
    return self.R*self.R*3.14
  
a=float(input("원의 반지름을 입력하시오. : "))
b=Circle(a)
print("원의 둘레는 ", b.enffp(), "이다.", sep='')
print('원의 넓이는 ', b.sjfqdl(), "이다.", sep='')
