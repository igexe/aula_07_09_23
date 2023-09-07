def extrato(lst):
    busca=int(input('\ndigite o id da conta que deseja\n'))
    for x in lst:
        if x['id_conta']==busca:
            print(x)