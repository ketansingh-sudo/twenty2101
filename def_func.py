def testing(num):
    if (num>50):
        print(num)
    else:
        return testing(testing(num+10))

testing(30)
