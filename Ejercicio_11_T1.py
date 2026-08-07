"""11. Escribe un program que te permita ingresar una cadena de texto y 
el programa indique si la cadena esta formada solamente por letras en 
mayúsculas"""

string = input('Ingresa una clave que contenga MAYUSCULAS: ')
mayuscula = True

if not string: 
    mayuscula = False
    print('Tu cadena esta vacía')
else:
    for caracter in string:
        if not caracter.isupper() or not caracter.isalpha:
            mayuscula = False
        break #si ya encontramos uno, no hay que seguir buscando 

    if mayuscula: 
    
        print(f'Tu clave {string} tiene puramente MAYUSCULAS')
    else:
        print(f'ERROR, la clave {string} no está formada únicamente por MAYUSCULAS')