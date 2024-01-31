import yaml
from dataclasses import dataclass
from db_iching_model import Trigram, Hexagram, Nonagram
@dataclass
class IChing:
    trigrams = []
    hexagrams = []
    nonagrams = []
    path = ""
    data = None

    def __init__(self, path='../bl.data/db_iching.yaml', data=None, build=True, build_nonagrams=True):

        self.path = path
        if self.path not in ["", None]:
            self.data = self.load()
        
        if data is not None:
            self.data = data

        if (self.data) is None:
            raise Exception("path or data must be provided")

        if build:
            self.build(self.data)

        if build_nonagrams: 
            self.build_nonagrams(self.trigrams, self.hexagrams)

    def load(self):
        with open(self.path, 'r') as file:
            data = yaml.safe_load(file)
        
        return data

    def trigram_from_xor(self, top_trigram, bottom_trigram):
        pivot = {trigram.bin: trigram for trigram in self.trigrams}
        middle_trigram =  pivot[top_trigram.bin ^ bottom_trigram.bin]
        return middle_trigram

    def build(self, data):
        self.trigrams = []
        self.hexagrams = []
        self.nonagrams = []
        trigrams_by_number = {}        

        for trigram_data in data['trigrams']:
            trigram = Trigram(**trigram_data)
            trigrams_by_number[trigram.number] = trigram

            self.trigrams.append(trigram)

        for hexagram_data in data['hexagrams']:
            hexagram = Hexagram(
                **hexagram_data,
                top_trigram = trigrams_by_number[hexagram_data['topTrigram']],
                bottom_trigram = trigrams_by_number[hexagram_data['bottomTrigram']])
            self.hexagrams.append(hexagram)

    def build_nonagrams(self, trigrams, hexagrams): 
        for hexagram in hexagrams:
            middle_trigram = self.trigram_from_xor(hexagram.top_trigram, hexagram.bottom_trigram)
            self.nonagrams.append(Nonagram(
                **hexagram.__dict__,
                middle_trigram=middle_trigram,
                middleTrigram=middle_trigram.number))

__all__ = ['IChing']
