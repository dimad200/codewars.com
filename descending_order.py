# Ваша задача - создать функцию, которая может принимать любое неотрицательное целое число в качестве аргумента и возвращать его с цифрами в порядке убывания. По сути, переставьте цифры, чтобы получить максимально возможное число.

### Examples:
#Input: `42145`
#Output: `54421`
#Input: `145263`
#Output: `654321`
#Input: `123456789`
#Output: `987654321`


def descending_order(num):
    num=str(num)
    a=list(num)
    for i in range(len(a)):
        a[i]=int(a[i])            

    all_richt=False
    while all_richt == False:
        all_richt=True
        for i in range(len(a)-1):
            if a[i]<a[i+1]:
                a_1=a[i]
                a_2=a[i+1]
                # print("a_1, a_2",a_1, a_2)
                a[i]=a_2               
                a[i+1]=a_1
                all_richt=False
    # print(type(a))
    # print(len(a))
    # print()
    num=str()
    for i in range(len(a)):
        # print(a[i])
        num=num+str(a[i])
    num=int(num)
     
      
    return(num)
