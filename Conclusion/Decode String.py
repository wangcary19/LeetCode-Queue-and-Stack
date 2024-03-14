num_stack = [3]
letters_stack = []
repeat = 0
num_cache = ""
word_cache = ""
output = ""

# can you do this recursively???

"""
for x in s:
    if x.isnumeric():
        num_cache += x
    elif x.isalpha():
        word_cache += x
    elif x == "[":
        num_stack.append(num_cache)
        num_cache = ""
        if word_cache != "":
            letters_stack.append(word_cache)
            word_cache = ""
        else:
            continue
    else: # x == "]"
        if word_cache != "":
            output += word_cache * int(num_stack.pop(-1))
            word_cache = ""
        else:
            output = (letters_stack.pop(-1) + output) * int(num_stack.pop(-1))
#end-for

return output + word_cache
"""