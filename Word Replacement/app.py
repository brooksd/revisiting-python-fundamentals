def replace_word():
    
    str = 'Hello, Im revisiting Python fundamentals'
    word_to_replace = input('Enter the Word to Replace:')
    word_replacement = input('Enter the Word Replacement:') 
    print(str.replace(word_to_replace, word_replacement))
    
replace_word()