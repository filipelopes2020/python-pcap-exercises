class User:
    def __init__(self, nickname, city):
        self.nickname = nickname
        self.city = city
    def introduce(self):    
        print('Hello, my name is',self.nickname,'and I am from ',self.city)

sample_user = User('Joao', 'Faro')
sample_user.introduce()
print(sample_user.nickname)
print(sample_user.city)

