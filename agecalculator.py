def agecalculate(age):
    age = int(input("Choose a number between 2-10"))
    if age <2:
        print("It looks like you have chosen a number under 2, Please try again")
        agecalculate(0)
        return 0
    if age >10:
        print("It looks like you have chosen a number above 10, Please try again")
        agecalculate(0)
        return 0
    else:
       ageformula1= age * 2
       ageformula2= ageformula1 + 5
       ageformula3= ageformula2 * 50
       
       birthdaypass = str(input("Has your birthday passed?"))
       bdaypass = birthdaypass.lower()
       if bdaypass == ("yes"):
        ageformula4 = ageformula3 + 1768
        ageyear = int(input("In Which Year Were You Born?"))
        if ageyear < 2014:
            print ("Looks Like You Entered A Valid Year")
        else:
            if ageyear > 2014:
                print ("Looks Like You Entered A Invalid Year (You Can't Be Younger Than 3)")
        
        ageformula5 = ageformula4 - ageyear
        agetotal = ageformula5 - (age * 100)
        agetotalst = str(agetotal)
        if agetotal > 115:
            print("Are you sure you are that old :)?")
        
        
    
        
       else:
        ageformula4 = ageformula3 + 1767
        ageyear = int(input("In Which Year Were You Born?"))
        ageformula5 = ageformula4 - ageyear
        agetotal = ageformula5 - (age * 100)
        agetotalst = str(agetotal)
        if agetotal > 115:
            print("Are you sure you are that old :)?")
            return
        
        
        
       print ("Your Age Is: " + agetotalst)
       return agetotalst
       
    
agecalculate(0)
 
 #It asks the user for a number and runs the formula to guess the age.
 #I found the formula from https://www.wikihow.com/Do-a-Number-Trick-to-Guess-Someone%27s-Age but I converted it into my own code.