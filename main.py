from Torre import Torre
from Disco import Disco

torre1 = Torre()
torre2 = Torre()
torre3 = Torre()


def iniciar_jogo():
    print("\033[1;34mTORRE DE HANÓI\033[0m\n")


def escolher_quantia_discos():
    quantia_discos = int(
        input("\033[34mDigite a quantia de discos desejada:\033[0m\n"))
    if quantia_discos >= 3 and quantia_discos <= 7:

        for i in range(1, quantia_discos + 1):
            torre1.empilha(Disco(i))
        torre1.to_string()
    else:
        print("Quantia inválida. Escolha entre 3 a 7 discos")
        escolher_quantia_discos()


if __name__ == '__main__':
    iniciar_jogo()
    escolher_quantia_discos()
    
    while True:
        select_torre_origem = int(input("\033[1;34mDe qual torre deseja mover?\033[0m\n"))
        select_torre_destino = int(input("\033[1;34mPara qual torre deseja transferir?\033[0m\n"))

        if select_torre_origem == 1 and select_torre_destino == 2:
            disco_movimentado = torre1.desempilha()
            torre2.empilha(disco_movimentado)
            torre1.to_string()
            torre2.to_string()
        elif select_torre_origem == 1 and select_torre_destino == 3:
            disco_movimentado = torre1.desempilha()
            torre3.empilha(disco_movimentado)
            torre1.to_string()
            torre3.to_string()
        elif select_torre_origem == 2 and select_torre_destino == 1:
            disco_movimentado = torre2.desempilha()
            torre1.empilha(disco_movimentado)
            torre2.to_string()
            torre1.to_string()
        elif select_torre_origem == 2 and select_torre_destino == 3:
            disco_movimentado = torre2.desempilha()
            torre3.empilha(disco_movimentado)
            torre2.to_string()
            torre3.to_string()
        elif select_torre_origem == 3 and select_torre_destino == 1:
            disco_movimentado = torre3.desempilha()
            torre1.empilha(disco_movimentado)
            torre3.to_string()
            torre1.to_string()
        elif select_torre_origem == 3 and select_torre_destino == 2:
            disco_movimentado = torre3.desempilha()
            torre2.empilha(disco_movimentado)
            torre3.to_string()
            torre2.to_string()
        else:
            print('opção inválida')



    

       

       
