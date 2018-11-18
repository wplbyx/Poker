#!/usr/bin/env python
# coding=utf-8

import random
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Poker:
    """ docstring for Poker """
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}
    
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in self.ranks 
                                       for suit in self.suits]
    
    def __repr__(self):
        """ show poker object as string """
        msg = [str(card) for card in self.cards]
        return '\n'.join(msg)
    
    def __len__(self):
        return len(self.cards)
        
    def __getitem__(self, position):
        return self.cards[position]
    
    
def sort_height(card):
    """ sort as height to poker """
    rank_value = Poker.ranks.index(card.rank)  # 当前卡片的点数大小
    suit_value = Poker.suit_values[card.suit]  # 当前卡片的花色大小
    return rank_value * len(Poker.suit_values) + suit_value
    
    
if __name__ == '__main__':
    """ Poker.py model file test """
    some_card = Card(3, 'spades')
    print('Card type is: {card}'.format(card=some_card))
    
    poker = Poker()
    print(poker)
    # print('poker type is: {}, and lenght is: {}'.format(poker, len(poker)))
    # print(poker[32])
    # for idx, card in enumerate(poker[5:21]):
    #     print('{:<3} in poker is  {}'.format(idx, card))
    
    card_tmp = random.choice(poker)  # 随机选取一张扑克牌卡片
    print('The random selection card is {}'.format(card_tmp))
    
    print('排序扑克牌大小')
    for card in sorted(poker, key=sort_height):
        print(card)
    
