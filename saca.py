def saca(lst):
    busca=int(input('\ndigite 1 para buscar contas poupança\ndigite 2 para buscar contas corrente\n'))
    
    if busca==1:
        busca='poupança'
    
    elif busca==2:
        busca='corrente'
    
    for x in lst:
        if x['tipo da conta']==busca:
            print('\n')
            print(x)
    
    busca=int(input('\nesses foram as contas do tipo '+busca+' digite o id da conta para prosseguir\n'))

    for x in lst:
        if x['id_conta']==busca:
            saca=float(input('na conta tem: '+str(x['saldo'])+'\nquanto deseja sacar\n'))
            if x['saldo']>=saca:
                x['saldo']-=saca
                print('ação realizada com sucesso '+str(saca)+' reais foram sacados da conta\n'+str(x['saldo'])+' reais ainda na conta\n')
            else:
                print('\nsaldo insulficiente para realizar a ação\n')