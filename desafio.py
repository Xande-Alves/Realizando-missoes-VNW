print('\nMISSÃO 01: Verifica aprovação do aluno.\nMISSÃO 02: Verifica situação eleitoral do aluno.\nMISSÃO 03: Verificação da classificação da nota dos alunos.\nMISSÃO 04: Verifica soma de números.\nMISSÃO 05: Verifica acesso ao cofre.\nMISSÃO 06: Verifica contagem de 1 a 10.\nMISSÃO 07: Verifica organização de números numa lista.\nMISSÃO 08: Verifica a exibição de primeiro e último nomes numa lista.\nMISSÃO 09: Verifica o dobro de um número.\nMISSÃO 10: Verifica contagem de letras de um nome.')

escolha_missao = None

while escolha_missao != 0:
    escolha_missao = int(input('Escolha a missão que deseja realizar (1 a 10), ou digite "0" para SAIR:   '))

    while escolha_missao not in range(0,11):
        escolha_missao = int(input('ESCOLHA INVÁLIDA: Escolha a missão que deseja realizar (1 a 10), ou digite "0" para SAIR:   '))

    if escolha_missao == 0:
        break

    elif escolha_missao == 1:
        print('MISSÃO 01 INICIADA!')
        print('=================================================================')
        continuar='S'

        while continuar == 'S':
            nota_aluno = float(input('Digite a nota do aluno:   '))
        
            if nota_aluno >= 5:
                print(f'O aluno obteve nota {nota_aluno} e foi APROVADO!')
            else:
                print(f'O aluno obteve nota {nota_aluno} e foi REPROVADO!')

            continuar = input('Deseja consultar nota de outro aluno? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja consultar nota de outro aluno? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 01 CONCLUÍDA!')
                print('================================================================')

    elif escolha_missao == 2:
        print('MISSÃO 02 INICIADA!')
        print('=================================================================')
        continuar = 'S'

        while continuar == 'S':
            idade_aluno = int(input('Digite a idade do aluno:   '))

            if idade_aluno>= 16:
                print(f'O aluno possui {idade_aluno} anos e está HABILITADO para votar!')
            else:
                print(f'O aluno possui {idade_aluno} anos e NÃO está HABILITADO para votar!')

            continuar = input('Deseja consultar situação eleitoral de outro aluno? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja consultar situação eleitoral de outro aluno? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 02 CONCLUÍDA!')
                print('================================================================')

    elif escolha_missao == 3:
        print('MISSÃO 03 INICIADA!')
        print('=================================================================')
        continuar = 'S'

        while continuar == 'S':
            nota_aluno2 = int(input('Digite a nota do aluno que deseja consultar (0 a 100):   '))

            while nota_aluno2 > 100 or nota_aluno2 < 0:
                nota_aluno2 = int(input('NOTA INVÁLIDA! Digite a nota do aluno que deseja consultar (0 a 100):   '))
            
            if nota_aluno2>=90:
                print("Parabéns, você tirou A!")
            elif nota_aluno2 >= 80:
                print("Muito bem, você tirou B.")
            elif nota_aluno2 >= 70:
                print("Bom trabalho, você tirou C.")
            elif nota_aluno2 >= 60:
                print("Fique atento, você tirou D.")
            else:
                print("Estude um pouco mais, você tirou F.")
            
            continuar = input('Deseja consultar nota de outro aluno? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja consultar a nota de outro aluno? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 03 CONCLUÍDA!')
                print('================================================================')

    elif escolha_missao == 4:
        print('MISSÃO 04 INICIADA!')
        print('=================================================================')
        continuar = 'S'

        while continuar == 'S':
            num1 = float(input('Digite um primeiro número:   '))
            num2 = float(input('Digite um segundo número para ser somado ao primeiro:   '))

            print(f'O número {num1} somado ao número {num2} resulta em {num1 + num2}.')

            continuar = input('Deseja realizar uma nova soma? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja realizar uma nova soma? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 04 CONCLUÍDA!')
                print('================================================================')

    elif escolha_missao == 5:
        print('MISSÃO 05 INICIADA!')
        print('=================================================================')
        continuar = 'S'

        while continuar == 'S':
            senha = input('Digite a senha para acessar o cofre:   ')

            while senha not in ['Python123','0000']:
                senha = input('SENHA INCORRETA! Digite a senha para acessar o cofre ou digite 0000 para desistir do acesso:   ')
            
            if senha == 'Python123':
                print('COFRE LIBERADO!')

            continuar = input('Deseja realizar um novo acesso ao cofre? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja realizar um novo acesso ao cofre? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 05 CONCLUÍDA!')
                print('================================================================')

    elif escolha_missao == 6:
        print('MISSÃO 06 INICIADA!')
        print('=================================================================')
        continuar = 'S'

        while continuar == 'S':
            contador = 1
            while contador <=10:
                print(contador)
                contador += 1
        
            continuar = input('Deseja realizar uma nova contagem? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja realizar uma nova contagem? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 06 CONCLUÍDA!')
                print('================================================================')

    elif escolha_missao == 7:
        print('MISSÃO 07 INICIADA!')
        print('=================================================================')
        continuar = 'S'

        while continuar == 'S':
            lista_numeros = [8,3,10,1,5]
            print(f'A lista de números está da seguinte forma: {lista_numeros}')
            
            organiza = input('Deseja organizá-la? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while organiza not in ['S','N']:
                organiza = input('OPÇÃO INVÁLIDA! Deseja organizar a lista? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if organiza == 'S':
                print(f'A lista foi organizada e ficou da seguinte forma {sorted(lista_numeros)}.')
            else:
                print('Tudo bem, quem sabe na próxima...')

            continuar = input('Deseja ver a lista de números novamente? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja ver a lista de números? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 07 CONCLUÍDA, SE VOCÊ ORGANIZOU A LISTA!')
                print('================================================================')

    elif escolha_missao == 8:
        print('MISSÃO 08 INICIADA!')
        print('=================================================================')
        continuar = 'S'
        lista_alunos = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo']

        while continuar == 'S':
            print(f'A lista de números está da seguinte forma: {lista_alunos}')
            mostra_primeiro_ultimo = input('Deseja que seja mostrado o primeiro e último alunos da lista? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while mostra_primeiro_ultimo not in ['S','N']:
                mostra_primeiro_ultimo = input('OPÇÃO INVÁLIDA! Deseja que seja mostrado o primeiro e último alunos da lista? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if mostra_primeiro_ultimo == 'S':
                print(f'O primeiro nome da lista é o {lista_alunos[0]} e o último é {lista_alunos[-1]}.')
            else:
                print('Tudo bem, quem sabe na próxima...')

            continuar = input('Deseja ver a lista de alunos novamente? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja ver a lista de alunos novamente? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 08 CONCLUÍDA, SE VOCÊ MOSTROU O NOME DO PRIMEIRO E ÚLTIMO ALUNO!')
                print('================================================================')

    elif escolha_missao == 9:
        print('MISSÃO 09 INICIADA!')
        print('=================================================================')
        continuar = 'S'

        while continuar == 'S':
            numero = float(input('Digite um número que deseja saber o seu dobro:   '))
            print(f'O dobro do número {numero} é {numero*2}.')
        
            continuar = input('Deseja ver a lista de alunos novamente? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja ver a lista de alunos novamente? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 09 CONCLUÍDA!')
                print('================================================================')

    else:
        print('MISSÃO 10 INICIADA!')
        print('=================================================================')
        continuar = 'S'

        def contar_letras(n):
            return f'O nome {nome} possui {len(nome)} letras.'

        while continuar == 'S':
            nome = input('Digite o nome que deseja contar as letras:   ')
            print(contar_letras(nome))

            continuar = input('Deseja contar as letras de um novo nome? Digite "S" para SIM e "N" para NÃO.   ').upper()

            while continuar not in ['S','N']:
                continuar = input('ESCOLHA INVÁLIDA: Deseja contar as letras de um novo nome? Digite "S" para SIM e "N" para NÃO.   ').upper()

            if continuar == 'N':
                print('MISSÃO 10 CONCLUÍDA!')
                print('================================================================')

    print('\nMISSÃO 01: Verifica aprovação do aluno.\nMISSÃO 02: Verifica situação eleitoral do aluno.\nMISSÃO 03: Verificação da classificação da nota dos alunos.\nMISSÃO 04: Verifica soma de números.\nMISSÃO 05: Verifica acesso ao cofre.\nMISSÃO 06: Verifica contagem de 1 a 10.\nMISSÃO 07: Verifica organização de números numa lista.\nMISSÃO 08: Verifica a exibição de primeiro e último nomes numa lista.\nMISSÃO 09: Verifica o dobro de um número.\nMISSÃO 10: Verifica contagem de letras de um nome.')

    escolha_missao = int(input('Escolha a missão que deseja realizar (1 a 10), ou digite "0" para SAIR:   '))
    
print('SAINDO DO MENU DE MISSÕES... ATÉ A PRÓXIMA!')          
        
        
