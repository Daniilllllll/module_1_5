

immutable_var = 1,2,3, False , 'a','b','c',
print(immutable_var)

#immutable_var[2]  =5
#print(immutable_var) не даст изменить, тк кортеж не поддерживает обращение по элементам

mutable_list = ([1,2],'a','b') #могу ли я изменять str('a' или 'b') внутри кортежа? или только числа можно
mutable_list[0][1] = 9
print(mutable_list)


#mutable_list = ([1,2],['a','b'])
#mutable_list[2]['a'] = 'c'
#print(mutable_list)
