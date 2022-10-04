const { shuffle, showCommendation } = require('./commendation');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
}); 

let words = [['endure', '耐える', 'たえる'],
            ['prevent', '防ぐ', 'ふせぐ'],
            ['admit', '認める', 'みとめる'],
            ['avoid', '避ける', 'さける'],
            ['sad', '悲しい', 'かなしい'],
            ['advise', '勧める', 'すすめる'],
            ['quit', '辞める', 'やめる'],
            ['regret', '後悔する', 'こうかいする']];

const practice = () => {
    try {
        words = shuffle(words);
        let words2 = [];
        let word = words.pop();
        words2.push(word);
        let key = word[1];
        let value = word[2];
        rl.question(`What is ${key} ? `, (input) => {
            if(input == 'exit') {
                return rl.close();
            } 
            else if(input == value) {
                showCommendation();
                rl.question(`Now use ${key} in a sentence `, () => {
                    showCommendation();
                    practice();
                })
            }else {
                console.log(`Wrong ${value}`);
                for (let word of words2) {
                    words.push(word);
                }
                practice();
            }
        });
    }catch {
        console.log('All Done, Bye Bye!');
        return rl.close();
    }
};

practice();