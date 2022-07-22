class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.eow = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.eow

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def remove(self, word):
        def dfs(node: TrieNode, word, idx):
            if idx == len(word):
                if not node.children:
                    return True
                node.eow = False
                return False
            char = word[idx]
            if char not in node.children:
                print(word, "not found in trie")
                return False
            should_delete_child = dfs(node.children[char], word, idx+1)
            if should_delete_child:
                del node.children[word[idx]]
            return not node.children
        dfs(self.root, word, 0)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("word")
    trie.insert("work")
    print(trie.search("word"))
    print(trie.search("wor"))
    print(trie.starts_with("wor"))
    trie.insert("wor")
    trie.insert("wordliness")
    print(trie.remove("fart"))
    print(trie.remove("wor"))
    print(trie.remove("wordliness"))
    print(trie.remove("word"))