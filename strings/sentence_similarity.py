sentence1 = 
sentence2 = 

def sentence_similarity(sentence1, sentence2, similarpairs):
    if len(sentence1) != len(sentence2):
        return False
    hashmap = {}
    for pair in similarpairs:
        if pair[0] in sentence1:
            hashmap[pair[0]] = pair[1]
        elif pair[1] in sentence1:
            hashmap[pair[1]] = pair[0]
    sentence1 = [hashmap[x] for x in sentence1 if x in hashmap else x]
    return sentence1 == sentence2