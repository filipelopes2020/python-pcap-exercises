class Dog():
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        
my_pet = Dog('Teddy', 2)
print(my_pet.__dict__)
print(my_pet.age)
print(my_pet._Dog__name)

# ------
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado

    def depositar(self, valor):
        self.__saldo += valor

    def obter_saldo(self):
        return self.__saldo

conta = ContaBancaria(1000)
#conta.saldo=50001
conta._ContaBancaria__saldo = 20000  # não recomendado, mas possível

conta.depositar(500)
print(conta._ContaBancaria__saldo)
print(conta.obter_saldo())  # 1500  porque o saldo é private na class por isso nao permite alterar o saldo diretamente


