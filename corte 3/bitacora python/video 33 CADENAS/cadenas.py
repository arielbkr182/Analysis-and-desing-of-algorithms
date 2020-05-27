edad=input("introduce la edad: ")
while(edad.isdigit()==False):
    print("por favor esun valor numerico")
    edad=input("introducela edad: ")
if (int(edad)<18):
    print("nose puede pasar")
else:
    print("puedes pasar")
