def inputint():
    n = input("Input a number >>> ")
    try:
        return(int(n))
    except:
        print("It's not a number")
        exit()


