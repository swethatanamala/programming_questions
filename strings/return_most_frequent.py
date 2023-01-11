paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
punctuation_marks = [".", ",", "?", ";", "!", ":", "'", "-", "@", "/", "*"]
for mark in punctuation_marks:
    paragraph = paragraph.replace(mark, ' ')
paragraph = paragraph.lower()
words = paragraph.split()
hashmap = {}
for word in words:
    if word not in banned:
        if word in hashmap:
            hashmap[word] += 1
        else:
            hashmap[word] = 1
answer = sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)[0]
print(answer)