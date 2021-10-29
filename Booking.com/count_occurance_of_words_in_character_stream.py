"""
Given a stream of characters and a list of words find and display count of each
 and every word once the stream ends.
 
Input: stream = "acacabcatghhellomvnsdb", words = ["aca","cat","hello","world"]
Output : ["aca" : 2 , "cat" : 1 , "hello" : 1 , "world" : 0].

"""

"""
1. create a trie of words, find largest word len -> k
2. for each ch in stream at i, check if stream(i:k) is in trie, if yes increase
 the count 
TC: O(nk)

Better approach is to use acho corasic algorithm,  with time complexity
 O(n+m+k), where
  n is stream length, 
  m - total length of dictionary world,
  k - number of appearance of dict keys in text.
"""
