def commendation
    commendations = Array['正しい！', 'はい、正解です！', '凄い！', '頭が良い！']
  	commendation = commendations.sample
  	puts commendation
end

while true
    words = Array[['endure', '耐える', 'たえる'],
            ['be_apart', '離れる', 'はなれる'],
            ['smile', '笑う', 'わらう'],
            ['maintain', '保つ', 'たもつ'],
            ['praise', '褒める', 'ほめる']]
  	words = words.sample
    key = words[1]
    value = words[2]
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