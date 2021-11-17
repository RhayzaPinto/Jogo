def inicio_jogo ():
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

def escolha():
    opcao = input('Digite a letra da opção escolhida: ')
    return opcao

def escolha_personagem():
    print('MACA a: Paciente relata fortes dores no peito \nMACA b: Paciente diz que constantemente sente muita falta de ar. \nMACA c: Paciente não identificado, visivelmente confuso.')
    paciente_escolhido = escolha()
    return paciente_escolhido

def fase_final(acao_escolhida):
    if acao_escolhida == 'a':
        print('[ENFERMEIRA]: Dra., o paciente acabou de retornar a emergência, infelizmente veio a falecer no caminho pois sofreu pois o socorro não chegou a tempo.')
    elif acao_escolhida == 'b':
        print('[ENFERMMEIRA]: Dra., a medicação recomendada não foi precisa e o paciente precisou ser encaminhado para a UTI')
    else:
        print('[ENFERMEIRA]: Parabéns Dra.! A cirurgia foi um sucesso e o paciente se recupera bem')


def texto_para_escolha():
    print('Agora você precisa decidir o tratamento mais adequado para o paciente, o que devemos fazer?')

inicio_jogo()
aux = 0

while aux != 1:

    personagem = escolha_personagem()   
     
    if personagem == 'a':
        aux = 1
        print('Ao avançar em direção a primeira maca, uma enfermeira se aproxima com uma prancheta.')
        print('[ENFERMEIRA]: Dra Cristina Jovem, este paciente procurou a urgência com queixas de “forte dor no peito” há 10 dias com piora progressiva agravada após moderado esforço físico. Dura pouco tempo e melhora logo após repouso.')
        texto_para_escolha()
        print('Opção a: Solicitar um Ecocardiograma \nOpção b: Prescrever medicação. \nOpção c: Dispensar paciente com orientação sob orientação de não praticar atividade física.')
        fase_2 = escolha()
        if fase_2 == 'a':
            print('[ENFERMEIRA]: Dra., identificamos um desnivelamento supra do segment ST de 2mm na parede anterior.')
            texto_para_escolha()
            print('Opção a: Encaminhar paciente para sala de observação. \nOpção b: Encaminhar paciente para iniciar medicação. \nOpção c: Dispensar paciente com prescrição medicamentosa.')
            fase_3 = escolha()
            if fase_3 == 'a':
                print('[ENFERMEIRA]: Dra., após 6h sob observação, c.')
                texto_para_escolha()
                print('Opção a: Dispensar paciente com orientação dos cuidados a serem tomados. \nOpção b: Encaminhar paciente para medicação. \nOpção c: Encaminhar paciente para cirurgia.')
                fase_final(escolha())
            elif fase_3 == 'b':
                print('[ENFERMEIRA]: O Paciente apresentou melhora do quadro, com pressão arterial dentro da normalidade porém ainda reclama da dor no peito.')
                texto_para_escolha()
                print('Opção a: Dispensar o paciente. \nOpção b: Encaminhar para medicação. \nOpção c: Encaminhar para cirurgia.')
                fase_final(escolha())
            else:
                print('[ENFERMEIRA]: Dra., o paciente acabou de retornar a emergência, infelizmente veio a falecer no caminho pois sofreu um infarto agudo do miocárdio e o socorro não chegou a tempo.')
        elif fase_2 == 'b':
            print('[ENFERMEIRA]: Dra., o paciente relata melhora da dor no peito, porém diz ter um sentimento de angústia, suspeitamos de efeito colateral da medicação.')
            texto_para_escolha()
            print('Opção a: Encaminhar paciente para sala de observação. \nOpção b: Os resultados estão dentro do esperado, dispense o paciente. \nOpção c: Encaminhar para cirurgia.')
            fase_3 = escolha()
            if fase_3 == 'a':
                print('[ENFERMEIRA]: Dra., após 6h sob observação, o paciente desenvolveu aumento da pressão arterial.')
                texto_para_escolha()
                print('Opção a: Dispensar paciente com orientação dos cuidados a serem tomados. \nOpção b: Encaminhar paciente para medicação. \nOpção c: Encaminhar paciente para cirurgia.')
                fase_final(escolha())
            elif fase_3 == 'c':
                fase_final('c')
            else:
                fase_final('b')
        else:
            fase_final('a')
    elif personagem == 'b':
        aux = 1
        print('Ao avançar em direção a segunda maca, uma enfermeira se aproxima com uma prancheta.')
        print('[ENFERMEIRA]: Dra Livia Wesley, Esta paciente tem 13 anos, deu entrada no hospital apresentando quadro de pneumonia bacteriana que inicialmente foi tratada com antibióticos.')
        texto_para_escolha()
        print('Opção a: Solicitar uma Ultrassonografia \nOpção b: Encaminhar para cirurgia. \nOpção c: Prescrever medicação.')
        fase_2 = escolha()
        if fase_2 == 'a':
            print('[ENFERMEIRA]: Dra., Lívia  a ultrassonografia constatou acúmulo de líquido na região pleural.')
            texto_para_escolha()
            print('Opção a: Encaminhar para cirurgia. \nOpção b: Encaminhar paciente para iniciar medicação. \nOpção c: Dispensar paciente com prescrição medicamentosa.')
            fase_3 = escolha()
            if fase_3 == 'a':
                print('Foi feita adrenagem de todo o líquido na cavidade pleural')
                texto_para_escolha()
                print('Opção a: Dar alta a paciente. \nOpção b: Iniciar Medicação \nOpção c: Encaminhar paciente para observação.')
                fase_final(escolha())
            elif fase_3 == 'b':                
                fase_final('b')
            else:
                fase_final('a')
        elif fase_2 == 'b':
            print('Ao abrir a cavidade torácica, Dra. Lívia constatou que a situação era mais grave que o esperado...')
            texto_para_escolha()
            print('Opção a: Desiste da operação e solicita mais exames. \nOpção b: Realiza a cirurgia mesmo assim. \nOpção c: Desiste da cirurgia e avisa que a paciente está em estado terminal.')
            fase_3 = escolha()
            if fase_3 == 'a':
                print('[ENFERMEIRA]: Dra., o exame constatou que o acúmulo de líquido se concentra na parte superior esquerda.')
                texto_para_escolha()
                print('Opção a: Dispensa o paciente, não tem mais o que fazer. \nOpção b: Encaminhar paciente para medicação. \nOpção c: Recomeça a cirurgia.')
                fase_final(escolha())
            elif fase_3 == 'b':
                print('A cirurgia foi muito complicada e demorou bem mais que o necessário. A paciente precisará ficar na UTI pra se recuperar totalmente.')
            else:
                print('O pais vão procurar outro médico para dar prosseguimento ao tratamento.')
        else:
            fase_final('b')
    else:
        aux = 1
        print('Ao avançar em direção a terceira maca, uma enfermeira se aproxima com uma prancheta.')
        print('[ENFERMEIRA]: Dra Meredith Cinza, este paciente foi trazido por estranhos a emergência após cair na rua e não se lembrar do nome e falar coisas desconexas.')
        texto_para_escolha()
        print('Opção a: Solicitar uma tomografia \nOpção b: Prescrever medicação. \nOpção c: Dispensar paciente, ele deve melhorar.')
        fase_2 = escolha()
        if fase_2 == 'a':
            print('[ENFERMEIRA]: Dra., identificamos um rompimento de um vaso cerebral.')
            texto_para_escolha()
            print('Opção a: Encaminhar paciente para sala de observação. \nOpção b: Encaminhar paciente para iniciar medicação. \nOpção c: Dispensar paciente.')
            fase_3 = escolha()
            if fase_3 == 'a':
                print('[ENFERMEIRA]: Dra., após 6h sob observação, o paciente aparentemente se lembra de seu nome, mas continua muito confuso.')
                texto_para_escolha()
                print('Opção a: Dispensar paciente com orientação dos cuidados a serem tomados. \nOpção b: Encaminhar paciente para medicação. \nOpção c: Encaminhar paciente para cirurgia.')
                fase_final(escolha())
            elif fase_3 == 'b':
                print('[ENFERMEIRA]: O Paciente está convulsionando.')
                texto_para_escolha()
                print('Opção a: Dispensar o paciente. \nOpção b: Encaminhar para medicação. \nOpção c: Encaminhar para cirurgia.')
                fase_final(escolha())
            else:
                print('[ENFERMEIRA]: Dra., o paciente acabou de retornar a emergência, infelizmente veio a falecer no caminho pois sofreu um AVC e o socorro não chegou a tempo.')
        elif fase_2 == 'b':
            print('[ENFERMEIRA]: O Paciente está convulsionando.')
            texto_para_escolha()
            print('Opção a: Dispensar o paciente. \nOpção b: Trocar medicação. \nOpção c: Encaminhar para cirurgia.')
            fase_final(escolha())            
        else:
            fase_final('a')