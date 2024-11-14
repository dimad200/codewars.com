# удалить каждый второй элемент из списка
def remove_every_other(my_list):
    c = my_list.copy()
    a=len(my_list)-1
    for i in range(len(my_list)):
        
        if (a-1)%2==0:
            del c[a]
        a-=1
        
    return c


a=['Hello', 'Goodbye', 'Hello Again']
print(remove_every_other(a))
