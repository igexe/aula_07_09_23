def cria_conta(id):
    conta={
        'id_conta':id,
        'numero':int(input('\ndigite o numero da conta\n')),
        'titular':input('\ndigite o nome do titular da conta\n'),
        'saldo':float(input('\ndigite o saldo da conta\n')),
        'tipo da conta':input('\ndigite o tipo da conta\n'),
        'limite':float(input('\ndigite o limite da conta\n'))
    }
    return conta