class Pessoa:
  def __init__(self, altura, idade):
    self.altura = altura
    self.idade = idade
  
  def correr(self):
    print(f"Pessoa está correndo com a altura de {self.altura}")
  
  def comer(self, comida):
    return f"Com {self.idade} anos, voce come {comida} ?"
  
pessoa = Pessoa(1.75, 31)
pessoa.correr()
response = pessoa.comer("lasanha")
print(response)
