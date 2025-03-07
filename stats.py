def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_chars(chars):
    sorted_chars = []

    for char, count in chars.items():
        sorted_chars.append({"char": char, "count": count})
    sorted_chars.sort(reverse=True, key=sort_on)
    print(sorted_chars)
    return sorted_chars

def sort_on(dict):
    return dict["count"]
    