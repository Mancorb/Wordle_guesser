      
def buscar_palabras(lenguaje, numero_letras, letras_contienen, letras_repetidas, letra_inicio, letra_fin) -> list:
    """Regresa un alista de letras que cumplan ciertas especificaciones
    Args:
        lenguaje (str): lenguaje de la wordlist
        numero_letras (int): numero de letras que debe de tener la palabra
        letras_contienen (list): lista de letras que debe contener la palabra
        letras_repetidas (tuple): tipo de letra que se puede repetir y numero de repeticiones validas
        letra_inicio (string): letra con la que debe empezar la palabra
        letra_fin (string): letra con la que debe terminar la palabra
    Returns:
        list: lista de palabras encontradas que cumplen con las especificaciones.
    """
    lista_palabras = _obtener_palabras(lenguaje)
    
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

def _obtener_palabras(lenguaje)-> list:
    """Lee un archivo tipo txt y regresa una lista con todas las palabras leidas cuya longitud sea minimo de 1
    Args:
        lenguaje (string): Especificacion de que archivo buscar (Español o Ingles)
    Returns:
        list: Lista de palabaras encontradas enel archivo.
    """
    wordList =[]
    file_name = " "
    #Especificar el lenguaje de la wordlist
    if lenguaje == "eng":
        file_name = "wordlist.txt"
    elif lenguaje == "esp":
        file_name = "wordlist_esp.txt"
        
    with open(file_name, "r",encoding='utf-8') as file:
        for line in file:
            if len(line)>0 and line != " " and line !="\n" and line!="":
                wordList.append(line[:-1])
                
    return wordList