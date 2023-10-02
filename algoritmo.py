def buscar_palabras(lista_palabras, numero_letras, letras_contienen, letras_repetidas, letra_inicio, letra_fin):
    palabras_encontradas = []
    
    for palabra in lista_palabras:
        # Filtrar por número de letras
        if numero_letras and len(palabra) != numero_letras:
            continue
        
        # Filtrar por letras que debe contener la palabra
        if letras_contienen:
            for letra in letras_contienen:
                if letra not in palabra:
                    break
            else:
                palabras_encontradas.append(palabra)
                continue
        
        # Filtrar por letras repetidas
        if letras_repetidas:
            letra, cantidad = letras_repetidas
            if palabra.count(letra) == cantidad:
                palabras_encontradas.append(palabra)
                continue
        
        # Filtrar por palabras que empiezan con una letra en específico
        if letra_inicio and palabra[0] == letra_inicio:
            palabras_encontradas.append(palabra)
            continue
        
        # Filtrar por palabras que terminan con una letra en específico
        if letra_fin and palabra[-1] == letra_fin:
            palabras_encontradas.append(palabra)
    
    return palabras_encontradas

# Ejemplo de uso
lista_palabras = ["perro", "gato", "pájaro", "elefante", "caballo", "pez", "serpiente", "langosta"]
numero_letras = 8
letras_contienen = ["a", "l"]
letras_repetidas = ("e", 3)
letra_inicio = "e"
letra_fin = "e"

resultados = buscar_palabras(lista_palabras, numero_letras, letras_contienen, letras_repetidas, letra_inicio, letra_fin)
print(resultados)