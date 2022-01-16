import io

# Escribir texto en un fichero:
texto="Un texto\n Otro texto"
fichero=open("fichero.txt","w")
fichero.write(texto)
fichero.close()


fichero=open("fichero.txt","r")
texto=fichero.read()
fichero.close()
print(texto)