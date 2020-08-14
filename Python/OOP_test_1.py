class PartyAnimal:
   x = 0 # klasses pieskirtais x

# __init__ metode tiks izpildita tikai vienu reizi
# veidojot (katru) instanci, talak ja vajag varam pasi izsaukt vel

   def __init__(self):
     print('I am constructed')
     self.x = 0 # metodes ieksejais x
     
   def party(self) :
     self.x = self.x + 1
     print("So far x property of object is",\
           "is : ",self.x)

#__del__ izpildita vienu reizi objektam mainot klassi un info
# no iepreksejas klases pazud, mainit klassi an = 9.5, no int uz float
   def __del__(self):
     print('I am destructed', self.x)
    
print ("Before an = PartyAnimal()")
#print(vars())
an = PartyAnimal()

print ("After an = PartyAnimal()")
#print(vars())
#print( "an data type or class", type(an))
#print("an methods and properties", dir(an))
#print("an x property data type", type(an.x))
#print("an party method data type", type(an.party))
#print(vars(an)) # objekts tika izveidots {tuks}?
#print(vars(an))
#tikai ja klasse ir ar __init__ un ar self.x = ..
#tikai tad {'x':0},savadak ir {}

print ("\nBefore first = an.party()")
an.party() # <- ta ir instance
print ("After first = an.party()")
#print(vars(an)) # objekts "aiztikts"{'x':1}

an.x = 100
an.__init__()

print ("\nBefore second = an.party()")
an.party()
print ("After second = an.party()")

an.x = 200

print ("\nBefore third = an.party()")
an.party()
print ("After third = an.party()")

print ("\nBefore one more = an.party()")
PartyAnimal.party(an)
print ("\nAfter one more = an.party()")

# Code: http://www.py4e.com/code3/party2.py
