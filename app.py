start=False
while (1):
    command=input("> ").lower()
    if command=='help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command=='start':
        if start:
            print('The car has already started')
        else:
            print('The car has started! Ready to go!')
        start=True
    elif command=='stop':
        if not start:
            print('The car has stopped')
        else:
            print('The car has stopped')
            start=False
    elif command=='quit':
        break
    else:
        print('I do not understand...')
