class PlayerCharacter():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def run(self):
		return self

	@classmethod
	def dodaj(cls, num1, num2):
		return num1 + num2

player1 = PlayerCharacter("Greg", 43)

print(PlayerCharacter.dodaj(4,9))