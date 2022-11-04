from locale import normalize
from typing import Dict, List, Tuple


SENTIMENT_DICT = {
    "POS": ["like", "great", "thank", "love"],
    "POS2": ["🙂", "❤️"],
    "NEG2": ["😡", "😞"],
    "NEG": ["failed"],
}

class WordProcessor:
    case_sensitive: bool
    no_punct: bool
    text: str
    words: List[str]

    def __init__(self, case_sensitive: bool, no_punct: bool) -> None:
        self.case_sensitive = case_sensitive
        self.no_punct = no_punct
        self.text = ""
        self.words = []

    def set_text(self, text: str) -> None:
        self.text = text

        self.words = text.split(" ")

    def count_words(self) -> Dict[str, int]:

        words = self.words

        if not self.case_sensitive:
            words = [w.lower() for w in words]

        if self.no_punct:
            words = [
                w for w in words if w not in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
            ]

        c: Dict[str, int] = {}

        for w in words:
            if w not in c:
                c[w] = 1
            else:
                c[w] = c[w] + 1

        return c

    # def add2i(self,a:int,b:int):
    #     return a+b

    def _sentiment_count(self) -> Tuple[int, int]:
        words = self.words
        words = [w.lower() for w in words]
        words = [w for w in words if w not in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""]

        total_sentiment, normalizer = 0, 0

        for w in words:
            if w in SENTIMENT_DICT["POS"]:
                total_sentiment += 1
                normalizer += 1

            if w in SENTIMENT_DICT["POS2"]:
                total_sentiment += 2
                normalizer += 1

            if w in SENTIMENT_DICT["NEG"]:
                total_sentiment -= 1
                normalizer += 1

            if w in SENTIMENT_DICT["NEG2"]:
                total_sentiment -= 2
                normalizer += 1

        return total_sentiment, normalizer

    def sentiment(self) -> float:
        total_sentiment, normalizer = self._sentiment_count()

        return total_sentiment / max(normalizer, 1)


wp = WordProcessor(case_sensitive=False, no_punct=False)
wp2 = WordProcessor(case_sensitive=False, no_punct=True)
wp3 = WordProcessor(case_sensitive=True, no_punct=True)

print(wp.case_sensitive)
print(wp.no_punct)

comments = [
    "I like this product !",
    "Python is great",
    "Thank you 🙂",
    "😡 I will give up using this",
    "❤️ Love it",
    "😡 not like",
    "Failed for the second time 😞",
    "Bye . Find other users",
]

# I expect this to retun a dict of works.  Such as , {'The': 1, 'the':1, 'quick':1}
wp.set_text("The quick fox jumps over the lazy dog .")
print(wp.count_words())


for c in comments:
    wp.set_text(c)
    print(f"'{c}' Sentiment: {wp.sentiment()}")
