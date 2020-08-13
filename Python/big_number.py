#! /usr/bin/python3.6
print("Ievadiet skaitli")
# a=2**2000000

# te ir tris darbibas - vertibas sagaidisana, vertibas parveidosana, pieskirsana
#argument = input()
#a = int(argument)
#pildot int(input()) "bez izmeiginajuma", programma var vnk izlidot ...
#tapec lai nelidotu, izmantosim  try.. except.. finally konstrukciju
pazime = False
while not pazime:
#while pazime==False:
#while pazime!=True:

    try:
        a = int( input() )
        pazime = True
    except:
        print("Diemzel, cienimajs lietotajs, to, kas ievadits nevar",\
	      "parveidot par vesela tipa skaitli :-( ")
        print("Ludzu, ievadi s_k_a_i_t_l_i velreiz")
#if (a == int): print("a**100")
# ja gribas, var salidzinat type(a) == int -> result bus True
if (a == 5):
     print(a**100)
     print("Aprekins ir gatav")
print("Sis teksts atrodas arpus darbibas bloka - pierakstits bez atstarpem prieksa, tapec tas",\
     "paradisies jebkura gadijuma")
#print ("Ievadāmai vērtībai jābūt skaitlim")
#b=a**100
