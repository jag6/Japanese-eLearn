import random as r
from random import sample as s

def commendation():
    commendation = ['正しい！', 'はい、正解です！', '凄い！', '頭が良い！']
    commendation = s(commendation, 1)
    for i in commendation:
        print(i)

while True:
    words = [[['endure', '耐える', 'たえる']],
            [['be_apart', '離れる', 'はなれる']],
            [['smile', '笑う', 'わらう']],
            [['maintain', '保つ', 'たもつ']],
            [['praise', '褒める', 'ほめる']]]
    while words:
        r.shuffle(words)
        word = words.pop(0)
        key = word[0][1]
        value = word[0][2]
        print('What is', key, '?')
        x = input()
        if x == value:
            commendation()
            print('Now use', key, 'in a sentence')
            x = input()
            commendation()
        else:
            print('Wrong')