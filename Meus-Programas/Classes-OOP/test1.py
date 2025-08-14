class User:
    def __init__(self, nickname, city):
        self.nickname = nickname
        self.city = city
    def introduce(self):    
        print('Hello, my name is',self.nickname,'and I am from ',self.city)

first_user = User('Joao', 'Faro')
second_user = User('Joquim', 'Lisboa')
third_user = User('Rui', 'Tavira')
first_user.introduce()
second_user.introduce()
third_user.introduce()
# Example of using the User class

#print(sample_user.nickname)
#print(sample_user.city)

#