import importlib
from math_divide import fake_divide, true_divide

package_name = 'math_divide'
package = importlib.import_module(package_name)

if hasattr(package, '__all__'):
    modules = package.__all__
else:
    modules = [name for name, obj in package.__dict__.items()]

for module in modules:
    print(module)

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
# __name__ = 'Иван Иванович'
# print('в файле module_4_1 __name__ =',__name__)
#
# for __name__ in range(10):
#     print('hi')

lst = list(range(1,11))
print(lst)

lst2 = [el**2 for el in lst]
# for el in lst:
#     lst2.append(el**2)

print(lst2)

import sys

print("Импортированные модули:")
for module in sys.modules:
    print(module)