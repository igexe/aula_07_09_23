import cria_conta as conta
import deposita

id=0
contas=[]

dados=open('dados.txt','r')
db=dados.readlines()

if int(db[0])>0:
    id=int(db[0])
    for x in db:
        if x!=db[0]:
            x=x.rstrip('\n')
            x=eval(x)
            contas.append(x)

else:
    pass

dados.close()

ig=True

while ig==True:
    act=int(input('\n1 para criar conta\n2 para realizar um deposito\n99 para encerrar seção\n'))

    match act:

        case 1:
            id+=1
            contas.append(conta.cria_conta(id))

            salva=str(id)+'\n'
            for x in contas:
                salva+=str(x)+'\n'

            dados=open('dados.txt','w')
            dados.writelines(salva)
            
            for x in contas:
                if x['id_conta']==id:
                    print('\nconta\n===========\n'+str(x)+'\n===========\nfoi salva com sucesso\n')

        case 2:
            deposita.deposita(contas)

            salva=str(id)+'\n'
            for x in contas:
                salva+=str(x)+'\n'

            dados=open('dados.txt','w')
            dados.writelines(salva)

            dados.close()

        case 99:
            ig=False

        case _:
            print('ação não reconhecida por favor escolha uma ação apresentada anteriormente')