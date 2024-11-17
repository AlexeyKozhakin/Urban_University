#from divide_math_package import fake_divide, true_divide
from divide_math_package.fake_math import divide as fake_divide
from divide_math_package.true_math import divide as true_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)

