from random import sample as s

def commendation():
    commendation = ['正しい！', 'はい、正解です！', '凄い！', '頭が良い！']
    commendation = s(commendation, 1)
    for i in commendation:
        print(i)