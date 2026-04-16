# tus datos
edades = [15,15,15,15]
musica = ['cumbias', 'electronica', 'cualquiera', 'phonk']

# reto 1: promedio de edad
promedio = sum(edades) / len(edades)
print('Promedio de edad:', promedio)

#reto 2: mayores de 15
mayores = [edad for edad in edades if edad > 15]
print('edades > 15:', mayores) 

#reto 3: fans del rock
fans_rock = [gen for gen in musica if gen =='rock']
print('total de fans rock:', len(fans_rock))