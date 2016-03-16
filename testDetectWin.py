import unittest
import detectWin

"""
 if isStraightFlush(cards):
        return 8
    elif isFourOfAKind(cards):
        return 7
    elif isFullHouse(cards):
        return 6
    elif isFlush(cards):
        return 5
    elif isStraight(cards):
        return 4
    elif isThreeOfAKind(cards):
        return 3
    elif isTwoPair(cards):
        return 2
    elif isPair(cards):
        return 1
    else:
        return 0

"""

class TestDetectWin(unittest.TestCase):

    def test_countSuits(self):
        cards = ["H2", "H3", "H4", "H5", "S2", "S3", "C2"]
        count = detectWin.countSuits(cards)
        self.assertEquals(count["H"], 4)
        self.assertEquals(count["S"], 2)
        self.assertEquals(count["C"], 1)
        self.assertFalse("D" in count)

    def test_countNumber(self):
        cards = ["H2", "H3", "H4", "H5", "S2", "S3", "C2"]
        count = detectWin.countNumbers(cards)
        self.assertEquals(count[2], 3)
        self.assertEquals(count[3], 2)
        self.assertEquals(count[4], 1)
        self.assertEquals(count[5], 1)


    def test_countContainsGroup(self):
        count = {"1": 1, "2": 2, "3": 3}
        self.assertTrue(detectWin.countContainsGroup(count, 3))
        self.assertFalse(detectWin.countContainsGroup(count, 3))


    # def test_isStraightFlush(self):
    #     cards = ["H8","H9", "C3", "H10", "S2", "H6", "H7"]
    #     expected = 8
    #     result = detectWin.getHandRank(cards)
    #     self.assertEqual(expected, result)

    def test_isFourOfAKind(self):
        cards = ["H4", "S10", "C4", "D10", "S4", "H10", "D4"]
        expected = 7
        result = detectWin.getHandRank(cards)
        self.assertEqual(expected, result)

    def test_isFullHouse(self):
        cards = ["H2", "S2", "C5", "D5", "C3", "D3", "H3"]
        expected = 6
        result = detectWin.getHandRank(cards)
        self.assertEqual(expected, result)

    def test_isFlush(self):
        cards = ["H2", "H4", "D3", "H6", "H8", "S3", "H10"]
        expected = 5
        result = detectWin.getHandRank(cards)
        self.assertEqual(expected, result)

    # def test_isStraight(self):
    #     cards = ["H2", "S3", "C3", "C4", "D5", "H13"]
    #     expected = 4
    #     result = detectWin.getHandRank(cards)
    #     self.assertEqual(expected, result)

    def test_isThreeOfAKind(self):
        cards = ["H3", "D3", "C3", "S2", "C10", "D5", "S11"]
        expected = 3
        result = detectWin.getHandRank(cards)
        self.assertEqual(expected, result)

    def test_isTwoPair(self):
        cards = ["H2", "C8", "D2", "S10", "D4", "C10", "H6"]
        expected = 2
        result = detectWin.getHandRank(cards)
        self.assertEqual(expected, result)

    def test_isPair(self):
        cards = ["H2", "D4", "H6", "C2", "C8", "S10", "C12"]
        expected = 1
        result = detectWin.getHandRank(cards)
        self.assertEqual(expected, result)

    def test_isNothing(self):
        cards = ["H2", "D4", "H6", "C8", "S10", "C12", "H14"]
        expected = 0
        result = detectWin.getHandRank(cards)
        self.assertEqual(expected, result)

    def test_detectWin_oneEnemyWins_oneEnemyLoses(self):
        jsonDict = {"river": ["C4", "C5", "C9", "H8", "S14"],
                    "me": ["H10", "S10"],
                    "ops": [
                        ["H2", "S3"],
                        ["C2", "C7"]
                    ]}
        self.assertFalse(detectWin.checkWin(jsonDict))

    def test_detectWin_myWin(self):
        pass
