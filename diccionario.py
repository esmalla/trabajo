#diccionario

#son estructura con clave y valor clave:valor

persona = {
    'Dilan':"Dilan Martinez",
    'alex':"alex Rojas",
    'Kimberly':"Kymberly  cc",
   #'materias':["españo","algebra","ecologia"] 

}
print(persona)
print(persona['alex'])

#print(persona['materias'])
cuantasPersonas =len(persona)

print(cuantasPersonas)

print('Kimberly' in persona)

esta= 'Karla'


print(persona.get('Kimberly'))
persona.update({"Dilan":"18"})

print(persona)

for pop in persona:
    print(persona[pop])


for llave in persona.keys():
    print(llave +"="+persona[llave])