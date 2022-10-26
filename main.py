from Disco import Disco
from Torre import Torre

# def movimentar_torre(self, torre_origem, torre_desino):
#     disco_movimentado = Torre.desempilha(torre_origem)
#     torre_desino.empilha(disco_movimentado)
    
if __name__ == '__main__':
    torre  = Torre()
    torre2 = Torre()
    torre3 = Torre()

    print("\033[1;34mTORRE DE HANOI\033[0m\n")
    qtde_disco = int(input("Qual a quantidade de disco?\n"))

    for i in range(1, qtde_disco + 1):
        torre.empilha(Disco(i))
        
    torre.to_string()
   

while True:
    select_torre_mover = int(input("\033[1;34mDe qual torre deseja mover?\033[0m\n"))
    select_torre_transferir = int(input("\033[1;34mPara qual torre deseja transferir?\033[0m\n"))
    
    # movimentar_torre()
    if select_torre_mover == 1 and select_torre_transferir == 3:
        disco_movimentado = torre.desempilha()
        torre3.empilha(disco_movimentado)
        torre.to_string()
        torre3.to_string()
    elif select_torre_mover == 3 and select_torre_transferir == 1:
        disco_movimentado = torre3.desempilha()
        torre.empilha(disco_movimentado)
        torre3.to_string()
        torre.to_string()
       
       
       
       
       
       
    # elif select_torre_mover == 2 and select_torre_transferir == 1:
    #     disco_movimentado = torre2.desempilha()
    #     torre.empilha(disco_movimentado)
    #     torre2.to_string()
    #     torre.to_string()
    # elif select_torre_mover == 2 and select_torre_transferir == 3:
    #     disco_movimentado = torre2.desempilha()
    #     torre3.empilha(disco_movimentado)
    #     torre2.to_string()
    #     torre3.to_string()
    # elif select_torre_mover == 3 and select_torre_transferir == 1:
    #     disco_movimentado = torre3.desempilha()
    #     torre.empilha(disco_movimentado)
    #     torre3.to_string()
    #     torre.to_string()
    # elif select_torre_mover == 3 and select_torre_transferir == 2:
    #     disco_movimentado = torre3.desempilha()
    #     torre2.empilha(disco_movimentado)
    #     torre3.to_string()
    #     torre2.to_string()
    # elif jogo_finalizado() == True:
    #     break
    # else:
    #     print('opção inválida')

    
        
