def findprimefactors(n):
    i=2
    while(n!=1):
        if(n%i==0):
            while (n%i==0):
                print(i)
                n=n/i
        i=i+1
findprimefactors(145)
