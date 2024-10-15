class Pessoa:
  def __init__(self, altura, cpf) -> None:
    self.altura = altura
    self.__cpf = cpf # Atributo Privado
    
  def apresentar(self):
    print(f"Olá! Minha altura - {self.altura}")
    self.__coletar_documento()
  
  def __coletar_documento(self): # Método privado
    print(f"Meu documento - {self.__cpf}")

jorge = Pessoa("1.70", "12345678909")
jorge.apresentar()
