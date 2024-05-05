ARQUIVO_NOMES = 'nomes.bla'
nomes = []

def le_arquivo():
  global nomes
  try:
    arquivo = open(ARQUIVO_NOMES, 'r')
    nomes = [linha.strip() for linha in arquivo.readlines()]
    arquivo.close()
  except FileNotFoundError:
    pass

def gravar_arquivo():
  arquivo = open(ARQUIVO_NOMES, 'w')
  arquivo.write('\n'.join(nomes))
  arquivo.close()

def le_int(mensagem):
  while True:
    try:
      return int(input(mensagem))
    except ValueError:
      print('Digite um valor inteiro válido!')

def exibe_menu():
  print('╔════════════════════╗')
  print('║ 1. Adicionar nome  ║')
  print('║ 2. Listar nomes    ║')
  print('║ 3. Sair            ║')
  print('╚════════════════════╝')

def adicionar_nome():
  nome = input('Digite o nome: ')
  nomes.append(nome)
  gravar_arquivo()

def listar_nomes():
  for i, nome in enumerate(nomes):
    print('%d - %s' % (i + 1, nome))

def main():
  le_arquivo()
  while True:
    exibe_menu()
    opcao = le_int('Digite a sua opcao: ')
    if opcao == 1: 
      adicionar_nome()
    elif opcao == 2:
      listar_nomes()
    elif opcao == 3:
      break
    else:
      print('Digite uma opção válida!')
  
if __name__ == '__main__':
  main()