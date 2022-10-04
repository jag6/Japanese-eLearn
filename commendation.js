const shuffle = (array) => {
    let currentIndex = array.length;

    while(currentIndex != 0){
        let randomIndex = Math.floor(Math.random() * array.length);
        currentIndex -=1;

        let temp = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temp;
    }

    return array;
};

const showCommendation = () => {
    let commendation = ['正しい！', 'はい、正解です！', '凄い！', '頭が良い！']; 
    shuffle(commendation);
    console.log(commendation[0]);
}

exports.shuffle = shuffle;
exports.showCommendation = showCommendation;