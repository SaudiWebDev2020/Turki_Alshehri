
# Book Index
# ------------------------------------------------------------------------
# Write a function that given a sorted array of page numbers, return a string representing a book index. Combine consecutive pages to create ranges. Given [1, 3, 4, 5, 7, 8, 10], return the string "1, 3-5, 7-8, 10".


def book_index(arr):
    newArr = []
    consecitiveStr = []
    string = ""
    for j in range(1, arr[len(arr) - 2], 1):
        for i in range(1, arr[len(arr) - 2], 1):
            if arr[i] == arr[j] and arr[i] + 1 == arr[j] + 1:
                string += str(i) + '-' + j + 1
            # else:
            #     # newArr.append(j)
            #     # string = ""
    print(string)


book_index([1, 3, 4, 5, 7, 8, 10])




# Common Suffix
# ------------------------------------------------------------------------
# When given an array of words, returns the largest suffix (word-end) that is common between all words. For example, for input ["ovation", "notation", "action"], return "tion". Given ["nice", "ice", "sic"], return "".


# def common_suffix(arr):
#     suffix = ""
#     # for i in range(0, len(arr)):
#     #     word = arr[i]
#     #     word2 = arr[i+1]
#     #     for j in range(0, len(word), 1):
#     #         print("inner loop")
#     #         if word[j] == word2[i]:
#     #             print("inner if")
#     #             suffix += word[j]
#     #     if suffix == "":
#     #         break
#     word = arr[0]
#     word2 = arr[1]
#     for j in range(0, len(word), 1):
#             print("word", word[j], 'word2', word2[j])
#             if word[j] == word2[j]:
#                 print("inner if")
#                 suffix += word[j]
#     print(suffix)


# common_suffix(["ovation", "notation", "action"])