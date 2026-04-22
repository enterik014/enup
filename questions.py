from typing import TypedDict, NotRequired, Literal
import datetime

context_type = Literal['title', 'image', 'text', 'source']

class Alternative(TypedDict):
    letter: Literal['A', 'B', 'C', 'D', 'E']
    text: str
    file_path: NotRequired[str]

class Context(TypedDict):
    type: context_type
    text: NotRequired[str]
    file_path: NotRequired[str]

class Question():
    def __init__(self):
        self.year = 0
        self.number = 0
        self.correct_alternative = 'A'
        self.statement = ''
        self.context: list[Context] = []
        self.alternatives: list[Alternative] = []
    
    def add_context(self, type: context_type, text=None, path=None):
        self.context.append({
            'type': type,
            'text': text,
            'file_path': path
        })
    
    def add_alternative(self, text=None, letter=None, path=None):
        if not letter:
            try:
                last_letter = self.alternatives[len(self.alternatives)-1].get('letter')
                letter = chr(ord(last_letter)+1)
            except:
                letter = 'A'
        
        self.alternatives.append({
            'letter': letter,
            'text': text,
            'file_path': path
        })