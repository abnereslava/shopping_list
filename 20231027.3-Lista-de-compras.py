listacompras = []
continuar = True
positivo = ["sim", "s", "yes", "y"]
negativo = ["não", "nao", "no", "n"]

def inserirmaisitens():
    resposta = input("Gostaria de inserir mais itens? [s/n]\n")
    if resposta in positivo:
        return True #Essa linha retorna o valor "True" para a variável "caller" (linha 21), continuando o loop.
    elif resposta in negativo:
        print("Encerrando.")
        return False #Essa linha retorna o valor "False" para a variável "caller" (linha 21), parando o loop.
    else:
        print("Resposta inválida. Tente novamente.")
        inserirmaisitens()
        return True

while continuar == True:
   novoitem = input("Insira o nome do item que precisa comprar: \n")
   listacompras.append(novoitem)
   print(f"\nItem acrescentado: {novoitem}. \nLista atual: {listacompras}.\n")
   continuar = inserirmaisitens() #Esta variável é chamada de "caller", pois, ao mesmo tempo que chama a função, a armazena, podendo ter seu valor atualizado posteriormente para False ou True (linhas 9, 12 e 15), continuando ou parando o loop em conformidade com a condicional while (linha 17).

print(f"Lista criada:\n{listacompras} \nBoas compras!")