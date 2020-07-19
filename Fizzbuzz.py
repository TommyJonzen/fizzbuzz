
fizznum = 3
buzznum = 5

for x in range(1, 101):
    if x % fizznum == 0 and x % buzznum == 0:
        print("fizzbuzz")
    elif x % fizznum == 0:
        print("fizz")
    elif x % buzznum == 0:
        print("buzz")
    else:
        print(x)

    
    

