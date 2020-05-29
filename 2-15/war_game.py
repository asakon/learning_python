from random import shuffle

class Card:
    # カード種別であるスートと、values
    # このリストを使ってカード種別を表現する
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9",
                    "10", "Jack", "Queen", "King", "Ace"]
    
    # カードは、値とスートで定まる
    def __init__(self, v, s):
        self.value = v
        self.suit = s

    # カードは、勝敗を判定するための特殊メソッドを持つ
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self. value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self. value == c2.value:
            return self.suit > c2.suit
        return False

    # カードが自身を表現する特殊メソッド
    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    # デッキは、カードのリストを持つ。カードはshuffleされる。
    # また、カードのリストはだんだん減っていくので（ゲームが終わりに近づく）、
    # カードを切り出すインスタンスメソッドを持つ。
    def __init__(self):
        self.cards = []
        for i in range (2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            # return None
            return
        return self.cards.pop()

class Player:
    # プレイヤーは勝ち数、持っているカード、名前をインスタンス変数として持つ
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    # Gameはデッキと２人のプレイヤーを持つ
    def __init__(self):
        name1 = input("プレイヤー1の名前　")
        name2 = input("プレイヤー2の名前　")
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    # Gameは、
    # ゲームをプレイするメソッド、
    # プレイする中で使用されるメソッドがある
    #  - 引いたカードを表示するメソッド
    #  - ラウンド毎の勝者を表示するメソッド
    #  - ゲームの最後に、勝者を判定して名前を告げるメソッド

    def print_draw(self, player1, player2):
        d = "{} は {}、 {} は {} を引きました"
        print(d.format(player1.name, player1.card, player2.name, player2.card))
    
    def print_winner(self, winner):
        w = "このラウンドは {} が勝ちました"
        print(w.format(winner.name))
    
    def game_winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        if player1.wins < player2.wins:
            return player2.name
        return "引き分け！"
    
    def play_game(self):
        cards = self.deck.cards
        print("ゲーム開始！")

        while len(cards) >= 2:
            message = "qで終了、それ以外のキーでプレイ:"
            response = input(message)
            if response == 'q':
                break
            
            self.player1.card = self.deck.draw()
            self.player2.card = self.deck.draw()

            #player1name = self.player1.name
            #player2name = self.player2.name

            self.print_draw(self.player1 , self.player2)

            if self.player1.card > self.player2.card:
                self.player1.wins += 1
                self.print_winner(self.player1)
            else:
                self.player2.wins += 1
                self.print_winner(self.player2)
 
        win = self.game_winner(self.player1, self.player2)
        print("ゲーム終了、{} の勝利です！".format(win))


game = Game()
game.play_game()
    