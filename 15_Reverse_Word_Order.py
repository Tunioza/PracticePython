# 15_Reverse_Word_Order
def reversing_words(a):
    a = a.strip().split(" ")
    a = a[::-1]
    for word in a:
        print(word, end=' ')


sentence = input("Daj jakąś wiązanke:\n")
reversing_words(sentence)

