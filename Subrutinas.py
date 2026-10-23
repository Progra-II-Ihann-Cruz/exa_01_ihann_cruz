import random
from cls_Stack import cls_Stack



def repartir_naipes(jugadores):
    disponibles = []
    for jugador in jugadores:
        if not jugador.partida.isempty():
         print( f"La pila de {jugador.nombre} debe estar vacía.")
         return
    for palo in baraja:
        for carta in palo:
            disponibles.append(carta)  

    random.shuffle(disponibles)

    for turno in range(10):
        for jugador in jugadores:
            carta = disponibles.pop()
            jugador.partida.push(carta)  


def validar_parentesis(expresion):
    pila = cls_Stack()
    if not pila.isempty():
        raise ValueError("La pila debe estar vacía antes de comenzar.")

    parejas = {")": "(", "]": "[", "}": "{"}
    try:
        for caracter in expresion:
            if caracter in "([{":
                if pila.isfull():
                    raise ValueError("La pila permite hasta 10 agrupadores abiertos a la vez.")
                pila.push(caracter)
            elif caracter in parejas:
                if pila.isempty() or pila.pop() != parejas[caracter]:
                    return False

        return pila.isempty()
    finally:
        while not pila.isempty():
            pila.pop()
        if not pila.isempty():
            raise ValueError("La pila debe estar vacía al finalizar.")


# means of char
# B = Bastos o pica
# C = Corazones
# D = Diamantes
# T = Treboles

baraja = [["1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B", "10B", "JB", "QB", "KB"],
          ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC"],
          ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"],
          ["1T", "2T", "3T", "4T", "5T", "6T", "7T", "8T", "9T", "10T", "JT", "QT", "KT"]]
