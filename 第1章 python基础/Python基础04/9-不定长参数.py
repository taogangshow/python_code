def sum_2_nums(a,b,*args):
    print("*"*50)
    print(a)
    print(b)
    print(args)
    result = a+b
    for num in args:
        result=result+num
    print("result=%d"%result)

sum_2_nums(11,22,33,44,55,66,77)
sum_2_nums(11,22,33)
sum_2_nums(11,22)
#sum_2_nums(11)错误,因为行参中至少要2个参数
