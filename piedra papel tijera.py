import random as r
import time as t
from colorama import init, Fore, Back, Style
nombre=input("Hola vamos a jugar a piedra papel o tijera, mi nombre es ktlm4. ¿Y tú, cómo te  llamas ? ")
print(" encantado de conocerte " + nombre)
print("empezamos")
t.sleep(2)
tu=0
yo=0
while yo<3 and tu<3:
  lista=["piedra","papel","tijera"]
  print("piedra,papel o tijera")
  t.sleep(1)
  print("una, dos y tres")
  t.sleep(2)

  print(Fore.GREEN+r.choice(lista))
  print(Fore.WHITE)
  ganado=input("¿quien ha ganado? ")
  if ganado=="tu":
   tu=tu+1
   print()
  elif ganado=="empate":
    print()
  else:
    yo=yo+1
    print()
if tu>yo:
  ganador="tú"
  print(Fore.BLUE+"¡Gané yo!")
else:
  ganador="yo"
  print(Fore.BLUE+"¡Ganaste! " + nombre+Fore.WHITE)