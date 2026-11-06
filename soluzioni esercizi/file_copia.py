'''
Scrivi un programma che copia il contenuto del file origine.txt nel file copia.txt.
Alla fine il programma deve mostrare il numero di caratteri copiati.
'''
file_input = open("origine.txt", "r")
contenuto = file_input.read()
file_input.close()

file_output = open("copia.txt", "w")
file_output.write(contenuto)
file_output.close()

print("Caratteri copiati:", len(contenuto))
