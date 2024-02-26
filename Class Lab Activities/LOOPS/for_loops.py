#Print_hi
for i in range(10):
    print('Hi')

#print_hello
for i in range(5):
    print('Hello')

print('There')

#print_hello_5_times_there_5_time
for  i  in range(5):
    print('Hello')
    print('There')


#print_0_t0_9
for i in range(10):
    print(i)

#print_two_ways_to_print_1_to_10
for i in range(10):
    print(i+1)
#print_next_ways
for i in range(1,11):
    print(i)

#print_two_ways_to_print_even_2_to_10
for i in range(2,12,2):
    print(i)
#print_in_next_way
for i in range(5):
    print((i+1) * 2)


#print_Down _from_10_to_1
for i  in range(10,0,-1):
    print(i)

#while_loop
i=0
while i < 10:
    print(i)
    i=i+1


i = 1
while i <=2**32:
    print(i)
    i *= 2

#keep_going
    keep_going= 'Yes'
    while keep_going == 'Yes':
        a=input('Would you like to try again?').lower()
        if a== 'no':
           keep_going = a
        else:
            print('0k, keep going!')