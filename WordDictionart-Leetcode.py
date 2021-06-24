# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = dict()
#         self.finish = False
        

#     def addWord(self, word: str) -> None:
#         node = self
#         for char in word:
#             if char not in node.root:
#                 node.root[char] = WordDictionary()
#             node = node.root[char]
        
#         node.finish = True

#     def search(self, word: str) -> bool:
#         node = self
#         for idx, letter in enumerate(word):
#             if letter == ".":
#                 queue = list(node.root.keys())
#                 print(queue)
#                 while queue:
#                     top = queue.pop()
#                     return node.root[top].search(word[idx+1:])
            
#             if letter not in node.root or node.finish:
#                 return False
            
#             node = node.root[letter]
                    
#         return True
                    
                
# trie = WordDictionary()
# for word in [["ran"],["rune"],["runner"],["runs"],["add"],["adds"],["adder"],["addee"]]:
#     trie.addWord(word[0])

# test = [["r.n"],["ru.n.e"],["add"],["add."],["adde."],[".an."],["...s"],["....e."],["......."],["..n.r"]]
# for t in test:
#     print("Testing: "+t[0]+" ****************")
#     print(trie.search(t[0]))
