#5장 홀수번 문제풀이 2024-04-02
#5.1
list_ex = [10, 20, 30, 40, 50, 60, 70]
high = 5
low = 3
print(list_ex[low])
print(list_ex[low+2])
print(list_ex[high - low])
print(list_ex[low - high])
print(list_ex[-1])
print(list_ex[-low])
print(list_ex[2*3])
print(list_ex[5 % 4])
print(list_ex)

#5.3
list1 = [3, 5, 7]
list2 = [2, 3, 4, 5, 6]
for i in list1:
    for j in list2:
        print("{} * {} = {}".format(i, j, i*j))
    
#5.5
list1 = ["I ike", "I love"]
list2 = ["pancakes.", "kiwi juice.", "espresso."]
for i in list1:
    for j in list2:
        print("{} {}".format(i, j))

#5.7
n_list = [10, 20, 30, 50, 60]
print("리스트 원소들 : ", n_list)
i = 0
for i in n_list:
    i += i
print("리스트 원소들의 합 : {}".format(i))

#5.9
n_list = [10, 20, 30, 50, 60]
print("리스트 원소들 : ", n_list)
result = 0
for i in n_list:
    if i > result:
        result = i

print("리스트 원소들 중 최대값 : {}".format(result))

#5.11
#list = list(map(int,input("5개의 수를 입력하세요 : ").split()))
#print("합 : ", sum(list))
#print("평균 : ", sum(list)/len(list))
#print("최댓값 : ", max(list))
#print("최댓값 : ", min(list))

#5.13
nums = list(map(int,input("10개의 수를 입력하세요 : ").split()))
print("합 : ", sum(nums))
print("평균 : ", sum(nums)/len(nums))
result = 0
for i in nums:
    result += (i - sum(nums)/len(nums))**2
    
print("표준편차 : ", (result/len(nums))**0.5)
    
#5.15
greet = "have a beautiful day."
print(greet[0:4])
print(greet[7:16])
print(greet[17:20])

#5.17-(1)
animals = ["dog", "cat", "tiger", "lion"]
print("animals = ", animals)
#5.17-(2)
animals.pop(0)
animals.append("dog")
print("animals = ", animals)
#5.17-(3)
animals = ["dog", "cat", "tiger", "lion"]
print("animals = ", animals)
for i in animals:
    print("I love {}.".format(i))

#5.19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []
for i in s_list:
    if not i in new_s_list:
        new_s_list.append(i)
print("new_s_list = ", new_s_list)

#5.21
scr = "a2b3c6a2c3figl"
for ch in scr:
    if ch.isnumeric():
        for i in range(int(ch)):
            print(ch,end='')
    else:
        ch_old = ch
#5.23
person1 =['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]
def function_of_persons(person_list):
    result = {}
    divide_list = []
    for i in range(int(len(person_list) / 5)):
        divide_list.append(person_list[i * 5:i * 5 + 5])
    result['n_persons'] = len(divide_list)
    result['average_age'] = 0
    result['n_male'] = 0
    result['f_male'] = 0
    result['person_list'] = divide_list
    for i in divide_list:
        result['average_age'] += i[1]
        if i[2] == 1:
            result['n_male'] += 1
        else:
            result['f_male'] += 1
    result['average_age'] /= result['n_persons']
    return result

person_list = person1 + person2 + person3 + person4
print(function_of_persons(person_list))
























    
