class MinhaClasse:
  def __init__(self,info, elem): # Metodo Construtor é o primeiro a ser executado
    self.atributo_1 = "meu atributo"
    self.atributo_3 = [1,2,"a"]
    self.new_atribute = info
    self.atributo_2 = elem
    print(self.new_atribute)
  # Metodos
  def metodo_1(self):
    print("Minha acao1")
    print("Minha acao2")
    print(self.atributo_2)
    return "Olá Mundo"
  
  def metodo_2(self, numero):
    self.metodo_1()
    print(self.atributo_3[1] + numero)
# Objeto       #Classe -> instanciamos um objeto
minha_classe = MinhaClasse("info aqui no construtor", 231)
#minha_classe.metodo_1()
reponse = minha_classe.metodo_1()
print(reponse)
minha_classe.metodo_2(3)