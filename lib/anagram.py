# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagrams = []

        for candidate in word_list:
            if self._is_anagram(candidate):
                anagrams.append(candidate)

        return anagrams

    def _is_anagram(self, candidate):
        return sorted(self.word.lower()) == sorted(candidate.lower())

