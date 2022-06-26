import random as r
from random import sample as s

def commendation():
    commendation = ['正しい！', 'はい、正解です！', '凄い！', '頭が良い！']
    commendation = s(commendation, 1)
    for i in commendation:
        print(i)

while True:
    words = [['endure', '耐える', 'たえる'],
            ['prevent', '防ぐ', 'ふせぐ'],
            ['admit', '認める', 'みとめる'],
            ['avoid', '避ける', 'さける'],
            ['sad', '悲しい', 'かなしい'],
            ['advise', '勧める', 'すすめる'],
            ['quit', '辞める', 'やめる'],
            ['reget', '後悔する', 'こうかいする']]
    while words:
        r.shuffle(words)
        word = words.pop(0)
        key = word[1]
        value = word[2]
        print('What is', key, '?')
        x = input()
        if x == value:
            commendation()
            print('Now use', key, 'in a sentence')
            x = input()
            commendation()
        else:
            print('Wrong', '(', value, ')')