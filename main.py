# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main


a = mean_var_std.calculate([2,6,2,8,4,0,1,5,7])

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)

dictlist = list()
for key, value in a.items():
    temp = [key,value]
    dictlist.append(temp)
a.items()
print(a)
