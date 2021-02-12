import requests

### Inicio do Menu ###
def menu():
  print("\n")
  menu_reset = str(input("Gostaria de pesquisar novos sites? s/n: ")).lower()
  if menu_reset == "s":
    main()
  elif menu_reset == "n":
    print("Programa fechado com sucesso!")
    return
  else:
    print("Digito invalido!")
    menu()

def main():
  print("Bem vindo ao Verificador de Site!")
  print('Entre com os sites desejado, separandos com " , ": \n')  
  ### Transforma oque foi escrito em uma lista e deixa tudo em minusculo ######
  entrada_lista = str(input()).lower().split(",")
  print("\n \n \n")

  for url in entrada_lista:
    ##### retira os espaços em brancos ##
    url = url.strip()
    #### caso for passado um valor sem o .com retorna que o valor é invalido ###
    if "." not in url:
      print(f"{url} Url invalido!")
      print("----------#----------------#------------")
    else:
      #### se for passado o valor sem o http antes, acrescenta automaticamente ####
      if "http" not in url:
        url = f"http://{url}"
      try:
        r = requests.get(url)
        if r.status_code == 200:
          print(f"{url} O Site está online")
          print("----------#----------------#------------")
        else:
          print(f"{url}  O Site está off.")
          print("----------#----------------#------------")
      except:
          print(f"{url} O Site está off.")
          print("----------#----------------#------------")
  menu()

main()          





