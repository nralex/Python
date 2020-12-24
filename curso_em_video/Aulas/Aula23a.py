try:
    a = int(input('Numerados: '))
    b = int(input('Denominador: '))
    r  = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipo de de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'O problema encontrado foi {erro.__class__}')

else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')