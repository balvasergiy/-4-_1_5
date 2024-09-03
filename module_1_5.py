immutable_var=1,2,'a','b'
print(immutable_var)
immutable_var_1=(1,2,'a','b')   #это неизменяемая упорядоченная коллекция
immutable_var_2=([1,2,'a','b']) #кортеж не поддерживает обращение по элементам
print(immutable_var_1)
print(immutable_var_2)
mutable_list=[1,2,'a','b','modified']
print(mutable_list)
mutable_list=[0][0]=2
print(mutable_list)
mutable_list=(1,2)*3+('a','b','modified')
print(mutable_list)