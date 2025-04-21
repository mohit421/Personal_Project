
class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence 
        self.index = 0
        self.words = self.sentence.split()
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration 
        index = self.index 
        self.index += 1
        return self.words[index]
    

my_sentence = Sentence("This is a test")

for word in my_sentence:
    print(word)

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))

# This should have the follwoing output:
# This
# is
# a 
# test


# Using Generator 

def Sentence1(sentence1):
    for word in sentence1.split():
        yield word 

my_sentence1 = Sentence1("this is a word")
for word in my_sentence1:
    print(word)


print(next(my_sentence1))
print(next(my_sentence1))
print(next(my_sentence1))
print(next(my_sentence1))
print(next(my_sentence1))