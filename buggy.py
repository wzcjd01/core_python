# __author__ = 'Wang Zhicheng'

num_str = raw_input("Enter a number: >> ")

num_num = int(num_str)

non_fac_list = range(1, num_num + 1)
print "Before: ", repr(non_fac_list)

i = 0
while i < len(non_fac_list):
    if num_num % non_fac_list[i] == 0:
        del non_fac_list[i]
    else:
        i += 1

print "After: ", repr(non_fac_list)