import random as r
from random import sample as s
from commendation import commendation

def practice():
    while True:
        words = [['endure', '耐える', 'たえる'],
                ['be_apart', '離れる', 'はなれる'],
                ['smile', '笑う', 'わらう'],
                ['maintain', '保つ', 'たもつ'],
                ['praise', '褒める', 'ほめる']]
        words = s(words, 1)
        key = words[0][1]
        value = words[0][2]
        print('What is', key, '?')
        x = input()
        if x == 'exit':
            print('All done, Bye Bye!')
            return
        elif x == value:
            commendation()
            print('Now use', key, 'in a sentence')
            x = input()
            commendation()
        else:
            print('Wrong', '(', value, ')')

practice()