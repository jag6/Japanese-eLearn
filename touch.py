import random as r
from random import sample as s

endure = ["耐える", "たえる"]
make_new = ["新しくする", "あたらしくする"]
smile = ["笑う", "わらうあ"]

while True:
    words = [endure, make_new, smile]
    words = s(words, 1)
    key = words[0][0]
    value = words[0][1]
    print('What is', key, '?')
    x = input()
    if x == value:
        print('Correct')
    else:
        print('Wrong')
        
