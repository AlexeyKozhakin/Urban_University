# def calculate_structure_sum(data_structure):
#
#     if isinstance(data_structure,(int,float,bool)):
#         return data_structure
#
#     elif isinstance(data_structure,str):
#         return len(data_structure)
#
#     elif isinstance(data_structure,(list,set,tuple)):
#          data_structure = list(data_structure)
#          if len(data_structure)==1:
#              return calculate_structure_sum(data_structure[0])
#
#          elif len(data_structure)==0:
#              return 0
#          else:
#              return (calculate_structure_sum(data_structure[0])+
#                      calculate_structure_sum(data_structure[1:]))
#
#     elif isinstance(data_structure,dict):
#          keys = list(data_structure.keys())
#          values = list(data_structure.values())
#          return (calculate_structure_sum(keys) +
#                  calculate_structure_sum(values))
#
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
#
# result = calculate_structure_sum(data_structure)
# print(result)

#
# lst = [3,2,1]
# tp = (3,2,1)
# st = {3,2,1}
#
# print(lst[1])
# print(tp[1])
# print(st[1])

# my_dict = {'a':1, 'b':2}
# keys = my_dict.keys()
# values = my_dict.values()
#
# print(keys)
# print(values)
#
# print(type(keys))
# print(type(values))

lst = [1, 2, 4, 5, 'hello', [1, 2, [1,2, [1, 3]]]]
sum = 0
for el in lst:
    if isinstance(el,(int,float,bool)):
       sum+=el
    elif isinstance(el,str):
        sum+=len(el)
    elif isinstance(el,list):
        for el2 in el:
            if isinstance(el2, (int, float, bool)):
                sum += el2
            elif isinstance(el2, str):
                sum += len(el2)

print(sum)

