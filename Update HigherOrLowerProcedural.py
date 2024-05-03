# Higher or Lower
import random

# 카드 상수
 SUIT_TUPLE = ('Spreads', 'Hearts', 'Diamonds', 'Clubs')
 RANK_TUPLE = ('Age', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

 NCARDS = 8

 # 입력받은 카드 덱에서 임의로 한 장의 카드를 선택해 반환한다.
def getCard(deckListIn):
    thisCard = deckListIn.pop() # 카드 덱 맨 위의 카드를 꺼내서 반환한다.
    return thisCard

# 입력받은 카드 덱을 복사 한 후 복사본을 무작위로 뒤섞어 반환한다.
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

# main
print('Higher or Lower 게임에 오신 것을 환영합니다.')
print('여러분은 다음에 보일 카드가 현재 카드보다 크거나 작은지 선택해야 합니다.')
print('맞힌다면 20점을 얻고 틀린다면 15점 감점됩니다.')
print('처음에는 50점이 주어집니다.')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = { 'rank': rank, 'suit': suit, 'value': thisValue + 1 }
        startingDeckList.append(cardDict)

score = 50

while True: # 게임을 여러번 플레이
    print()
    gameDeckList = shuffle(startingDeckList)
    correntCardDict = getCard(gameDeckList)
    correntCardRank = correntCardDict['rank']
    correntCardValue = correntCardDict['value']
    correntCardSuit = correntCardDict['suit']
    print('카드 덱 가장 위의 카드 등급은 ',correntCardRank + ', 문양은 ' + correntCardSuit + ' 입니다.')
    print()