def word_count(content):
    return len(content.split())

def char_count(content):
    chars = {}
    for char in content.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars