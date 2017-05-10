Name: Coty Hamilton

Email: cotyhamilton@gmail.com

Assignment: Final

Due: 10 May @ 12:00 p.m.

---


`# https://github.com/rugbyprof/2143-ObjectOrientedProgramming/blob/master/Resources/python_cheatsheet.md`


**`Question 1:`**

``` python
# http://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item-in-python

def dirReduc(path):

    numY = min(path.count("NORTH"),path.count("SOUTH"))
    numX = min(path.count("EAST"),path.count("WEST"))

    for x in range(numY):
        path.remove("NORTH")
        path.remove("SOUTH")

    for x in range(numX):
        path.remove("EAST")
        path.remove("WEST")

    return path

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

# prints: ['WEST']

```

**`Question 2:`**

``` python
def tickets(money):
    bank = []

    for x in range(len(money)):
        # reverse sort bank to iterate through it later and subtract largest values first
        bank.sort(reverse=True)
        bank.append(money[x])

        change = money[x] - 25

        i = 0
        while i < len(bank):
            if change >= bank[i]:
                change -= bank[i]
                del bank[i]
            else:
                i += 1
        
        if change != 0:
            return False

    return True

print(tickets([25, 25, 50, 100, 25, 50, 25]))

# prints: True

```



**`Question 3:`**
``` python
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "[%d,%d]" % (self.x, self.y) 

class Shape(object):
    def __init(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def area(self):
        pass
```

**`Question 4:`**
``` python
def isDup(s):
    listOfDup = []
    s = s.lower()

    for x in range(1, len(s)):
        if s[x] in s[0:x]:
            if s[x] not in listOfDup:
                listOfDup.append(s[x])
    return(len(listOfDup))

s = "Indivisibi2lities2ww"

print(isDup(s))

# prints: 4
```


**`Question 5:`**
``` python
def isConsec(conList):
    for x in range(1, len(conList)):
        if abs(conList[x] - conList[x-1]) != 1:
            return conList[x]
    return None

print(isConsec([-2,-1,0,1,2,3,4,6,7,8]))

# prints: 6
```


**`Question 6:`**
``` python

class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return '%s %s' % (self.firstname, self.lastname)

class Parent(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
        self.children = []

    def addChild(self, firstname, lastname):
        child = Child(firstname, lastname)
        child.parent = self
        self.children.append(child)
    
    def get_children(self):
        return [x.get_name() for x in self.children]

class Child(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)
        self.parent = None

    
Coty = Parent("Coty", "Hamilton")
Coty.addChild("John", "Hamilton")
Coty.addChild("Other", "Hamilton")
print('Parent\'s name is %s' % Coty.get_name())
print('Coty\'s children are %s' % Coty.get_children())
print('Child\'s parent is %s' % Coty.children[0].parent.get_name())

# prints :
    # Parent's name is Coty Hamilton
    # Coty's children are ['John Hamilton', 'Other Hamilton']
    # Child's parent is Coty Hamilton
```


**`Question 7:`**
``` python
import random

class RouletteWheel(object):
    def __init__(self):
        self.wheel = []
        self.buildWheel()
    
    def __buildWheel(self):
        self.wheel.extend(({"number": "0", "color": "green"}, {"number": "00", "color": "green"}))
        for x in range(1, 11):
            if x % 2 == 0:
                self.wheel.extend(({"number": x, "color": "black"}, {"number": x + 18, "color": "black"}))
            else:
                self.wheel.extend(({"number": x, "color": "red"}, {"number": x + 18, "color": "red"}))
        for x in range(11,19):
            if x % 2 == 0:
                self.wheel.append({"number": x, "color": "red"})
            else:
                self.wheel.append({"number": x, "color": "black"})
        for x in range(26, 37):
            if x % 2 == 0:
                self.wheel.append({"number": x, "color": "red"})
            else:
                self.wheel.append({"number": x, "color": "black"})
    
    def spin(self):
        return random.choice(self.wheel)

class RouletteTable(object):
    def __init__(self):
        bets = {}
        self.__buildBets()
    
    def __buildBets(self):
        # key is name of bet, value is tuple of a list of winning numbers and the payout
        bets["0"] = (["0"], 35)
        bets["00"] = (["00"], 35)
        # ...
        bets["Row"] = (["0", "00"], 17)
        # ... 
        bets["3rd Dozen"] = ([25,26,27,28,29,30,31,32,33,34,35,36], 2)

class Player(object):
    def __init__(self, name, bank):
        self.name = name
        total_bank = bank
        current_bet_amount = 0
        current_bet = None

    def makeBet(self):
        # get input from user, either name of bet
        #   or list of numbers to bet on
        # set current bet and amount
        # subtract bet from total_bank
        return current_bet

class Game(object):
    def __init__(self, name = "Coty", bank = 34 ):
        self.wheel = RouletteWheel
        self.table = RouletteTable
        self.player = Player(name, bank)
        self.__play()

    def __play(self):
        while self.player.total_bank != 0:
            bet = self.player.makeBet()
            # if bet is a list of numbers player wants to bet on
            # determine if numbers can be comined in edge or corner bets
                # and do something about that
                pay = self.__get_payout(bet)

            # if bet is a string (name of bet), assign to bet
            #   a list of numbers corresponding to name from self.table

                pay = self.table[bet][1]
            
            win = self.table.spin()
            if win['number'] in bet:
                self.player.total_bank += (self.payout(self.player.current_bet_amount, pay))

            # ask player if they want to continue
            # break if not

        # print winners name, bank, number of rounds and stuff

    def __get_payout(self, bet):
        # calculate payout based on number of values in list

    def payout(p_bet, pay):
        return p_bet * pay
        # or however this works, I dont know
```
