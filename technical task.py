#Class
class Player:
    def __init__(self,name,lives):
        self._name = name
        self._lives = lives
        self._score = 0

    def turn(self,num):
        print(self._name,"'s turn:")
        if num%3 == 0 and num%5 != 0:
            correct = 'fizz'
        elif num%5 == 0 and num%3 != 0:
            correct = 'buzz'
        elif num%3 == 0 and num%5 == 0:
            correct = 'fizz buzz'
        else:
            correct = str(num)
        ans = input('Please enter the next value: ')
        if ans == correct:
            print('Correct!')
            num += 1
            self._score += 1
            return num
        else:
            print('Incorrect!')
            self._lives -= 1
            return num
            
    def outOfLives(self):
        if self._lives == 0:
            return True
        else:
            return False

    def displayResults(self):
        print(self._name,"'s results:")
        print('Lives left:',self._lives)
        print('Score:', self._score)
        return self._score

#Explaining the Game
print('Welcome to the FizzBuzz game!')
print('This game requires two players to count up from 1, however:')
print("1) If the number is divisible by 3, the player must input 'fizz'")
print("2) If the number is divisible by 5, the player must input 'buzz'")
print("3) If the number is divisible by 3 and 5, the player must input 'fizz buzz'")
print('You can choose how many lives you have from 1 to 5')
print()
print('Here is an example round:')
print('Player1: >1')
print('This answer is correct because the count starts from one')
print('Player2: >2')
print('This answer is correct because the count increases by one every *correct* turn')
print('Player1: >3')
print('This answer is incorrect because 3 is divisible by 3')
print('The correct answer is: fizz')
print()
print('Numbers replaced by fizz include: 3,6,9')
print('Numbers replaced by buzz include: 5,10')
print('Numbers replaced by fizz buzz include: 15')
print()
        
#Creating players
player1name = input('Player 1, please input your name: ')
player2name = input('Player 2, please input your name: ')
valid = False
while valid == False:
    lives = input('How many lives would you like to have(1 - 5): ')
    if lives.isnumeric() == True:
        if int(lives) >= 1 and int(lives) <= 5:
            lives = int(lives)
            valid = True

player1 = Player(player1name,lives)
player2 = Player(player2name,lives)

#Gameplay
num = 1
endOfGame = False
while endOfGame == False:
    num = Player.turn(player1,num)
    noLives = Player.outOfLives(player1)
    if noLives == True:
        endOfGame = True
    else:
        num = Player.turn(player2,num)
        noLives = Player.outOfLives(player2)
        if noLives == True:
            endOfGame = True

score1 = Player.displayResults(player1)
score2 = Player.displayResults(player2)
if score1 > score2:
    print(player1name, 'won!')
elif score2 > score1:
    print(player2name, 'won!')
else:
    print("It's a tie!")
