#########################################
##### Name: <Lingyun Xu>            #####
##### Uniqname:<lingyunx>           #####
#########################################

import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)


    # Add methods below to test main assignments. 
    # Test that if you create a card with rank 12, its rank_name will be "Queen"
    def test_1_queen(self):
        card = cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")


    # Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
    def test_2_clubs(self):
        card = cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")


    # Test that if you invoke the __str__ method of a card instance 
    # that is created with suit=3, rank=13, it returns the string "King of Spades"
    def test_3_str(self):
        card = cards.Card(suit=3, rank=13)
        self.assertEqual(str(card), "King of Spades")


    # Test that if you create a deck instance, it will have 52 cards in its 
    # cards instance variable
    def test_4_deck(self):
        card = cards.Deck()
        self.assertEqual(len(card.cards), 52)


    # Test that if you invoke the deal_card method on a deck, it will return a card instance.
    def test_5_deal(self):
        d1 = cards.Deck()
        c1 = d1.deal_card()
        self.assertIsInstance(c1, cards.Card)


    # Test that if you invoke the deal_card method on a deck, the deck has one fewer cards 
    # in it afterwards.
    def test_6_deal(self):
        d1 = cards.Deck()
        length1 = len(d1.cards)
        d1.deal_card()
        length2 = len(d1.cards)
        self.assertEqual(length1-length2, 1)
        

    # Test that if you invoke the replace_card method, the deck has one more card 
    # in it afterwards. (Please note that you want to use deal_card function first 
    # to remove a card from the deck and then add the same card back in)
    def test_7_replace(self):
        d1 = cards.Deck()
        len1 = len(d1.cards)
        d1.deal_card()
        c1 = d1.deal_card()
        len2 = len(d1.cards)
        d1.replace_card(c1)
        len3 = len(d1.cards)
        self.assertEqual(len3-len2, 1)


    # Test that if you invoke the replace_card method with a card that is already in 
    # the deck, the deck size is not affected.(The function must silently ignore it 
    # if you try to add a card that’s already in the deck)
    def test_8_replace(self):
        d1 = cards.Deck()
        len1 = len(d1.cards)
        c1 = cards.Card()
        if c1 in d1.cards:
            d1.replace_card(c1)
            len2 = len(d1.cards)
            self.assertEqual(len2-len1, 0)


############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
