
ponto_de_cozimento = int(input('ponto de cozimento ='))

if 48 <= ponto_de_cozimento <= 53:
  
    print('Carne selada')
if 54 <= ponto_de_cozimento <= 59:
  
    print('Ao ponto para o mal')
if 60 <= ponto_de_cozimento <= 64:

    print('ao ponto')
if 65<= ponto_de_cozimento <= 70:

    print('Ao ponto para o bem')
if 71<= ponto_de_cozimento:

    print('Bem Passado')

elif 48<= ponto_de_cozimento <= 71:
  
    print('Carne pronta')

else:
    print('Não pronto')
