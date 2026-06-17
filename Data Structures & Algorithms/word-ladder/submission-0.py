# Word Ladder
# You are given two words, beginWord and endWord, and also a list of words wordList. All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.

# Your goal is to transform beginWord into endWord by following the rules:

# You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
# You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
# Return the minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        alphabets = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        wordset = set(wordList)
        
        if endWord not in wordset: #beginWord may not be as per test case
            return 0

        def nextWords(word) -> List[str]:
            nextwords = []

            for i in range(len(word)):
                for letter in alphabets:
                    if letter == word[i : i + 1]:
                        continue

                    possibleWord = word[:i] + letter + word[i + 1 :]
                    if possibleWord in wordset:
                        nextwords.append(possibleWord)

            return nextwords

        # applying BFS
        q = deque([beginWord])
        visited = set([beginWord])

        transform_count = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
            
                if word == endWord: return transform_count

                for nextWord in nextWords(word):
                    if nextWord not in visited:
                        q.append(nextWord)
                        visited.add(nextWord)
            
            transform_count += 1
        
        return 0

