import copy

original_list =  [1,2,[1,2]]
deep_copy_list = copy.deepcopy(original_list)

deep_copy_list[2][0] = 999
print(original_list)