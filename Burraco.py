import random
#TODO


class deck(object):
    """Deck of cards"""
    def __init__(self):
        super(deck, self).__init__()
        self.mazo = range(104)
        self.mazo.extend(['J' for _ in range(6)])
        random.shuffle(self.mazo)
        self.mazo.reverse()
        print self.mazo

    def takeCard(self):
        """returns the next card"""
        return self.mazo.pop()
    def easyPrint(self,card):
        """Printing cards as they are"""
        #print "card is :" +str(card)
        pinta=""
        carta=""
        if card =="J":
            pinta = "Joker"
        elif card < 13 or (card > 51 and card < 65):
            pinta="Pica"
        elif (card > 12 and card < 26) or (card > 64 and card < 78):
            pinta = "Trebol"
        elif (card > 25 and card < 39) or (card > 77 and card < 91):
            pinta = "Corazon"
        elif (card > 38 and card < 52) or (card > 90 and card < 104):
            pinta = "Diamante"
        if card =="J":
            carta ="Mono"
        elif (card % 13) == 1:
            carta = "Mono"
        else:
            carta = (card % 13)+1
        return [carta,pinta]
    
class jugador(object):
    """docstring for jugador"""
    def __init__(self, name):
        super(jugador, self).__init__()
        self.name = name
        self.mano = []
    def addCard(self,card):
        """Add a card to a players hand"""
        if isinstance(card,int):
            self.mano.append(card)
        else:
            self.mano.extend(card)
        self.mano.sort()
        
class juego(object):
    """Nuevo Juego de Buraco"""
    def __init__(self):
        super(juego, self).__init__()
        self.mazo = deck()
        self.jugadores=[]
        self.turno=0
        self.dealer=0
        self.buracos=[[-1 for x in xrange(11)] for x in xrange(2)]
    def addPlayer(self,player):
        """Method for adding players to a game"""
        if len(self.jugadores) < 4:
            self.jugadores.append(jugador(player))
    def printStatus(self):
        """Prints status of game"""
        print "mazo status: "
        for cards in map(self.mazo.easyPrint,self.mazo.mazo):
            print cards
        for buracos in self.buracos:
            print "Burraco - "
            for cards in map(self.mazo.easyPrint,buracos):
                print cards
                #pass
        for player in self.jugadores:
            print "Player :"+ player.name
            for cards in map(self.mazo.easyPrint,player.mano):
                print cards

    def cut(self):
        """Cut the deck """
        cutline = random.randint(4,110)
        print "cutline set at "+str(cutline)
        return self.mazo.mazo[:cutline],self.mazo.mazo[cutline:]
    
    def deal(self):
        """Deals one card and removes it from the deck"""
        cutter = (self.turno -1)%4
        bur,deal = self.cut()
        self.mazo.mazo = deal
        monos=0
        #busco monos en el corte.
        for card in bur[-4:]:
            if "Mono" in self.mazo.easyPrint(card):
                monos+=1
                self.jugadores[cutter].addCard(card)
                bur.remove(card)
        if len(self.mazo.mazo)>=44:
            for i in range(44):
                j=i%4
                if monos != 0 and cutter == j:
                    monos -=1
                else:
                    self.jugadores[j].addCard(self.mazo.takeCard())
            bur.extend(self.mazo.mazo)
            self.mazo.mazo= bur
            self.mazo.mazo.reverse()
            for i in range(22):
                self.buracos[i%2][i%11]=self.mazo.takeCard()
        else:
            bur.extend(self.mazo.mazo)
            self.mazo.mazo = bur
            self.mazo.mazo.reverse()
            for i in range(22):
                self.buracos[i%2][i%11]=self.mazo.takeCard()
            for i in range(44):
                j=i%4
                if monos != 0 and cutter == j:
                    monos -=1
                else:
                    self.jugadores[j].addCard(self.mazo.takeCard())
                        
    def start(self):
        """Start the game"""
        #player to the left cuts
        self.deal()
            
def main():
    """docstring for main"""
    game = juego()
    game.addPlayer("Charles")
    game.addPlayer("Alejandra")
    game.addPlayer("Amarilis")
    game.addPlayer("Andres")
    game.start()
    game.printStatus()
	
if __name__ == '__main__':
	main()