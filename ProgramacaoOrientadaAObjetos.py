'''
Orientação a Objetos: paradigma de programação
Classes e Objetos
'''
#Com atributos públicos - Exemplo: fabricante, modelo
'''
class Veiculo:
    def movimentar(self):
        print(f'Automovel movido a gasolina')

    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.num_registro = None

if __name__ == '__main__':
    meu_veiculo = Veiculo('GM' , 'Cadillac Escalade')
    meu_veiculo.movimentar()
    print(meu_veiculo.fabricante)
    print(meu_veiculo.modelo)
'''    
#Com atributos privados - Exemplo: __fabricante , __modelo
class Veiculo:
    def movimentar(self):
        print(f'Automovel movido a gasolina')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    #Para acessar atributos privados não definidos para inserir dados, utiliza-se o set
    def set_num_registro(self, num_registro):
        self.__num_registro = num_registro

    #Para acessar atributos privados, utiliza-se o get
    def get_fabricante_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
    
    def get_num_registro(self):
        return self.__num_registro
    
#Conceito de Herança

class Carro(Veiculo):
    #Método __init__ será herdado da classe Veiculo
    def movimentar(self):
        print(f'Veiculo de passeio')

class Motocicleta(Veiculo):
    #Método __init__ será herdado da classe Veiculo
    def movimentar(self):
        print(f'Motocicleta de passeio')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__categoria = categoria
        #super() indica quais métodos serão herdados de Veiculo
        super().__init__(fabricante , modelo)

    def get_categoria(self):
        return self.__categoria

    def movimentar(self):
        print(f'Aviao para voos domesticos')

if __name__ == '__main__':
    meu_veiculo = Veiculo('GM' , 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabricante_modelo()
    meu_veiculo.set_num_registro('32546121-9')
    print(f'Registro: {meu_veiculo.get_num_registro()}.\n')

    meu_carro = Carro('Volkswagen','Up')
    meu_carro.movimentar()
    meu_carro.get_fabricante_modelo()

    outro_carro = Carro('Hyundai','HB20')
    outro_carro.movimentar()
    outro_carro.get_fabricante_modelo()

    moto1 = Motocicleta('Honda' , 'CG125')
    moto1.movimentar()
    moto1.get_fabricante_modelo()

    aviao1= Aviao('Boeing', '747', 'Comercial')
    aviao1.movimentar()
    aviao1.get_fabricante_modelo()
    print(f'Categoria: {aviao1.get_categoria()}\n.')



    
