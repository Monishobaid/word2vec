import numpy as np 


sentences = [
    "the cat drinks milk",
    "the dog drinks water",
    "the cat eats fish",
    "the dog eats meat"
]

sentences_token = []
hashmap = {}
word_to_id_mapping = {}

for i in sentences:

    words_in_setences = i.split()
    sentences_token.append(words_in_setences)

print(sentences_token)

for i in range(len(sentences_token)):
    for j in range(len(sentences_token[i])):
        if sentences_token[i][j] in hashmap:
            hashmap[sentences_token[i][j]] += 1
        else:
            hashmap[sentences_token[i][j]] = 1

print(hashmap)


vocal = len(hashmap.keys())
counter = 0

for i in sentences_token:
    for j in i:
        if j in word_to_id_mapping:
            pass
        else:
            word_to_id_mapping[j] = counter
            counter += 1
    
print(word_to_id_mapping)
print(vocal)

encoded_sentences = []

for i in sentences_token:
    current_sentences = []
    for j in i:
        current_sentences.append(word_to_id_mapping[j])
    encoded_sentences.append(current_sentences)

print(encoded_sentences)

# embedding matrix 
embedding_dim = 5

rng = np.random.default_rng(42)

embedding_matrix = rng.uniform(
    -0.5,
    0.5,
    size = (vocal, embedding_dim)
)

print("embedding matrix", embedding_matrix)

sentence = sentences_token[0]
center_index = 1

center_word = sentence[center_index]

print("center word",center_word)

window_size = 2

start = max(0, center_index-window_size)
end = min()


