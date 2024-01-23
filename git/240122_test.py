my_str = 'banana'
x = 'b'
# find

print(my_str.find('b'))
print(my_str.find('x'))

#index
print(my_str.index('b'))
print(my_str.index(x))

# isalpha

string1 = 'Hello'
string2 = '123'
print(string1.islower())
print(string2.isalpha())

# replace
text = 'Hello, world!'
b = 'Banaa'
new_text = b.lower()
print(b.lower())

# append

my_list = [1,2,3]
my_list.append(0*5)
print(my_list.pop(2))
print(my_list)



#할당
original_list = [1,2,3]
copy_list = original_list 
copy_list[0] = 'hello'
print(original_list)

a=[1,2,[100,200]]
b = a[:]
# 얕은 복사의 한계 (2중리스트 이차원리스트는 복사를 못행...)
b[2][0] = 999
print(a)
print(b)