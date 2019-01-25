largest = None
smallest = None
while True:
    num = input('Enter a number: ')

    if num == 'done' :
        break

    try:
        inum = int(num)

    except:
        print('Invalid input')
        str = num
        continue


    if largest is None :
        largest = inum
    elif smallest is None :
        smallest = inum
    elif largest < inum :
        largest = inum
    elif smallest > inum :
        smallest = inum

print('Maximum is',largest)
print('Minimum is',smallest)
