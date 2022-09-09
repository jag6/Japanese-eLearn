def commendation
    commendations = Array['正しい！', 'はい、正解です！', '凄い！', '頭が良い！']
    commendation = commendations.sample
    puts commendation
end

while true
    words = Array[['endure', '耐える', 'たえる'],
            ['prevent', '防ぐ', 'ふせぐ'],
            ['admit', '認める', 'みとめる'],
            ['avoid', '避ける', 'さける'],
            ['sad', '悲しい', 'かなしい'],
            ['advise', '勧める', 'すすめる'],
            ['quit', '辞める', 'やめる'],
            ['reget', '後悔する', 'こうかいする']]
    while words
        words.shuffle
        word = words.pop
        key = word[1]
        value = word[2]
        puts 'What is ' + key + ' ?'
        x = gets.chomp
        if x == value
            commendation
            puts 'Now use ' + key + ' in a sentence'
            x = gets.chomp
            commendation
        else
            puts 'Wrong ' + value
        end
    end
end