def inicio_jogo():
    print("              |")
    print("        __'-|-!__")
    print(" _!_,__|=========|______:,_ ")
    print("|                   __     |")
    print("|  HOSPITAL      __|  |__  | ")
    print("|  = ==== =     |__    __| |")
    print("|                  |__|    | ")
    print("|                          |")
    print("|__________________________| ")
    print('Mais um dia de plantão... Você acabou de chegar ao hospital e observa a emergência com 3 macas diferentes')

def fase_final(acao_escolhida):
    if acao_escolhida == 'a':
        print('[ENFERMEIRA]: Dra., o paciente acabou de retornar a emergência, infelizmente veio a falecer no caminho pois o socorro não chegou a tempo.')
    elif acao_escolhida == 'b':
        print('[ENFERMMEIRA]: Dra., a medicação recomendada não foi precisa e o paciente precisou ser encaminhado para a UTI')
    else:
        print('[ENFERMEIRA]: Parabéns Dra.! A cirurgia foi um sucesso e o paciente se recupera bem')

def fase(ambientacao, historia, texto, opcoes):
    print(ambientacao)
    print(historia)
    print(texto)
    print(opcoes)

def escolha_personagem():
    print('MACA a: Paciente relata fortes dores no peito \nMACA b: Paciente diz que constantemente sente muita falta de ar. \nMACA c: Paciente não identificado, visivelmente confuso.')
    paciente_escolhido = escolha()
    return paciente_escolhido

def escolha():
    opcao = input('Digite a letra da opção escolhida: ')
    return opcao

def maca(escolhaDePersonagem):
    if escolhaDePersonagem == 'a':
        return 'primeira'
    elif escolhaDePersonagem == 'b':
        return 'segunda'
    else:
        return 'terceira'

def medica(escolhaDePersonagem):
    if escolhaDePersonagem == 'a':
        return 'Cristina Jovem'
    elif escolhaDePersonagem == 'b':
        return 'Livia Wesley'
    else:
        return 'Meredith Cinza'

def dor(escolhaDePersonagem):
    if escolhaDePersonagem == 'a':
        return 'no peito'
    elif escolhaDePersonagem == 'b':
        return 'nas costas'
    else:
        return 'na cabeça'

def parte_do_corpo (escolhaDePersonagem):
    if escolhaDePersonagem == 'a':
        return 'no coração'
    elif escolhaDePersonagem == 'b':
        return 'no pulmão'
    else:
        return 'no cérebro'

def sintomas_observacao (escolhaDePersonagem):
    if escolhaDePersonagem == 'a':
        return 'no coração'
    elif escolhaDePersonagem == 'b':
        return 'no pulmão'
    else:
        return 'no cérebro'

def exame (escolhaDePersonagem):
    if escolhaDePersonagem == 'a':
        return ' Ecocardiograma'
    elif escolhaDePersonagem == 'b':
        return 'a Ultrassonografia'
    else:
        return 'a Tomografia'

inicio_jogo()

personagem = escolha_personagem()

ambientacao = (f'Ao avançar em direção a {maca(personagem)} maca, uma enfermeira se aproxima com uma prancheta.')
historia = (f'[ENFERMEIRA]: Dra {medica(personagem)}, este paciente procurou a urgência com queixas de dores {dor(personagem)} há 10 dias com piora progressiva.')
texto_para_escolha = 'Agora você precisa decidir o tratamento mais adequado para o paciente, o que devemos fazer?'
resultado_exame = (f'[ENFERMEIRA]: Dra., identificamos um coágulo {parte_do_corpo(personagem)}.')
evolucao_observacao = (f'[ENFERMEIRA]: Após 6h em observação o paciente está {sintomas_observacao(personagem)} ')
evolucao_medicacao = (f'[ENFERMEIRA]: O Paciente apresentou melhora do quadro, com pressão arterial dentro da normalidade porém ainda reclama da dor {dor(personagem)}.')
evolucao_cirurgia = (f'[ENFERMEIRA]: A cirurgia correu bem, conseguimos eliminar o coágulo {sintomas_observacao(personagem)}')

