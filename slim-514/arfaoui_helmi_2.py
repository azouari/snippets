celsius = [] * 10
fahrenheit = [] * 10
for i in range(10):
    x=int(input("Entrer les 10 temperatures en celcius: "))
    celsius.insert(i,x)
    fahrenheit.insert(i, (x*9)/5 +32)
print("La liste des températures en celsius est : ", celsius)
print("La liste des temperatures en fahrenheit est : ",fahrenheit)