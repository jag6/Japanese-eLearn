import random as r
from commendation import commendation

def practice():
    while True:
        words = [['endure', '耐える', 'たえる'],
                ['prevent', '防ぐ', 'ふせぐ'],
                ['admit', '認める', 'みとめる'],
                ['avoid', '避ける', 'さける'],
                ['sad', '悲しい', 'かなしい'],
                ['advise', '勧める', 'すすめる'],
                ['quit', '辞める', 'やめる'],
                ['regret', '後悔する', 'こうかいする']]
        while words:
            words2 = []
            r.shuffle(words)
            word = words.pop(0)
            words2.append(word)
            key = word[1]
            value = word[2]
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
                print('Wrong', value)
                for word in words2:
                    words.append(word)

practice()