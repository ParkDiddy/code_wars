# takes any string and adds a # and removes spaces and capitalizes first word
def generate_hashtag(s):
    if not s or len(s) > 140:
        return False
    s = s.lower().split()
    for count, word in enumerate(s):
        s[count] = word.capitalize()
    return f"#{''.join(s)}"

print(generate_hashtag("    Codewars      is nice "))