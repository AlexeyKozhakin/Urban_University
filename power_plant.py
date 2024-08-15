import random

access1 = False
access2 = False
access3 = False
#================================== 1 ======================================
n1 = random.randint(0,9)
n2 = random.randint(0,9)
print(f'{n1}+{n2}=?')
res = int(input())
if res == n1 + n2:
    access1 = True
# #================================== 2 ======================================
variants_dict = {
    1:'A:Water\nB:Gas\nC:Uranium\n',
    2:'A:USA\nB:Russia\nC:France\n',
    3:'A:North Korea\nB:The Soviet Union\nC:Japan\n'
}

quest_right_answer_dict = {
1:['Which element is used as fuel in a nuclear power stations?','C'],
2:['Which country uses the most nuclear power?', 'A'],
3:["Which country opened the first nuclear power plant in 1954 known as 'Atom Mirny'?", 'B']
}

num_quest = random.randint(1,3)
print(quest_right_answer_dict[num_quest][0])
print(variants_dict[num_quest])
res = input()
if res == quest_right_answer_dict[num_quest][1]:
    access2 = True

#==================================================== 3 ===================================
right_pin = '6502'
print('Enter PIN:')
pin = input()
if pin == right_pin:
    access3 = True

if access1==access2==access3==True:
    print('Access granted')
else:
    print('Access denied')