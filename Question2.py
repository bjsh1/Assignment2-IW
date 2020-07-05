#2.Write an if statement to determine whether a variable holding a year is a leap year.

def is_leap(year):

    if (year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("{} Year is leap".format(year))
            else:
                print("{} Year is not leap".format(year))
        
            #print("{} Year is not leap".format(year))
        
        else:
            print("{} Year is leap".format(year))    

        #print("{} Year is leap".format(year))
    else:
        print("{} Year is not leap".format(year))
is_leap(2200)