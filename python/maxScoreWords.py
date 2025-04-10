# https://leetcode.com/problems/maximum-score-words-formed-by-letters/

from typing import List

class Solution:
    # w = len(words)
    # l = len(letters)
    # Time: O(2^w * l)
    # Space: O(2^w * l)
    def __init__(self):
        self.maxScore = 0
        self.allLetters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        lettersToScores = {}
        for l, s in zip(self.allLetters, score):
            if l in letters:
                lettersToScores[l] = s

        self.maxScore = 0
        def exploreAllWordsCombo(i, remainingLetters, score):
            if i == len(words):
                return

            # Don't take word
            exploreAllWordsCombo(i+1, remainingLetters, score)

            # Take word
            newRemainingLetters = remainingLetters.copy()
            newScore = score
            for letter in words[i]:
                if letter not in newRemainingLetters:
                    return
                newRemainingLetters.remove(letter)
                newScore += lettersToScores[letter]
            self.maxScore = max(self.maxScore, newScore)
            exploreAllWordsCombo(i+1, newRemainingLetters, newScore)
        exploreAllWordsCombo(0, letters, 0)
        return self.maxScore
