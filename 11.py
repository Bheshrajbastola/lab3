'''Building the car game ::
  CAR GAME:
        > help
          start - to start the car
          stop - to stop the car
          quit - to exit
        > asd
          I don't understand this
        > start
          Car started... Ready to go!!
        > stop
          Car stopped..
        > quit'''
start = input('Enter "help" to see instructions: ').lower()

if start == 'help':
    started = False

    while True:
        user_input = input("start - start the car\nstop - stop the car\nquit - exist program\n").lower()
        if user_input == "start":
            if started:
                print("The car is already on.\n")
            else:
                started = True
                print("The car has started. Now what?\n")
        elif user_input == "stop":
            if not started:
                print("The car is already stopped.\n")
            else:
                started = False
                print("The car has stopped. Now what?\n")
        elif user_input == 'quit':
            break
else:
    print("This is not a valid command.")