from algoritmo import buscar_palabras

if __name__ == "__main__":
    
    # Ejemplo de uso
    lenguaje = "esp"
    numero_letras = 8
    letras_contienen = ["a", "l"]
    letras_repetidas = ("e", 3)
    letra_inicio = "e"
    letra_fin = "e"

    print(buscar_palabras(lenguaje,numero_letras,letras_contienen,letras_repetidas,letra_inicio,letra_fin))