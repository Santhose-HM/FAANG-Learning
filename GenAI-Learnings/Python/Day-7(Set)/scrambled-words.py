scrambled_words ={"plea","medical","listen","leap","decimal","silent"}
result  = set()
for word in scrambled_words:
    for word2 in scrambled_words:
        if word!= word2 and sorted(word) == sorted(word2):
            pair = tuple(sorted((word,word2)))
            result.add(pair)
for pair in result:
    print(pair)