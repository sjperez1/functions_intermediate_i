# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def change_x():
    x[1][0] = 15
change_x()
print(x)

def change_last_name():
    students[0]['last_name'] = 'Bryant'
change_last_name()
print(students)

def change_sports_directory():
    sports_directory['soccer'][0] = 'Andres'
change_sports_directory()
print(sports_directory)

def change_z():
    z[0]['y'] = 30
change_z()
print(z)

# 2. Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary(some_list):
    for list_student in range(0, len(some_list)):
        for student in some_list[list_student]:
            # student is accessing each key in each list and some_list[list_student][student] is accessing each value in each list
            print(student, some_list[list_student][student])
iterate_dictionary(students)

# 3. Get Values From a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterate_dictionary2(key_name, some_list):
    # We have more information in this problem, like what the key name is, so 2 for loops are not needed like in the previous one. student2[key_name] is targeting each dictionary's value corresponding to the key in the brackets. This makes sense because the notation to access values is dictionary_name["key_name"].
    for student2 in some_list:
        print(student2[key_name])
iterate_dictionary2('first_name', students)
iterate_dictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(some_dict):
    # for something in this dictionary (each something will be a key-value pair), print the length of value (which is a list here) corresponding with a key and the name of the key.
    for keys in some_dict:
        # print(some_dict[keys])
        # print(keys)
        print(len(some_dict[keys]), keys.upper())
        # for something in the value of a key, print all of the things within that value and corresponding key.
        for values in some_dict[keys]:
            print(values)
print_info(dojo)