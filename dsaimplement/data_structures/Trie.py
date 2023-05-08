from typing import Dict

class TrieNode:
    def __init__(self, char) -> None:
        self.char = char
        self.children: Dict[str, TrieNode] = {}
        self.is_end = False
        # to track multiple occurences of same word
        self.counter = 0
        
class Trie:
    def __init__(self) -> None:
        # insert root node
        self.root = TrieNode("*")
    
    def insert(self, word: str) -> None:
        """
        Iterative approach to insert word into true

        Args:
            word (str): word to be added
        """ 
        node = self.root    
        for char in word:
            # if char present
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        # indicate end of word
        node.is_end = True

        # another occurence of word
        node.counter += 1
    
    def search(self, word: str, word_or_prefix: str = "word") -> None:
        """
        Searches for word/prefix in trie

        Args:
            word (str): word to be searched
            word_or_prefix (str): prefix to be searched
        """
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.is_end if word_or_prefix == "word" else True