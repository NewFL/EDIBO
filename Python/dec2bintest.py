
#!/usr/bin/python3

a = int(input("Type number ")) 
#need to add variable that will contane number after /
print (a)
c =int(a / 2)
print (c)
if (c != 0):
    d = a % 2
    print (d)
#PROBLEM IF TYPE 5 THEN D IS PRINTED AS 0, BUT IT SHOULD BE 1,AS 5%2=1
#else:
#    (c == 0)
#    print ("Done")
    
