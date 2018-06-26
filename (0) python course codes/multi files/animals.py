class dog:
    numOfDogs = 0
    def __init__(self,n,col,eyecol,l=30,w=1,nationality='jp'):   # l,w default if not passed
        dog.numOfDogs +=1
        self.color = col      
        self.eyecolor = eyecol
        self.length = l
        self.weight = w
        self.name = n
        self.nat = nationality
    
    def run(self):
        print(self.name,' is running now')
    
    def sit(self,command):
        if command == 'Ni Haw' and self.nat == 'jp':
            print(self.name , 'is sitting now and Nihow daw ')
        elif command == 'sit' and self.nat == 'br':
            print(self.name,'is sitting now and happy')
        elif command == 'ray7' and self.nat == 'egy':
            print(self.name,'marmt nafso fel tena :D')
        else:
            print(self.name,'didnt got it')
            
def add(x,y):
    print(x+y)