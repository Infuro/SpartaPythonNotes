
def is_isogram(word):
    word = word.replace(" ", "")
    word = word.replace("-", "")

    list = []
    [list.append(i) for i in word if i not in list]

    if len(word) == len(list):
        print('is isogram')
    else:
        print('not isogram')

word = "isogram"
is_isogram(word)

def is_isogram(word):
    word = word.replace(" ", "")
    word = word.replace("-", "")

    list = []
    [list.append(i) for i in word if i not in list]

    if len(word) == len(list):
        print('is isogram')
    else:
        print('not isogram')

for i in word:
    if i not in list:
        list.append(i)