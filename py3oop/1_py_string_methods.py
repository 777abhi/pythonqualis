zenPython = ''' 
The Zen of Python, by Tim Peters 

Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated. 
Flat is better than nested.
Sparse is better than dense. 
Readability counts. 
Special cases aren't special enough to break the rules. 
Although practicality beats purity. 
Errors should never pass silently. 
Unless explicitly silenced. 
In the face of ambiguity, refuse the temptation to guess. 
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea.
'''
words = zenPython.split(" ")

print("original string -->")
print(words)
print(len(words))

for i in range(len(words)):
    words[i] = words[i].strip(',').strip('.').strip('-').strip('*').strip('!').strip().strip(' .')


print("original string after strip-->")
print(words)

print(words[4])

for i in range(len(words)):
    words[i] = words[i].lower()

print("original string after strip and lower case-->")
print(words)

print(words[4])

unique_words = set(words)

for word in unique_words:
    print(word)

print(len(unique_words))

word_frequency = words.count('the')
print(word_frequency)

frequent_words = []

for word in words:
    word_frequency = words.count(word)
    if(word_frequency>5):
        frequent_words.append(word)
frequent_words = set(frequent_words)
print(len(frequent_words))