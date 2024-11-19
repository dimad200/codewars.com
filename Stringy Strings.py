# write me a function stringy that takes a size and returns a string of alternating 1s and 0s.
# the string should start with a 1.
# a string with size 6 should return :'101010'.
# with size 4 should return : '1010'.
# with size 12 should return : '101010101010'.
# The size will always be positive and will only use whole numbers.

# напишите мне функцию stringy, которая принимает значение size и возвращает строку из чередующихся 1 и 0.
# строка должна начинаться с 1.
# строка размером 6 должна возвращать значение '101010'.
# при размере 4 должно быть возвращено значение "1010".
# при размере 12 должно быть возвращено значение "101010101010".
# Размер всегда будет положительным и будут использоваться только целые числа.
def stringy(size):
    ls=[]
    flag_1 = True
    for i in range(int(size)):
        if flag_1==True:
            flag_1=False
            ls.append(1)
        else:
            flag_1=True
            ls.append(0)
    return str(ls).replace(", ","").replace("[","").replace("]","")


print(stringy(4))
    # Good Luck!