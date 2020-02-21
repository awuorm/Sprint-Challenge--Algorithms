'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    word_list = list(word)
    if len(word_list) <= 1:
        return count
    else:
        if word_list[len(word_list)-1] == "h" and word_list[len(word_list)-2] == "t":
            count += 1
        return count_th("".join(word_list[:-1]), count)


# ===> Needs refactoring
#     if 'th' not in word:
#         print(count)
#         return count
#     else:
#         if 'th' in word:
#             count += 1
#             word = word.replace("th","")
#         print(word,count)
#         return count_th(word, count)
# # count_th("thhtthht")
# count_th("abcthefthghith")