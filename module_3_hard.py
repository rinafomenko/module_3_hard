#data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((),[{(2, 'Urban', ('Urban2', 35))}])]
def calculate_structure_sum(*data_structure):
    #print (len(data_structure))
    sum_ = 0
    for i in range(len(data_structure)):
        
        if isinstance(data_structure[i], int) == True:

            sum_ = sum_ + data_structure[i]

        elif isinstance(data_structure[i], str) == True:

            sum_ = sum_ + len(data_structure[i])

        else:
            if isinstance(data_structure[i], dict) == True:
                keys_ =list(data_structure[i].keys())
                values_ = data_structure[i].values()
                sum_ = sum_ + sum(values_)
                #print(keys_)
                sum_keys = 0
                for j in range(len(keys_)):
                    sum_keys = sum_keys + len(keys_[j])
                sum_ = sum_ + sum_keys

            elif isinstance(data_structure[i], list) == True or isinstance(data_structure[i], set) == True or isinstance(data_structure[i], tuple) == True:
                list_ = list(data_structure[i])
                #print (list_)
                sum_ = sum_ + calculate_structure_sum(*list_)


    return sum_

result = calculate_structure_sum([1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((),[{(2, 'Urban', ('Urban2', 35))}]))
print(result)
