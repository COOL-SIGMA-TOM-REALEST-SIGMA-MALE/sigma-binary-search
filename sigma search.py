array = ['1','2','3','4','5','6','7','8']
usershinput = input('enter number liberal')
suschungus = len(array)
print(suschungus)
suschungus = (suschungus -1)//2
while True:
    print (suschungus)
    if array [suschungus] > usershinput:
        suschungus = suschungus//2
        print ('hi')
    elif array[suschungus] < usershinput:
        suschungus = suschungus * 1.5
        suschungus = suschungus//2
        suschungus = int(suschungus*2)
        
        print('hi2')
    
    else:
        print ('input found at ' , suschungus)
        break
    print('next index' ,suschungus)              
