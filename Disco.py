class Disco:
    def __init__(self, tamanho):
        self._tamanho = tamanho

    def get_tamanho(self):
        return self._tamanho

    def to_string(self):
        print('Disco: ' + str(self._tamanho))
        
    
