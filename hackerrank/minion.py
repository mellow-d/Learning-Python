def minion_game(string):
    string = string.upper()
    word = string
    #counting no of repetitiion of substring
    def repetition(sub_str, string):
        n = len(sub_str)
        count = 0
        for i, j in enumerate(string):
            if string[i:n + i] == sub_str:
                count += 1
        return count


    #seperating vowel starting and consonant starting words
    def seperation(lst):
        str_vowel = []
        str_consonant = []
        for i in lst:
            if i[0] == 'A' or i[0] == 'E' or i[0] == 'I' or i[0] == 'O' or i[0] == 'U':
                str_vowel.append(i)
            else:
                str_consonant.append(i)
        return str_consonant, str_vowel
    #
    def lst_word(word):
        lst = []
        for i in range(1, len(word) + 1):
            # trying to fetch words
            for j in range(len(word)):
                lst.append(word[j:i + j])
        lst = list(set(lst))
        return lst
    lst=lst_word(word)
    man1, man2 = seperation(lst)

    def score(man1, man2):
        score1 = 0
        score2 = 0
        for i in man1:
            score1 += repetition(i, word)
        for j in man2:
            score2 += repetition(j, word)
        return score1, score2

    man1_score, man2_score = score(man1, man2)

    if man1_score > man2_score:
        print('Stuart', man1_score)
    elif man1_score < man2_score:
        print('Kevin', man2_score)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input("enter a string: ")
    minion_game(s)