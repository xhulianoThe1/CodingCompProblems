import re 
from collections import Counter

def count_words(sentence):
    return Counter([word.strip("'") for word in re.split("[^a-zA-Z0-9't]", sentence.lower()) if word])


#Solution 2 
# import re 
# from collections import defaultdict

# def count_words(sentence):
#     dic = defaultdict(int)
#     sentence = re.split("[^a-zA-Z0-9't]", sentence.lower())
#     for word in sentence: 
#         if word: 
#             word = word.strip("'")
#             dic[word] += 1
#     return dic