listacompras = []
continuar = True
positivo = ["sim", "s", "yes", "y"]
negativo = ["não", "nao", "no", "n"]

def inserirmaisitens():
    resposta = input("Gostaria de inserir mais itens? [s/n]\n").lower()
    if resposta in positivo:
        return True 
    elif resposta in negativo:
        print("Encerrando.")
        return False 
    else:
        print("Resposta inválida. Tente novamente.")
        inserirmaisitens()
        return True

while continuar == True:
   novoitem = input("Insira o nome do item que precisa comprar: \n")
   listacompras.append(novoitem)
   print(f"\nItem acrescentado: {novoitem}. \nLista atual: {listacompras}.\n")
   continuar = inserirmaisitens()

print(f"Lista criada:\n{listacompras} \nBoas compras!")
