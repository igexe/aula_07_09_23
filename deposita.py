def deposita(lst):
    busca=int(input('\ndigite o id da conta a qual deseja depositar dinheiro\n'))
    for x in lst:
        if x['id_conta']==busca:
            deposito=float(input('\ndigite o valor do deposito\n'))
            x['saldo']+=deposito