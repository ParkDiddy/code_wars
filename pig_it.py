import re


def pig_it(text):
    word_pattern = re.compile(r'[a-zA-Z]+')

    def pig_word(word):
        return word[1:] + word[0] + 'ay'

    return word_pattern.sub(lambda match: pig_word(match.group()), text)


print(pig_it("Hello there sir 67!"))
