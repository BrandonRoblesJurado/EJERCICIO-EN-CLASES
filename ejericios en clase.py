"uso de while infinito"
c =1
print(c)

#while validacion
vocal = input("ingrese vocal")
while vocal not in(´a´,´e´,´i´,´o´,´u´):
    if vocal==´.´:
        break
    vocal = imput("vocal:")
print(´su vocal o punto es :{}´.format(vocal))


################################################

#FOR RANGE(V)-range (vi,vf)-range(vi,vf,inc)
frase = input("ingrese frase:")
for indice in range (len(frase)):
    print(indice), ´=´frase [indise]

#for in cadena - in (tupla) - in [lista
for car in frase
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
print("cantidad vocales: {} ".format(cvoc) )























