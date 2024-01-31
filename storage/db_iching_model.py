from dataclasses import dataclass
from termios import TIOCPKT_START
from typing import Any, List
import math

#create domain -> color mapping

@dataclass
class Trigram:  
    number: int
    names: List[str]
    chineseName: str
    pinyinName: str
    character: str
    attribute: str
    images: List[str]
    chineseImage: str
    pinyinImage: str
    familyRelationship: str
    binary: str
    lines: List[int]

    @property
    def bin(self):
        return int(self.binary, 2)
    @property
    def domain(self):
        return self.images[0]
    
    @property 
    def color_hex(self):
        return self.bin << 5
    
    #todo: add a property for the color of the trigram's domain
    @property
    def color_domain(self):
        mapping = {
            'heaven':   '#FFFFFF',
            'thunder':  '#FFFF00',
            'earth':    '#AAAAAA',
            'water':    '#00FFFF',
            'fire':     '#FF0000',
            'swamp':    '#008000',
            'mountain': '#FF00FF',
            'wind':     '#00FFFF',
        }

        return mapping[self.domain]
        

    
@dataclass
class Hexagram:
    number: int
    names: List[str]
    chineseName: str
    pinyinName: str 
    character: str
    binary: str
    lines: List[int]    
    topTrigram: int
    bottomTrigram: int
    top_trigram: 'Trigram'
    bottom_trigram: 'Trigram'


@dataclass
class Nonagram:
    number: int
    names: List[str]
    chineseName: str
    pinyinName: str 
    character: str
    binary: str
    lines: List[int]    
    topTrigram: int
    bottomTrigram: int
    top_trigram: 'Trigram'
    bottom_trigram: 'Trigram'
    middleTrigram: int
    middle_trigram: 'Trigram'    


    @property
    def color_hex(self):
        r = self.top_trigram.color_hex      #| self.top_trigram.bin
        g = self.middle_trigram.color_hex   #| self.middle_trigram.bin
        b = self.bottom_trigram.color_hex   #| self.bottom_trigram.bin
        return f'#{r:02x}{g:02x}{b:02x}'

__all__ = ['Trigram', 'Hexagram', 'Nonagram']
