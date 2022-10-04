const { shuffle } = require('./commendation');
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let words = [['endure', '耐える', 'たえる'],
            ['be_apart', '離れる', 'はなれる'],
            ['smile', '笑う', 'わらう'],
            ['maintain', '保つ', 'たもつ'],
            ['praise', '褒める', 'ほめる']];

const practice = () => {
    words = shuffle(words);
    let key = words[0][1];
    let value = words[0][2];
    rl.question(`What is ${key} ? `, (input) => {
        if(input == 'exit') {
            return rl.close();
        } 
        else if(input == value) {
            shuffle(commendation);
            console.log(commendation[0]);
            practice();
        }else {
            console.log(`Wrong ${value}`);
            practice();
        }
    });
};

practice();