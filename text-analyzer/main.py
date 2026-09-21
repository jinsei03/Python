text = input("Enter your sentece with no punctuation: ")
words = (text.lower()).split()
amount = len(words)
unique = []
unique_count = 0
common = {}
most_common = None
common_count = 0
longest = words[0]

for word in words:
    if word not in unique:
        unique.append(word)
        unique_count += 1
    if word in common:
        common[word] += 1
    else:
        common[word] = 1

for word, count in common.items():
    if count > common_count:
        most_common = word
        common_count = count 

for word in words:
    if len(word) > len(longest):
        longest = word
        
print("Words: ", amount)
print("Unique words: ", unique_count)
print("Most common word: ", most_common)
print("Longest word: ", longest)
