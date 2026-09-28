import random
import math


numero_secreto = random.randint(1, 24)

print("🎯 Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar onde está o esconderijo entre as posições 1 e 24.")
print("Você tem 6 tentativas. Boa sorte!\n")

for tentativa in range(1, 7):
    chute = int(input(f"Tentativa {tentativa}/6 - Digite o seu palpite (1-24): "))
    
  
    distancia = abs(numero_secreto - chute)
    
    
    if distancia == 0:
        print(f"🎉 Parabéns! Você acertou na tentativa {tentativa}!")
        break
    elif distancia <= 2:
        print("🔥 Muito Quente!\n")
    elif distancia <= 4:
        print("☀️ Quente!\n")
    else:
        print("🧊 Frio!\n")
else:
    # Este 'else' só executa se o jogador gastar as 6 tentativas sem acertar
    print(f"💥 Fim de jogo! O número secreto era {numero_secreto}.")