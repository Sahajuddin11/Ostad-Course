num_to_word  = {1: 'one', 2: 'two', 3: 'three', 4:'four'}
num_to_word[5]='five'

print(num_to_word)
print(num_to_word.keys())
print(num_to_word.values())
print(num_to_word.get(3))

for key,value in num_to_word.items():
    print(key,value)
    
num_to_word.clear()

for key,value in num_to_word.items():
    print(key,value)
