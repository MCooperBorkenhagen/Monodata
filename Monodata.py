



def is_vowel(char):

    return char in 'aeiouy'

 

 

def index_first_vowel(word):

    v = [(i,x) for i,x in enumerate(word) if is_vowel(x)]

    if len(v) > 1 and v[0][1] == 'y' and v[0][0] == 0:

        return v[1][0]

    else:

        return v[0][0]

 

 

with open("data/kidwords.txt", 'r') as f:

    words_orig = [w.strip() for w in f.readlines()]

 

 

ix = [index_first_vowel(w) for w in words_orig]

words = [

    w[0:i+1] + '_' + w[i+1:]

    if i+1 < len(w) and not is_vowel(w[i+1])

    else w

    for w,i in zip(words_orig, ix)

]

          

max_vowel_index = max(ix)

word_length = [len(w) for w in words]

max_length = max(len(w) for w in words)

 

tmp = [(w,v,l) for w,v,l in zip(words,ix,word_length) if l == max_length]

 

m = max_length + (max_vowel_index - min(x[1] for x in tmp))

 

padded = [

    '_'*(max_vowel_index - i) + w + '_'*(m-len(w)-(max_vowel_index - i))

    for i,w

    in zip(ix, words)

]

 

with open("data/kidwords_padded.txt", 'w') as f:

    for p in padded:

        f.write(p + '\n')
