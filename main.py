listado = []
nombre = 'Cody'

# var = '' or 0 or [] or True
'''
if listado: 
    var = listado
else:
    var = nombre
'''
# var = listado if listado else nombre

var = listado or nombre

print(var)