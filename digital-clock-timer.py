import time

timer = int(input("Please enter the time in seconds: ")) 

if timer > 0 :
    for x in range(timer, 0 , -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600 )
        print(f"{hours:02}:{minutes:02}:{seconds:02}") #02 is being used to format the number two two characters
        time.sleep(1)
    print("Times Up")
else:
    print("Enter time greater than 0")
