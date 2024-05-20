import secrets


listaPalavrasAleatorias = [
    # Times do Brasileirão Série A
    "Flamengo", "Corinthians", "Palmeiras", "Santos", "Sao Paulo", "Gremio", "Internacional", "Cruzeiro", "Atletico Mineiro", "Botafogo",
    "Vasco da Gama", "Fluminense", "Bahia", "Sport Recife", "Athletico Paranaense", "Coritiba", "Fortaleza", "Ceara", "Chapecoense",
    # Times do Brasileirão Série B
    "Avai", "Figueirense", "Santa Cruz", "Nautico", "Criciuma", "CSA", "Vitoria", "Juventude", "CRB", "Sampaio Correa",
    "Remo", "Parana", "Londrina", "Oeste", "Brasil de Pelotas", "Guarani", "Operario Ferroviario", "Confianca", "Botafogo-SP", "Ferroviario",
    # Seleções do Mundo
    "Brasil", "Argentina", "Alemanha", "Espanha", "Italia", "Franca", "Portugal", "Holanda", "Inglaterra", "Belgica",
    "Uruguai", "Croacia", "Suica", "Colombia", "Chile", "Mexico", "Estados Unidos", "Nigeria", "Camaroes", "Senegal",
    # Times da Ligue 1
    "Paris Saint-Germain", "Olympique de Marseille", "Lyon", "Monaco", "Lille", "Bordeaux", "Saint-Etienne", "Rennes", "Nice", "Montpellier",
    "Nantes", "Reims", "Strasbourg", "Toulouse", "Angers", "Amiens", "Metz", "Nimes", "Dijon", "Brest",
    # Times da La Liga
    "Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla", "Valencia", "Real Sociedad", "Villarreal", "Real Betis", "Athletic Bilbao", "Celta Vigo",
    "Getafe", "Levante", "Osasuna", "Espanyol", "Alaves", "Valladolid", "Granada", "Eibar", "Mallorca", "Huesca",
    # Times da Serie A Tim
    "Juventus", "Inter de Milao", "Milan", "Napoli", "Roma", "Lazio", "Atalanta", "Fiorentina", "Sampdoria", "Torino",
    "Udinese", "Bologna", "Sassuolo", "Cagliari", "Genoa", "Parma", "Verona", "Spezia", "Benevento", "Crotone",
    # Times da Bundesliga
    "Bayern de Munique", "Borussia Dortmund", "RB Leipzig", "Borussia Monchengladbach", "Bayer Leverkusen", "Wolfsburg", "Eintracht Frankfurt", "Hertha Berlim", "Union Berlin", "Stuttgart",
    "Freiburg", "Hoffenheim", "Augsburg", "Mainz", "Werder Bremen", "Arminia Bielefeld", "Colonia", "Schalke", "Greuther Furth", "Bochum"
]

pEscondida = secrets.choice(listaPalavrasAleatorias).lower()
letrasAdivinhadas = [True if char == ' ' or char == "-" else False for char in pEscondida]
letrasErradas = []
  
def mostrarPalavra():
  for index in range(len(pEscondida)):
    if letrasAdivinhadas[index]:
      print(pEscondida[index], end=" ")
    else:
      print("_", end=" ")
  print()
  print()

def printLetrasErradas(lista):
    stringOrganizada = "  ".join(lista)
    print("Palpites errados: " + stringOrganizada)
  
  
def forca():
   
  partesCorpo = 0  
    
  while not all(letrasAdivinhadas) and partesCorpo < 15: 
    
    printLetrasErradas(letrasErradas)
    print()
    print()
    mostrarPalavra()
    
    entrada = input("Digite uma letra:\n>>> ").lower()
    if not entrada.isalpha() or len(entrada) != 1:
      print("Por favor digite apenas uma letra.")
      continue
    if entrada in letrasErradas:
      partesCorpo += 1
      print("Voce ja digitou esta letra")
      continue
    
    if entrada in pEscondida:
      for i in range(len(pEscondida)):
        if pEscondida[i] == entrada:
          letrasAdivinhadas[i] = True
      print("Letra correta!")
    
    else:
      
      letrasErradas.append(entrada)
      partesCorpo += 1
    
  print(f"\nO jogo terminou!\nA palavra era: {pEscondida}")
  
forca()