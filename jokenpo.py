# PEDRA PAPEL E TESOURA
import secrets

def jogada(jogP1, jogMaq):
  if jogP1 == jogMaq:
    return 3
  
  elif jogP1 == "pedra":
    if jogMaq == "tesoura":
      return 1            # 1 = p1 ganha, 2 = maq ganha, 3 = empate puxa um continue
    else:
      return 2

  elif jogP1 == "papel":
    if jogMaq == "pedra":
      return 1
    else:
      return 2
    
  if jogMaq == "papel":        # so chega aqui se eu coloquei tesoura
    return 1
  else:
    return 2


# main
p1Wins = 0
maqWins = 0

jogadas = ["pedra", "papel", "tesoura"]

while p1Wins != 3 or maqWins != 3:
  
  print(f"\n\nVitorias P1: {p1Wins}\nVitorias IA: {maqWins}\n\n")

  jogadaP1 = input("Jogada Player 1: \ndigite 'pedra', 'papel' ou 'tesoura'\n>>> ")
  
  if jogadaP1.lower() not in jogadas:
    continue
  
  jogadaP1 = jogadaP1.lower()
  
  jogadaMaq = secrets.choice(jogadas)
  
  turno = jogada(jogadaP1, jogadaMaq)
  
  if turno == 3:
    print(f"\nJogada P1: {jogadaP1} x Jogada IA: {jogadaMaq}\nTurno empatado")
    continue
  
  elif turno == 2:
    print(f"\nJogada P1: {jogadaP1} x Jogada IA: {jogadaMaq}\nMaquina ganhou")
    if maqWins == 2:
      print(f"\n\nMAQUINA VENCEU O JOGO\n\n")
      break
    maqWins += 1
    
  else:
    print(f"\nJogada P1: {jogadaP1} x Jogada IA: {jogadaMaq}\nPlayer 1 ganhou")
    if p1Wins == 2:
      print(f"\n\nPLAYER 1 VENCEU O JOGO\n\n")
      break
    p1Wins += 1