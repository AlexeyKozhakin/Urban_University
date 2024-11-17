import random
#
count=0
#============================== 1 ============================
n1 = random.randint(0,9)
n2 = random.randint(0,9)
print(f'{n1}+{n2}=?')
x = int(input())
if x == n1 + n2:
    count+=1

# #============================== 2 =============================
dict_questions = {
1:['Which element is used as fuel in a nuclear power stations?',
   'A:Water\nB:Gas\nC:Uranium',
   'C'],
2:['Which country uses the most nuclear power?',
   'A:The United States\nB:Russia\nC:France',
   'A'],
3:["Which country opened the first nuclear power plant in 1954 known as 'Atom Mirny'",
   'A:North Korea\nB:The Soviet Union\nC:Japan',
   'B']
}

num_question = random.randint(1,3)
print(dict_questions[num_question][0])
print(dict_questions[num_question][1])
x = input()

if x == dict_questions[num_question][2]:
    count+=1
#======================================== 3 =================================================

print('Enter PIN:')
correct_pin = '6502'
pin = input()
if pin == correct_pin:
    count+=1

if count == 3:
    print('Access granted')
else:
    print('Access denied')

#
# st = 'Молоко\nХлеб\nСметана'
# print(st)


# st = 'Привет hello \'hi\' '
#
# print(st)