from collections import Counter, defaultdict

class Solution:
    def __init__(self):
        self.s = ""
        self.wordLength = 0

    def skipStartWord(self, found: dict[str, int], count: int, start: int) -> tuple[dict[str, int], int, int]:
        startWord = self.s[start:start+self.wordLength]
        found[startWord] -= 1
        count -= 1
        start += self.wordLength
        return found, count, start

    def initializeWordSearchValues(self, tempLeft: int) -> tuple[dict[str, int], int, int]:
        found = defaultdict(int)
        count = 0
        right = tempLeft + self.wordLength
        return found, count, right

    """
    Optimized sliding window:
    - Since all words have the same length (let's say length=3), divide the string into groups 
      starting at positions 0, 1, and 2. This ensures all possible word positions are checked.
    - Example: For "barfoothefoo" and word length 3:
       - Group 0: [bar][foo][the][foo]
       - Group 1: [arf][oot][hef][oo-]
       - Group 2: [rfo][oth][efo][o--]
    - For each group, slide window one word at a time, keeping track of:
       - Words found
       - Occurences of each word
    - Skip invalid words that aren't in our word list
    - When match is found, remember it for the next slide
    - Adjust our window when a word is seen more than its needed

    Time: O(len(s)*wordLength)
	Space: O(len(words))
	"""
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        self.s = s
        self.wordLength = wordLength = len(words[0])
        wordsCounter = Counter(words)
        indexes = []
        for left in range(0, wordLength):
            start = tempLeft = left
            wordsFound, wordsCount, right = self.initializeWordSearchValues(tempLeft)
            while right <= len(s):
                word = s[tempLeft:right]
                if word not in wordsCounter:
                    start = tempLeft + wordLength
                    tempLeft += wordLength
                    wordsFound, wordsCount, right = self.initializeWordSearchValues(tempLeft)
                    continue

                wordsFound[word] += 1
                wordsCount += 1
                while wordsFound[word] > wordsCounter[word]:
                    wordsFound, wordsCount, start = self.skipStartWord(
                        wordsFound, wordsCount, start
                    )

                if wordsCount == len(words):
                    indexes.append(start)
                    wordsFound, wordsCount, start = self.skipStartWord(
                        wordsFound, wordsCount, start
                    )

                tempLeft += wordLength
                right = tempLeft+wordLength

        return indexes

    '''
    Brute force approach:
    - Checks every possible starting position in string s
    - For each position, tries to match all words consecutively
    - Uses a counter to track word frequencies and ensure no word is used more times than available

    Time: O(len(s) * wordLength * len(words))
    Space: O(len(words))
    '''
    def findSubstringInitial(self, s: str, words: list[str]) -> list[int]:
        wordLength = len(words[0])
        wordsCounter = Counter(words)
        indexes = []
        for left in range(0, len(s)):
            right = left + wordLength * len(words)
            if right > len(s):
                break
            wordsUsed = 0
            wordsFound = defaultdict(int)
            for leftTemp in range(left,right,wordLength):
                word = s[leftTemp:leftTemp+wordLength]
                if word not in wordsCounter:
                    break
                wordsUsed += 1
                wordsFound[word] += 1
                if wordsFound[word] > wordsCounter[word]:
                    wordsUsed -= 1
                    break
            if wordsUsed == len(words):
                indexes.append(left)
        return indexes
