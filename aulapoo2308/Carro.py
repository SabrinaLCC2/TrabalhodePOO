class Carro:

    cor : str
    modelo : str
    marca: str
    ano : int
    

    def __init__(self, cor, modelo, marca,ano): 
        self.cor = cor
        self.modelo = modelo
        self.ano = ano 
        self.marca = marca

    def frear(self):
        print(f"O Carro de cor {self.cor}, modelo {self.marca}, e Ano {self.ano}  efetuou uma frenagem")
    
    def frente (self):
        print("Executou o método")
    
    def re (self):
        print("Executou o método")    
        
    def correr(self):
        print("Executou o método")
        

def somar (v1,v2):
        somar=v1+v2
        print(soma)

