"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación III
Period.......: 3-2026
Documents....: Exam_01 - 01_Stack
Goals........: Using stack class
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================="""
from cls_Stack import cls_Stack
from Subrutinas import validar_parentesis, repartir_naipes, jugar, mostrar_resultados, vaciar_pilas
from Jugador import Jugador

print()
print("Stack implementation")
print("=================================")

# Create stack instance
pilita = cls_Stack()

# Load data chunk into stack while this not full
for letra in "Cuquita":
    if not pilita.isfull():
        pilita.push(letra)
    else:
        break

while not pilita.isempty():
    print(pilita.pop())


def main():
    print("Problema 1: Validación de paréntesis")
    expresion = input("Escriba una expresión matemática: ")
    try:
        if validar_parentesis(expresion):
            print("La expresión está bien escrita en cuanto a sus agrupadores.")
        else:
            print("La expresión está mal escrita en cuanto a sus agrupadores.")
    except ValueError as error:
        print("No se pudo evaluar la expresión:", error)


    #Problema 2
    jugadores = [
        Jugador("Ihann Cruz"),
        Jugador("Federick Umaña"),
        Jugador("Jefferson Ortega"),
        Jugador("Luca Solano")
    ]

    repartir_naipes(jugadores)

    for jugador in jugadores:
        print(f"El jugador: {jugador.nombre} tiene {len(jugador.partida)} cartas.")

    ganador = jugar(jugadores)
    vaciar_pilas(jugadores)
    mostrar_resultados(ganador)

if __name__ == "__main__":
    main()

