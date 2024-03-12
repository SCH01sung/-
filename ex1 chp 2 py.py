#연습문제 2장 2024-03-12
#2.1
print(100,'+', 200,'=', 100 + 200)
print(200,'+',300,'+',400,'=',200+300+400)

#2.3
width = 30
height = 60
area = width * height
print(area)

#2.5
x = int(input('정사각형의 밑변을 입력하시오 : '))
area = x * x
print('정사각형의 면적 :',area)

#2.7
print('10! = ',10*9*8*7*6*5*4*3*2*1)

#2.9
print('섭씨 화씨')
print('0 32.0')
print('10 50.0')
print('20 68.0')
print('30 86.0')
print('40 104.0')
print('50 122.0')

#2.11
fa = int(input('화씨 온도를 입력하세요 : '))
ce = (fa-32)*5/9
print('화씨', fa,' 도는 섭씨 ',ce,'도 입니다')

#2.13
radius = int(input('원의 반지름을 입력하세요 :'))
PI = 3.141592
area = radius **2 * PI
dul = radius * PI * 2
print('원의 둘레 =',dul,'원의 면적 =', area)

#2.15
a = int(input('밑변을 입력하세요 :'))
b = int(input('높이를 입력하세요 :'))
ac = a**2+b**2
c = ac**0.5
print('빗변 :', c)

#2.17
print(2<<0, 2<<1, 2<<2, 2<<3, 2<<4, 2<<5, 2<<6, 2<<7, 2<<8, 2<<9)

#2.19
n = int(input('정수를 입력하세요 : '))
print('입력된 정수는 0에서 100범위 안에 있는 짝수인가요?', n % 2 == 0 and 0 <= n <=100)

#2.21
a = int(input('정수를 입력하세요 : '))
print(a,'의 2진수 값 : ',bin(a))
print(a,'의 2진수 값에 대한 비트단위 부정값 : ',bin(~a))

#2.23
a = int(input('세 자리 정수를 입력하세요 : '))
print('백의 자리 : ',a//100)
print('십의 자리 : ',(a//10)%10)
print('일의 자리 : ',a%10)
