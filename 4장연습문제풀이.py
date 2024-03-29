#4장 연습문제 홀수 번 풀이 2024-03-28
#4.1
def my_greet():
    print("환영합니다.")
my_greet()
my_greet()

#4.3
def max2(m,n):
    if m > n :
        return m
    else :
        return n
def min2(m,n):
    if m < n :
        return m
    else :
        return n
print("100과 200중 큰 수는 : ", max2(100, 200))
print("100과 200중 작은 수는 : ", min2(100,200))

#4.5
def inch2cm(inch):
    return inch * 2.54
for i in range(1,6):
    print("{} 인치 = {} 센티미터".format(i, inch2cm(i)))
        
#4.7
a, b, c = map(int,input("세 수를 입력하시오 : ").split())
def mean3(a, b, c):
    return (a + b+ c) / 3
def max3(a, b, c):
    return max(a, b, c)
def min3(a, b, c):
    return min(a, b, c)
print("10, 20, 30의 평균값은 ", mean3(10, 20, 30))
print("10, 20, 30의 최대값은 ", max3(10, 20, 30))
print("10, 20, 30의 최소값은 ", min3(10, 20, 30))

#4.9
a_list = list(map(int,input("정수를 여러 개 입력하시오 : ").split()))
def mean_of_n(nums):
    return sum(nums) / len(nums)
def max_of_n(nums):
    return max(nums)
def min_of_n(nums):
    return min(nums)
print("평균값은 {}".format(mean_of_n(a_list)))
print("최대값은 {}".format(max_of_n(a_list)))
print("최소값은 {}".format(min_of_n(a_list)))

#4.11
x1 = int(input("x1 좌표를 입력하시오 : "))
y1 = int(input("y1 좌표를 입력하시오 : "))
x2 = int(input("x2 좌표를 입력하시오 : "))
y2 = int(input("y2 좌표를 입력하시오 : "))
def area(x1, y1, x2, y2):
    return ((x2 - x1)*(y2 - y1)) / 2
print("직각삼각형의 면적은 : {}".format(area(x1, y1, x2, y2)))

#4.13
def A(s):
    return s**2
def B(w, h, l):
    return w * h * l
def C(r, k):
    return (1/3)*3.14*r*r*k
def D(a):
    return (4/3)*3.14*a**3
def E(t, u):
    return 3.14*t*t*u
print("모서리의 길이가 12인 정육면체", A(12))
print("모서리의 길이가 20인 정육면체", A(20))
print("가로, 세로, 길이가 각각 3, 5, 6인 직육면체", B(3, 5, 6))
print("반지름과 높이가 각각 20, 10인 원뿔", C(20, 10))
print("반지름이 15인 구", D(15))
print("반지름과 높이가 각각 20, 10인 원기둥", E(20, 10))
    
#4.15
def my_sort(*nums):
    return sorted(nums)
print(my_sort(45, 3, 4, 56, 5))
print(my_sort(9, 8, 7, 6, 5, 4, 3))

#4.17
def sum_range(n1, n2):
    result = 0 
    for i in range(n1, n2+1):
        result += i
    return result
   
print("10에서 20까지의 정수의 합 : {}".format(sum_range(10, 20)))
print("40에서 100까지의 정수의 합 : {}".format(sum_range(40, 100)))

#4. 19
def fibo(n):
    if n <= 1:
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
a = int(input("fibo(n)의 n을 입력하세요 : "))
print("fibo({}) = {}".format(a, fibo(a)))

#4.21
people_address = input('주민등록번호 첫 6숫자 형식 입력: ')
if int(people_address[0:2]) >= 50:
    YY = '19' + people_address[0:2]
else:
    YY = '20' + people_address[0:2]
print('{}년 {}월 {}일'.format(YY, people_address[2:4], people_address[4:6]))

#4.23
def area_and_circumference(r):
    area = r * r * 3.14
    circumference = 2 * r * 3.14
    return area, circumference
while True:
    r = int(input('반지름을 입력하시오: '))
    if r < 0:
        print('프로그램을 종요합니다.')
        break
    Tuple = area_and_circumference(r)
    print('넓이 : {:7.3f}, 둘레 : {:7.3f}'.format(Tuple[0], Tuple[1]))
   
#4.25
s1 = 'Kang Young Min'
s2 = ' Kang Young-Min'
s3 = 'Park Dong Min'
s4 = ' Park Dong-Yun'
L = [s1, s2, s3, s4]
for i in range(4):
    result = L[i].replace(' ', '')
    result = result.replace('-', '')
    result = result.upper()
    print('{}(은)는 {}(으)로 수정됨'.format(L[i], result))
    L[i] = result
for i in L:
    print('{} : {} 개의 N이 나타남'.format(i, i.count('N')))

#4.27
def unit_fraction(frac):
    n = int(1/frac)
    r1 = 1/n
    r2 = 1/(n+1)
    if abs(r1 - frac) < abs(r2 - frac):
        return n
    else:
        return n + 1
num = float(input('1보다 작고 0보다 큰 소수를 입력하세요: '))
n = unit_fraction(num)
print('가장 가까운 단위분수는 1/{}이며, 이 값은 {}입니다.'.format(n, 1/n))
    
