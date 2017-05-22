print("Bem vindo ao Batalhas Medievais BETA! ")
print()
print("Esse jogo requer dois jogadores.")

def guia():
    print()
    print("Existem cinco classes disponíveis para escolha.")
    print("Entre elas são Mago ,Caçador ,Arqueiro ,Invocador e Padre.")
    print()
    print("A classe Mago tem como ataque principal magia de três elementos (fogo, gelo e eletricidade) ,sua fraqueza é ataque físico.")
    print("A classe Caçador tem como ataque principal o ataque fisico, sua fraqueza são as orações de condenação.")
    print("A classe Arqueiro tem como ataque principal as flechas elementares (fogo, gelo e eletricidade), sua fraqueza são seres invocados.")
    print("A classe Invocador tem como ataque principal a invocação de seres como dragões ,unicórnios alados ou o reaper (a morte), sua fraqueza são flechas elementares.")
    print("A classe Padre tem como ataque principal as orações de condenação ,sua fraqueza são magias elementares.")
    print()
    print()
    print("MAGIAS ELEMENTARES!")
    print("As magias elementares causam danos aos seguintes oponentes: ")
    print("Fogo causa dano de 20 de HP no Caçador(flecha), 30 de HP no Padre(flecha) ,Caçador(ataque) , Invocador(flecha) e 40 no Padre(ataque). Nos demais causa apenas 20 de dano no HP.")
    print("Gelo causa dano de 20 de HP no Caçador(flecha), 30 de HP no Padre(ataque), Invocador(ataque), Caçador(ataque), e 40 no Invocador(flecha). Nos demais causa apenas 20 de dano no HP.")
    print("Eletricidade causa dano de 10 no Caçador(flecha), 30 de HP no Invocador(ataque), Padre(flecha), 40 no Invocador(flecha) e no Padre(ataque). Nos demais causa apenas 20 de dano no HP.")
    print()
    print()
    print("INVOCAÇÕES!")
    print("As invocações causam danos aos seguintes oponentes: ")
    print("Dragões causa dano de 30 de HP no Arqueiro e Caçador. Nos demais causa apenas 20 de dano no HP.")
    print("Reaper (a morte) tira 1 de HP do Mago e do Padre ,e causa morte em quatro turnos neles. Pode ser previnido pela interferência divina do Padre ,mas a prevenção só funciona por um turno. Nos demais não causa dano.")
    print("Unicórnios Alados não causam danos a ninguém ,mas recuperam 30 do HP do Invocador e podem ser usados apenas uma vez por partida.")
    print()
    print()
    #print("ATAQUES ESPECIAIS!")
    #print("Os ataques especiais podem ser usados nas seguintes situações:")
    #print("1# Depois de três ataques seguidos do Caçador ou Padre")
    #print("2# Se houver tri-elementar do Arqueiro ou Mago. Tri-elementar é quando diferentes ataques elementares são jogados três vezes seguidas.")
    #print("3# Se o Invocador invocar diferentes seres, três vezes seguidas.")
    #print("O ataque especial do Mago é a magia 'Ultima' ,que aniquila qualquer oponente ,exceto o Caçador ,que perde metade do HP.")
    #print("O ataque especial do Caçador é 'A espada de Grayskull' ,que aniquila qualquer oponente ,exceto o Padre ,que perde metade do HP.")
    #print("O ataque especial do Arqueiro é 'O arco Apocalíptico' ,que aniquila qualquer oponente ,exceto o Invocador ,que perde metade do HP.")
    #print("O ataque especial do Invocador é 'Cronos' ,que aniquila qualquer oponente ,exceto o Mago ,que perde metade do HP.")
    #print("O ataque especial do Padre é a oração 'Fogueira da Heresia!' ,que aniquila qualquer oponente ,exceto o Arqueiro ,que perde metade do HP.")
    #print()
    #print()
    print("OBSERVAÇÕES!")
    print("Ataques comuns causam apenas 20 de dano no HP.")
    print("Existe um código que decide aleatoriamente quem será o primeiro a jogar.")
    print("O Padre pode curar 30 do seu HP através de orações sagradas, mas os deuses atendem até duas orações sagradas por partida.")
    print("O Padre pode usar a interferência divina somente duas vezes por partida para tirar 32 de HP do Mago ,22 de HP do Arqueiro ou previnir o Reaper (a morte) por um turno.")
    print("O Caçador pode usar a segunda chance apenas uma vez por partida ,e serve para encher o HP de ambos os jogadores.")
    print("O Caçador pode usar o escudo e perder apenas 10 de HP caso sofra um ataque comum.")


