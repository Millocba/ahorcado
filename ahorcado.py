import random

# Juego del ahorcado
# El jugador tiene que adivinar una palabra secreta letra por letra
# Aqui se elige una palabra secreta al azar de una lista de palabras
palabras_a_adivinar = ["python", "programacion", "desarrollo", "computadora", "algoritmo"]
palabra_a_adivinar = random.choice(palabras_a_adivinar)

# Se inicializan las variables del juego
vidas = 6
# aqui se crea una lista de graficos que representan el estado del juego
# cada vez que el jugador pierde una vida, se muestra un grafico diferente
# el primer grafico es el estado inicial, y el ultimo es el estado final (perdido)
graficovidas = [" +-------+\n |       |\n |       |\n         |\n         |\n         |\n         |\n         |\n     ____|_____"," +-------+\n |       |\n |       |\n O       |\n         |\n         |\n         |\n         |\n     ____|_____"," +-------+\n |       |\n |       |\n O       |\n |       |\n         |\n         |\n         |\n     ____|_____"," +-------+\n |       |\n |       |\n O       |\n/|       |\n         |\n         |\n         |\n     ____|_____"," +-------+\n |       |\n |       |\n O       |\n/|\\      |\n         |\n         |\n         |\n     ____|_____"," +-------+\n |       |\n |       |\n O       |\n/|\\      |\n/        |\n         |\n         |\n     ____|_____"," +-------+\n |       |\n |       |\n O       |\n/|\\      |\n/ \\      |\n         |\n         |\n     ____|_____"]
letras_adivinadas = []

# Se crea una lista de guiones bajos que representa la palabra secreta
palabra_dividida = ["_" for _ in palabra_a_adivinar]
print("Bienvenido al juego del ahorcado!")
print("Tienes 6 vidas para adivinar la palabra secreta.")

# Se inicia el juego
while vidas > 0 and "_" in palabra_dividida:

    # Se muestra el estado actual del juego
    print(graficovidas[6-vidas])
    print(" ".join(palabra_dividida)) 

    # se pide al jugador que ingrese una letra
    letra= input("Ingresa una letra: ").lower()

    # se valida la letra ingresada
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, ingresa solo una letra.")
        continue
    # se valida si la letra ya fue adivinada
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra. Intenta con otra.")

    # se valida si la letra es correcta o incorrecta
    elif letra in palabra_a_adivinar:
        letras_adivinadas.append(letra)

        # se actualiza la lista de guiones bajos con la letra adivinada
        # se reemplaza el guion bajo por la letra adivinada en la posicion correcta
        for i, letra_palabra in enumerate(palabra_a_adivinar):
            if letra == letra_palabra:
                palabra_dividida[i] = letra
        print(" ".join(palabra_dividida))
    else:
        letras_adivinadas.append(letra)

        # si la letra no es correcta, se resta una vida
        vidas -= 1
        print(f"Letra incorrecta. Te quedan {vidas} vidas.")

    # se valida si ya se completaron todas las letras de la palabra 
    if "_" not in palabra_dividida:
        print("Felicidades! Adivinaste la palabra:", palabra_a_adivinar)

# se valida si se han perdido todas las vidas
if vidas == 0: 
    print(graficovidas[6-vidas])
    print("Perdiste! La palabra era:", palabra_a_adivinar)
print("Gracias por jugar al ahorcado")
print("Fin del juego")