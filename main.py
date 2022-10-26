from Torre import Torre
from Disco import Disco

torre1 = Torre()
torre2 = Torre()
torre3 = Torre()


def iniciar_jogo():
    print("\033[1;34mTORRE DE HANÓI\033[0m\n")


def escolher_quantia_discos():
    quantia_discos = int(input("\033[34mDigite a quantia de discos desejada:\033[0m\n"))
    if quantia_discos >= 3 and quantia_discos <= 7:

        for i in range(1, quantia_discos + 1):
            torre1.empilha(Disco(i))
        torre1.to_string()
    else:
        print("Quantia inválida. Escolha entre 3 a 7 discos")
        escolher_quantia_discos()

def movimentar_discos(torre_origem, torre_destino):
    disco_movimentado = Torre.desempilha(torre_origem)
    torre_destino.inserir(disco_movimentado)
    Torre.to_string(torre_origem)
    Torre.to_string(torre_destino)
    

if __name__ == '__main__':
    iniciar_jogo()
    escolher_quantia_discos()
    jogo_finalizado = False
    
    while not jogo_finalizado:
        torre_origem = int(input("\033[1;34mDe qual torre deseja mover?\033[0m\n"))
        torre_destino = int(input("\033[1;34mPara qual torre deseja transferir?\033[0m\n"))
        
        if torre_origem == 1:
            torre_origem = torre1
        elif torre_origem == 2:
            torre_origem = torre2
        elif torre_origem == 3:
            torre_origem = torre3
        else: 
            print("Torre inválida")
        
        if torre_destino == 1:
            torre_destino = torre1
        elif torre_destino == 2:
            torre_destino = torre2
        elif torre_destino == 3:
            torre_destino = torre3
        else: 
            print("Torre inválida")
            
        movimentar_discos(torre_origem, torre_destino)
            
        if torre1.get_tamanho() == 0 and torre2.get_tamanho() == 0:
            jogo_finalizado = True
            print("\033[1;34m\n★★★PARABÉNS, VOCÊ FINALIZOU A TORRE DE HANÓI ★★★\033[0m\n")
            



    

       

       