opcoes_1 = (f'Opção a: Solicitar um{exame(personagem)} \nOpção b: Prescrever medicação. \nOpção c: Dispensar paciente.')
opcoes_2 = 'Opção a: Encaminhar paciente para sala de observação. \nOpção b: Encaminhar paciente para iniciar medicação. \nOpção c: Dispensar paciente com prescrição medicamentosa.'
opcoes_3 = 'Opção a: Dispensar paciente com orientação dos cuidados a serem tomados. \nOpção b: Encaminhar paciente para medicação. \nOpção c: Encaminhar paciente para cirurgia.'
opcoes_4 = 'Opção a: Dispensar o paciente. \nOpção b: Encaminhar para medicação. \nOpção c: Encaminhar para cirurgia.'
opcoes_5 = 'Opção a: Encaminhar paciente para sala de observação. \nOpção b: Os resultados estão dentro do esperado, dispense o paciente. \nOpção c: Encaminhar para cirurgia.'
opcoes_6 = 'Opção a: Dispensar paciente com orientação dos cuidados a serem tomados. \nOpção b: Encaminhar paciente para medicação. \nOpção c: Encaminhar paciente para cirurgia.'
opcoes_7 = 'Opção a: Solicitar uma Ultrassonografia \nOpção b: Prescrever medicação. \nOpção c: Dispensar paciente.'
opcoes_8 = 'Opção a: Encaminhar para cirurgia. \nOpção b: Encaminhar paciente para iniciar medicação. \nOpção c: Dispensar paciente com prescrição medicamentosa.'
opcoes_9 = 'Opção a: Dar alta a paciente. \nOpção b: Iniciar Medicação \nOpção c: Encaminhar paciente para observação.'
opcoes_10 = 'Opção a: Dispensa o paciente, não tem mais o que fazer. \nOpção b: Encaminhar paciente para medicação. \nOpção c: Recomeça a cirurgia.'
opcoes_11 = 'Opção a: Encaminhar paciente para sala de observação. \nOpção b: Encaminhar paciente para iniciar medicação. \nOpção c: Dispensar paciente.'
opcoes_12 = 'Opção a: Dispensar paciente com orientação dos cuidados a serem tomados. \nOpção b: Encaminhar paciente para medicação. \nOpção c: Encaminhar paciente para cirurgia.'
opcoes_13 = 'Opção a: Dispensar o paciente. \nOpção b: Encaminhar para medicação. \nOpção c: Encaminhar para cirurgia.'
opcoes_14 = 'Opção a: Dispensar o paciente. \nOpção b: Trocar medicação. \nOpção c: Encaminhar para cirurgia.'

if personagem == 'a':
    fase(ambientacao, historia, texto_para_escolha, opcoes_1)
    fase_2 = escolha()
    
    if fase_2 == 'a':
        fase ( '', resultado_exame,texto_para_escolha, opcoes_2)
        fase_3 = escolha()
        
        if fase_3 == 'a':
            fase ( '', evolucao_observacao,texto_para_escolha, opcoes_3)
            fase_final(escolha())
        
        elif fase_3 == 'b':
            fase( '', evolucao_medicacao,texto_para_escolha, opcoes_4)
            fase_final(escolha())
        
        else:
            fase_final('a')
    
    elif fase_2 == 'b':
        fase( '', evolucao_medicacao,texto_para_escolha, opcoes_5)
        fase_3 = escolha()
        
        if fase_3 == 'a':
            fase( '', evolucao_observacao,texto_para_escolha, opcoes_6)
            fase_final(escolha())
        
        elif fase_3 == 'c':
            fase_final('c')
        
        else:
            fase_final('b')
    
    else:
        fase_final('a')

elif personagem == 'b':
    fase(ambientacao, historia, texto_para_escolha, opcoes_1)      
    fase_2 = escolha()
    
    if fase_2 == 'a':
        fase( '', resultado_exame,texto_para_escolha, opcoes_8)
        fase_3 = escolha()
        
        if fase_3 == 'a':
            fase(evolucao_cirurgia, '', texto_para_escolha, opcoes_9)
            fase_final(escolha())
        
        elif fase_3 == 'b':                
            fase_final('b')
        
        else:
            fase_final('a')
    
    elif fase_2 == 'b':
        fase( '', evolucao_medicacao,texto_para_escolha, opcoes_1)
        fase_3 = escolha()
        
        if fase_3 == 'a':
            fase( '', resultado_exame,texto_para_escolha, opcoes_10)
            fase_final(escolha())
        
        elif fase_3 == 'b':
            fase_final('b')
        
        else:
            fase_final('a')
    
    else:
        fase_final('b')

elif personagem == 'c':
        fase(ambientacao, historia, texto_para_escolha, opcoes_1)
        fase_2 = escolha()
        
        if fase_2 == 'a':
            fase( '', resultado_exame,texto_para_escolha, opcoes_11)
            fase_3 = escolha()
            
            if fase_3 == 'a':
                fase( '', evolucao_observacao,texto_para_escolha, opcoes_12)
                fase_final(escolha())
            
            elif fase_3 == 'b':
                fase( '', evolucao_medicacao,texto_para_escolha, opcoes_13)
                fase_final(escolha())
            
            else:
                fase_final('a')
        
        elif fase_2 == 'b':
            fase( '', evolucao_medicacao,texto_para_escolha, opcoes_14)
            fase_final(escolha())
        
        else:
            fase_final('a')