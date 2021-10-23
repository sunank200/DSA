"""
Write algorithm for java grep command for word matching in the following
context. Given a file containing n words. Given a word w and a number k.
Find k words in the file occurring before occurrence of w.Assume that the
average word size is m in the file

eg.
aaa
bbb
ccc
booking
alpha
beta
gamma

for k=3 and w = booking
the output should be [aaa,bbb,ccc,booking]
similarly for k =2 and w = beta
output should be [booking,alpha,beta]
Assume that the file size can grow very large
and try to get solution with space complexity lesser than O(n)

I suggessted solution for iterating through file until the word w is found and
maintaiining a queue of size K
The time complexity of my solution was O(nm)
and space complexity was O(k) .Any answers to improve the time and space
complexity
Apparently they were looking for a better implementation of grep


"""


def grep_implementation(words, word_of_interest, k):
    """
    #     1. Create a queue of size k+1.
    #     2. Add the word to queue if size of queue is less than k+1 and word is not
    #     word_of_interest.
    TC: O(mn)
    SC: O(k)
    :param words:
    :param word_of_interest:
    :param k:
    :return:
    """
    word_queue = []
    result = []
    for word in words:
        if word == word_of_interest:
            while len(word_queue) > 0:
                result.append(word_queue[0])
                word_queue.pop(0)
            result.append(word)
            break
        elif len(word_queue) < k:
            word_queue.append(word)
        else:
            word_queue.pop(0)
            word_queue.append(word)

    return result


if __name__ == "__main__":
    word_list = ["aaa", "bbb", "ccc", "booking", "alpha", "beta", "gamma"]
    print(grep_implementation(word_list, "beta", 2))
