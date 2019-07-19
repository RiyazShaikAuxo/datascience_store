#advantages of Compehentions is performance/Optimization

square_list=[]
for x in range(1,10):
    square_list.append(x**2)
print(square_list)

#OR

square_list=[x**2 for x in range(1,10)]
print(square_list)