def resultados (x,y):
    global pl1
    global pl2
    global defesa
    global prays
    global uni
    global turno
    global invld
    global morte
    global nd2_chance
    global divina
    global antireaper
    global countmorte
    #MAGO
    if x == 1 and y == 2:
        print()
        atk = input("Digite 'x' para Fogo ,'o' para Gelo ou 'z' para Eletricidade: ")
        if atk == "x":
            pl2-=30
            print()
            print("O Caçador perdeu 30 do HP.")
        elif atk == "o":
            pl2-=30
            print()
            print("O Caçador perdeu 30 do HP.")
        elif atk == "z":
            if defesa:
                pl2-=10
                print()
                print("O Caçador perdeu 10 do HP.")
                defesa=False
            else:
                pl2-=20
                print()
                print("O Caçador perdeu 20 do HP.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 1 and y == 3:
        print()
        atk = input("Digite 'x' para Fogo ,'o' para Gelo ou 'z' para Eletricidade: ")
        if atk == "x" or atk == "o" or atk == "z":
            pl2-=20
            print()
            print("O Arqueiro perdeu 20 do HP.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 1 and y == 4:
        print()
        atk = input("Digite 'x' para Fogo ,'o' para Gelo ou 'z' para Eletricidade: ")
        if atk == "x":
            pl2-=20
            print()
            print("O Invocador perdeu 20 do HP.")
        elif atk == "o":
            pl2-=30
            print()
            print("O Invocador perdeu 30 do HP.")
        elif atk == "z":
            pl2-=30
            print()
            print("O Invocador perdeu 30 do HP.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 1 and y == 5:
        print()
        atk = input("Digite 'x' para Fogo ,'o' para Gelo ou 'z' para Eletricidade: ")
        if atk == "x":
            pl2-=40
            print()
            print("O Padre perdeu 40 do HP.")
        elif atk == "o":
            pl2-=30
            print()
            print("O Padre perdeu 30 do HP.")
        elif atk == "z":
            pl2-=40
            print()
            print("O Padre perdeu 40 do HP.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    #CAÇADOR
    elif x == 2 and y == 1:
        print()
        atk = input("Digite 'x' para atacar com a espada de Grayskull ,'o' para usar o escudo ou 'z' para segunda chance: ")
        if atk == 'x':
            pl2-=30
            print()
            print("O Mago perdeu 30 do HP.")
        elif atk == 'o':
            print()
            print("O Caçador se defendeu.")
            defesa = True
        elif atk == 'z':
            if not nd2_chance:
                pl1=100
                pl2=100
                nd2_chance=True
                print()
                print("--- Segunda Chance --- ")
            else:
                print()
                print("Você já usou segunda chance ,não há uma terceira ;-;")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 2 and y == 3:
        print()
        atk = input("Digite 'x' para atacar com a espada de Grayskull ,'o' para usar o escudo ou 'z' para segunda chance: ")
        if atk == 'x':
            pl2-=20
            print()
            print("O Arqueiro perdeu 20 do HP.")
        elif atk == 'o':
            print()
            print("O Caçador se defendeu.")
            defesa = True
        elif atk == 'z':
            if not nd2_chance:
                pl1=100
                pl2=100
                nd2_chance=True
                print()
                print("--- Segunda Chance --- ")
            else:
                print()
                print("Você já usou segunda chance ,não há uma terceira ;-;")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 2 and y == 4:
        print()
        atk = input("Digite 'x' para atacar com a espada de Grayskull ,'o' para usar o escudo ou 'z' para segunda chance: ")
        if atk == 'x':
            pl2-=20
            print()
            print("O Invocador perdeu 20 do HP.")
        elif atk == 'o':
            print()
            print("O Caçador se defendeu.")
            defesa = True
        elif atk == 'z':
            if not nd2_chance:
                pl1=100
                pl2=100
                nd2_chance=True
                print()
                print("--- Segunda Chance --- ")
            else:
                print()
                print("Você já usou segunda chance ,não há uma terceira ;-;")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 2 and y == 5:
        print()
        atk = input("Digite 'x' para atacar com a espada de Grayskull ,'o' para usar o escudo ou 'z' para segunda chance: ")
        if atk == 'x':
            pl2-=20
            print()
            print("O Padre perdeu 20 do HP.")
        elif atk == 'o':
            print()
            print("O Caçador se defendeu.")
            defesa = True
        elif atk == 'z':
            if not nd2_chance:
                pl1=100
                pl2=100
                nd2_chance=True
                print()
                print("--- Segunda Chance --- ")
            else:
                print()
                print("Você já usou segunda chance ,não há uma terceira ;-;")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    #ARQUEIRO
    elif x == 3 and y == 1:
        print()
        print("Escolha o elemento da flecha")
        atk = input("Digite 'x' para Fogo ,'o' para Gelo ou 'z' para Eletricidade: ")
        if atk == "x" or atk == "o" or atk == "z":
            pl2-=20
            print()
            print("O Mago perdeu 20 do HP.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 3 and y == 2:
        print()
        print("Escolha o elemento da flecha")
        atk = input("Digite 'x' para Fogo ,'o' para Gelo ou 'z' para Eletricidade: ")
        if atk == "x" or atk == "o":
            if defesa:
                pl2-=10
                print("O Caçador perdeu 10 do HP.")
            else:
                pl2-=20
                print()
                print("O Caçador perdeu 20 do HP.")
        elif atk == "z":
            if defesa:
                pl2-=4
                print()
                print("O Caçador perdeu 4 do HP.")
                defesa=False
            else:
                pl2-=10
                print()
                print("O Caçador perdeu 10 do HP.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 3 and y == 4:
        print()
        print("Escolha o elemento da flecha")
        atk = input("Digite 'x' para Fogo ,'o' para Gelo ou 'z' para Eletricidade: ")
        if atk == "x":
            pl2-=30
            print()
            print("O Invocador perdeu 30 do HP.")
        elif atk == "o":
            pl2-=40
            print()
            print("O Invocador perdeu 40 do HP.")
        elif atk == "z":
            pl2-=40
            print()
            print("O Invocador perdeu 40 do HP.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 3 and y == 5:
        print()
        print("Escolha o elemento da flecha")
        atk = input("Digite 'x' para Fogo ,'o' para Gelo ou 'z' para Eletricidade: ")
        if atk == "x":
            pl2-=30
            print()
            print("O Padre perdeu 30 do HP.")
        elif atk == "o":
            pl2-=20
            print()
            print("O Padre perdeu 20 do HP.")
        elif atk == "z":
            pl2-=30
            print()
            print("O Padre perdeu 30 do HP.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    #INVOCADOR
    elif x == 4 and y == 1:
        print()
        print("Escolha a invocação")
        atk = input("Digite 'x' para Dragões ,'o' para Reaper(a morte) ou 'z' para Unicórnios Alados: ")
        if atk == "x":
            pl2-=20
            print()
            print("O Mago perdeu 20 do HP.")
        elif atk == "o":
            pl2-=1
            morte=True
            print()
            print("O Mago recebeu a condenação de quatro turnos e perdeu 1 de HP.")
        elif atk == "z":
            if uni:
                if pl1 == 100:
                    print()
                    print("O Invocador já está na capacidade máxima de HP")
                    uni=False
                elif pl1 <= 70:
                    pl1+=30
                    print()
                    print("O Invocador ganhou 30 de HP.")
                    uni=False
                else:
                    pl1=100
                    print()
                    print("O Invocador encheu o HP.")
                    uni=False
            else:
                print()
                print("Você pode invocar os unicórnios alados apenas uma vez.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 4 and y == 2:
        print()
        print("Escolha a invocação")
        atk = input("Digite 'x' para Dragões ,'o' para Reaper(a morte) ou 'z' para Unicórnios Alados: ")
        if atk == "x":
            pl2-=30
            print()
            print("O Caçador perdeu 30 do HP.")
        elif atk == "o":
            print()
            print("O Caçador não perdeu nada de HP.")
        elif atk == "z":
            if uni:
                if pl1 == 100:
                    print()
                    print("O Invocador já está na capacidade máxima de HP")
                    uni=False
                elif pl1 <= 70:
                    pl1+=30
                    print()
                    print("O Invocador ganhou 30 de HP.")
                    uni=False
                else:
                    pl1=100
                    print()
                    print("O Invocador encheu o HP.")
                    uni=False
            else:
                print()
                print("Você pode invocar os unicórnios alados apenas uma vez.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 4 and y == 3:
        print()
        print("Escolha a invocação")
        atk = input("Digite 'x' para Dragões ,'o' para Reaper(a morte) ou 'z' para Unicórnios Alados: ")
        if atk == "x":
            pl2-=30
            print()
            print("O Arqueiro perdeu 30 do HP.")
        elif atk == "o":
            print()
            print("O Arqueiro não perdeu nada de HP.")
        elif atk == "z":
            if uni:
                if pl1 == 100:
                    print()
                    print("O Invocador já está na capacidade máxima de HP")
                    uni=False
                elif pl1 <= 70:
                    pl1+=30
                    print()
                    print("O Invocador ganhou 30 de HP.")
                    uni=False
                else:
                    pl1=100
                    print()
                    print("O Invocador encheu o HP.")
                    uni=False
            else:
                print()
                print("Você pode invocar os unicórnios alados apenas uma vez.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 4 and y == 5:
        print()
        print("Escolha a invocação")
        atk = input("Digite 'x' para Dragões ,'o' para Reaper(a morte) ou 'z' para Unicórnios Alados: ")
        if atk == "x":
            pl2-=20
            print()
            print("O Padre perdeu 20 do HP.")
        elif atk == "o":
            if not antireaper:
                pl2-=1
                morte=True
                print()
                print("O Padre recebeu a condenação de quatro turnos e perdeu 1 de HP.")
            else:
                print()
                print("A interferência divina previniu a morte.")
                countmorte+=1
        elif atk == "z":
            if uni:
                if pl1 == 100:
                    print()
                    print("O Invocador já está na capacidade máxima de HP")
                    uni=False
                elif pl1 <= 70:
                    pl1+=30
                    print()
                    print("O Invocador ganhou 30 de HP.")
                    uni=False
                else:
                    pl1=100
                    print()
                    print("O Invocador encheu o HP.")
                    uni=False
            else:
                print()
                print("Você pode invocar os unicórnios alados apenas uma vez.")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    #PADRE
    elif x == 5 and y == 1:
        print()
        print("Escolha a oração")
        atk = input("Digite 'x' para as orações de condenação ,'o' para fazer oração sagrada ou 'z' para interferência divina: ")
        if atk == 'x':
            pl2-=20
            print()
            print("O Mago perdeu 20 do HP.")
        elif atk == 'o':
            if prays != 2:
                if pl1 == 100:
                    print()
                    print("O Padre já está na capacidade máxima de HP")
                elif pl1 <= 70:
                    pl1+=30
                    print()
                    print("O Padre ganhou 30 de HP.")
                    prays+=1
                else:
                    pl1=100
                    print()
                    print("O Padre encheu o HP.")
                    prays+=1
            else:
                print()
                print("Os deuses já não ouvem mais suas orações de cura ;-;")
        elif atk == 'z':
            if divina != 2:
                pl2-=32
                print()
                print("O Mago perdeu 32 de HP.")
                divina+=1
            else:
                print()
                print("Os deuses já não ouvem mais suas orações de inteferência ;-;")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 5 and y == 2:
        print()
        print("Escolha a oração")
        atk = input("Digite 'x' para as orações de condenação ,'o' para fazer oração sagrada ou 'z' para interferência divina: ")
        if atk == 'x':
            pl2-=30
            print()
            print("O Caçador perdeu 30 do HP.")
        elif atk == 'o':
            if prays != 2:
                if pl1 == 100:
                    print()
                    print("O Padre já está na capacidade máxima de HP")
                elif pl1 <= 70:
                    pl1+=30
                    print()
                    print("O Padre ganhou 30 de HP.")
                    prays+=1
                else:
                    pl1=100
                    print()
                    print("O Padre encheu o HP.")
                    prays+=1
            else:
                print()
                print("Os deuses já não ouvem mais suas orações de cura ;-;")
        elif atk == 'z':
            if divina != 2:
                print()
                print("O Caçador não perdeu nada de HP.")
                divina+=1
            else:
                print()
                print("Os deuses já não ouvem mais suas orações de inteferência ;-;")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 5 and y == 3:
        print()
        print("Escolha a oração")
        atk = input("Digite 'x' para as orações de condenação ,'o' para fazer oração sagrada ou 'z' para interferência divina: ")
        if atk == 'x':
            pl2-=20
            print()
            print("O Arqueiro perdeu 20 do HP.")
        elif atk == 'o':
            if prays != 2:
                if pl1 == 100:
                    print()
                    print("O Padre já está na capacidade máxima de HP")
                elif pl1 <= 70:
                    pl1+=30
                    print()
                    print("O Padre ganhou 30 de HP.")
                    prays+=1
                else:
                    pl1=100
                    print()
                    print("O Padre encheu o HP.")
                    prays+=1
            else:
                print()
                print("Os deuses já não ouvem mais suas orações de cura ;-;")
        elif atk == 'z':
            if divina != 2:
                pl2-=22
                print()
                print("O Arqueiro perdeu 22 de HP.")
                divina+=1
            else:
                print()
                print("Os deuses já não ouvem mais suas orações de inteferência ;-;")
        else:
            print()
            print("Jogada inválida.")
            invld=True
    elif x == 5 and y == 4:
        print()
        print("Escolha a oração")
        atk = input("Digite 'x' para as orações de condenação ,'o' para fazer oração sagrada ou 'z' para interferência divina: ")
        if atk == 'x':
            pl2-=20
            print()
            print("O Invocador perdeu 20 do HP.")
        elif atk == 'o':
            if prays != 2:
                if pl1 == 100:
                    print()
                    print("O Padre já está na capacidade máxima de HP")
                elif pl1 <= 70:
                    pl1+=30
                    print()
                    print("O Padre ganhou 30 de HP.")
                    prays+=1
                else:
                    pl1=100
                    print()
                    print("O Padre encheu o HP.")
                    prays+=1
            else:
                print()
                print("Os deuses já não ouvem mais suas orações de cura ;-;")
        elif atk == 'z':
            if divina != 2:
                antireaper=True
                print()
                print("Os deuses baniram o Reaper por 1 turno.")
                divina+=1
            else:
                print()
                print("Os deuses já não ouvem mais suas orações de inteferência ;-;")
        else:
            print()
            print("Jogada inválida.")
            invld=True

while True:
    guia2 = input("Digite o número zero para ver o guia ,ou pressione enter para continuar.")
    if guia2 == "0":
        guia()
        break
    else:
        break
defesa=False
pl1=100
pl2=100
uni=True
acabou=False
t3=False
prays=0
divina=0
condenado=0
countmorte=0
morte=False
nd2_chance=False
antireaper=False
while True:
    if acabou:
        print()
        fechar = input("Pressione enter se você quer jogar novamente, ou digite zero para sair.")
        if fechar == "0":
            break
        else:
            pl1=100
            pl2=100
            prays=0
            divina=0
            condenado=0
            countmorte=0
            morte=False
            defesa=False
            uni=True
            nd2_chance=False
            antireaper=False
    ok=True
    ok2=True
    ok3=True
    print()
    print("Para escolher a classe digite 1 para Mago, 2 para Caçador, 3 para Arqueiro , 4 para Invocador ou 5 para Padre")
    print()
    classe=input("Selecione a classe do player 1: ")
    if classe != '1' and classe != '2' and classe != '3' and classe != '4' and classe != '5':
        print()
        print("Seleção inválida!")
        ok=False
    if ok:
        classe2=input("Selecione a classe do player 2: ")
        if classe2 != '1' and classe2 != '2' and classe2 != '3' and classe2 != '4' and classe2 != '5':
            print()
            print("Seleção inválida!")
            ok2=False
        if ok2:
            if classe == classe2:
                print()
                print("Jogadores devem ter classes diferentes.")
                ok3=False
            if ok3:
                if classe == '1':
                    j1="Mago"
                elif classe == '2':
                    j1="Caçador"
                elif classe == '3':
                    j1="Arqueiro"
                elif classe == '4':
                    j1="Invocador"
                elif classe == '5':
                    j1="Padre"
                if classe2 == '1':
                    j2="Mago"
                elif classe2 == '2':
                    j2="Caçador"
                elif classe2 == '3':
                    j2="Arqueiro"
                elif classe2 == '4':
                    j2="Invocador"
                elif classe2 == '5':
                    j2="Padre"
                invld=False
                import random
                sort = random.randint(1,2)
                if sort == 1:
                    turno = True
                    print()
                    print('Parabéns player 1 |'+j1+'| ,o python escolheu você para jogar primeiro!!')
                elif sort == 2:
                    turno = False
                    print()
                    print('Parabéns player 2 |'+j2+'| ,o python escolheu você para jogar primeiro!!')
                while True:
                    if invld:
                        if turno:
                            turno=False
                        else:
                            turno=True
                    if turno:
                        if pl1 == 0 and pl2 == 0:
                            print()
                            print("O jogo empatou !_!")
                            acabou = True
                            break
                        elif pl1 == 0:
                            print()
                            print("O %s GANHOU!"%j1)
                            acabou = True
                            break
                        elif pl2 == 0:
                            print()
                            print("O %s GANHOU!"%j2)
                            acabou = True
                            break
                    else:
                        if pl1 == 0 and pl2 == 0:
                            print()
                            print("O jogo empatou !_!")
                            acabou = True
                            break
                        if pl2 == 0:
                            print()
                            print("O %s GANHOU!"%j1)
                            acabou = True
                            break
                        elif pl1 == 0:
                            print()
                            print("O %s GANHOU!"%j2)
                            acabou = True
                            break
                    if turno:
                        print()
                        print("Vez do %s"%j1)
                        turno=False
                        if not invld:
                            if t3:
                                inter=pl2
                                pl2=pl1
                                pl1=inter
                        if morte and pl1%2==1:
                            condenado+=1
                        if countmorte == 1:
                            antireaper=False
                        invld=False
                        classe=int(classe)
                        classe2=int(classe2)
                        resultados(classe,classe2)
                        if pl1 < 0:
                            pl1=0
                        if pl2 < 0:
                            pl2=0
                        if condenado == 4:
                            pl1=0
                            print()
                            print("%s foi condenado pelo Reaper!"%j1)
                        print()
                        print("HP do %s: %d"%(j1,pl1))
                        print("HP do %s: %d"%(j2,pl2))
                    else: 
                        print()
                        print("Vez do %s"%j2)
                        turno=True
                        t3=True
                        if not invld:
                            inter=pl1
                            pl1=pl2
                            pl2=inter
                        if morte and pl1%2==1:
                            condenado+=1
                        if countmorte == 1:
                            antireaper=False
                        invld=False
                        classe=int(classe)
                        classe2=int(classe2)
                        resultados(classe2,classe)
                        if pl1 < 0:
                            pl1=0
                        if pl2 < 0:
                            pl2=0
                        if condenado == 4:
                            pl1=0
                            print()
                            print("%s foi condenado pelo Reaper!"%j1)
                        print()
                        print("HP do %s: %d"%(j1,pl2))
                        print("HP do %s: %d"%(j2,pl1))
