ARQUIVO_CARROS = 'carros.csv'
carros = []

def converte_carro_para_csv(carro):
  return carro["modelo"] + ";" + carro["cor"] + ";" + carro["ano"]

def converte_carros_para_csv(carros):
  return '\n'.join([converte_carro_para_csv(carro) for carro in carros])

def converte_linha_para_carro(linha):
  dados = linha.split(';')
  return {
    "modelo": dados[0],
    "cor": dados[1],
    "ano": dados[2]
  }

def converte_csv_para_carros(linhas):
  return [converte_linha_para_carro(linha.strip()) for linha in linhas]

def le_arquivo():
  global carros
  try:
    arquivo = open(ARQUIVO_CARROS, 'r')
    carros = converte_csv_para_carros(arquivo.readlines())
    arquivo.close()
  except FileNotFoundError:
    pass

def gravar_arquivo():
  arquivo = open(ARQUIVO_CARROS, 'w')
  arquivo.write(converte_carros_para_csv(carros))
  arquivo.close()

def le_int(mensagem):
  while True:
    try:
      return int(input(mensagem))
    except ValueError:
      print('Digite um valor inteiro válido!')

def exibe_menu():
  print('╔════════════════════╗')
  print('║ 1. Adicionar carro ║')
  print('║ 2. Listar carros   ║')
  print('║ 3. Sair            ║')
  print('╚════════════════════╝')

def adicionar_carro():
  carros.append({
    "modelo": input('Digite o modelo do carro: '),
    "cor": input('Digite a cor do carro: '),
    "ano": input('Digite o ano do carro: ')
  })
  gravar_arquivo()

def listar_carros():
  for carro in carros:
    print(carro)

def main():
  le_arquivo()
  while True:
    exibe_menu()
    opcao = le_int('Digite a sua opcao: ')
    if opcao == 1: 
      adicionar_carro()
    elif opcao == 2:
      listar_carros()
    elif opcao == 3:
      break
    else:
      print('Digite uma opção válida!')
  
if __name__ == '__main__':
  main()