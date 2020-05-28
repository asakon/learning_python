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
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self. value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
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

    def pop_card(self):
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
        #name1 = inpur("プレイヤー1の名前　")
        #name2 = inpur("プレイヤー2の名前　")
        self.deck = Deck()
        self.player1 = Player(input("プレイヤー1の名前　"))
        self.player2 = Player(input("プレイヤー2の名前　"))

    # Gameは、
    # ゲームをプレイするメソッド、
    # プレイする中で使用されるメソッドがある
    #  - カードを引くメソッド
    #  - ラウンド毎の勝者を宣言するためのメソッド
    #  - ゲームの最後に、勝者を判定して名前を告げるメソッド

    def draw(self, player1, player1card, player2, player2card):
        d = "{} は {}、 {} は {} を引きました"
        print(d.format(player1, player1card, player2, player2card))
    
    def declear_winner_round(self, winner):
        w = "このラウンドは {} が勝ちました"
        print(w.format(winner))
    
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
            
            player1card = self.deck.pop_card()
            player2card = self.deck.pop_card()

            player1name = self.player1.name
            player2name = self.player2.name

            self.draw(player1name , player1card, player2name , player2card)

            if player1card > player2card:
                self.player1.wins += 1
                self.declear_winner_round(player1name)
            else:
                self.player2.wins += 1
                self.declear_winner_round(player2name)
 
        win = self.game_winner(self.player1, self.player2)
        print("ゲーム終了、{} の勝利です！".format(win))


game = Game()
game.play_game()
    