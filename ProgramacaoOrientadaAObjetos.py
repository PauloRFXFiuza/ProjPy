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
    
    #Para acessar atributos privados, utiliza-se o get
    def get_fabricante_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
    
    #Para acessar atributos privados não definidos, utiliza-se o set

if __name__ == '__main__':
    meu_veiculo = Veiculo('GM' , 'Cadillac Escalade')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabricante_modelo()
    
