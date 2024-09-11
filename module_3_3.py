values_list = [11, False, 'city']
values_dict = {'a':1, 'b':'Строка', 'c': True}

def print_params (a=1, b='Строка', c=True):
    print(a, b, c)
    global values_list
    global values_dict
values_list_2 = [54.32, 'Строка']

print_params()
print_params(b=25)
print_params (c=[1,2,3])
print_params(*values_list)
print_params (**values_dict)
print_params(*values_list_2, 42)
