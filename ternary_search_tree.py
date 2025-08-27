class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.is_end = False

    def __repr__(self):
        return f"TSTNode('{self.char}')"


class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if not word:
            return
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, index):
        char = word[index]
        if not node:
            node = TSTNode(char)
        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.middle = self._insert(node.middle, word, index + 1)
            else:
                node.is_end = True
        return node

    def search(self, word):
        if not word:
            return False
        return self._search(self.root, word, 0)

    def _search(self, node, word, index):
        if not node:
            return False
        char = word[index]
        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index == len(word) - 1:
                return node.is_end
            return self._search(node.middle, word, index + 1)

    def traverse(self):
        words = []
        self._traverse(self.root, '', words)
        return words

    def _traverse(self, node, prefix, result):
        if not node:
            return
        self._traverse(node.left, prefix, result)
        if node.is_end:
            result.append(prefix + node.char)
        self._traverse(node.middle, prefix + node.char, result)
        self._traverse(node.right, prefix, result)


if __name__ == '__main__':
    tst = TernarySearchTree()
    words = ["cat", "cap", "can", "bat", "bag", "bad"]
    for word in words:
        tst.insert(word)

    test_cases = {
        "cat": True,
        "cap": True,
        "cab": False,
        "": False,
        "bat": True,
        "bag": True,
        "dog": False
    }

    for word, expected in test_cases.items():
        result = tst.search(word)
        assert result == expected, f"Test failed for '{word}': expected {expected}, got {result}"

    print("✅ All basic tests passed.")


def load_words_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return []
if __name__ == '__main__':
    tst = TernarySearchTree()

    
    filepath = r"/Users/amudhans/Desktop/Concepts_of Datascience_secondchance/data/search_trees/insert_words.txt"

    
    words_from_file = load_words_from_file(filepath)
    for word in words_from_file:
        tst.insert(word)

    print(f"✅ Inserted {len(words_from_file)} words into the TST.")

   
    print("🌳 Words in TST (via traverse):")
    print(tst.traverse())

    
    test_words = ["cat", "banana", "tree", "dog"]
    for word in test_words:
        found = tst.search(word)
        print(f"🔍 Search '{word}': {'Found ✅' if found else 'Not found ❌'}")


class TernarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def search(self, word):  
        if not word:
            return False
        return self._search(self.root, word, 0)

    def _search(self, node, word, index):
        if not node:
            return False
        char = word[index]
        if char < node.char:
            return self._search(node.left, word, index)
        elif char > node.char:
            return self._search(node.right, word, index)
        else:
            if index == len(word) - 1:
                return node.is_end
            return self._search(node.middle, word, index + 1)

    def insert(self, word):
        if not word:
            return
        if not self.search(word):  
            self.root = self._insert(self.root, word, 0)
            self._size += 1

    def _insert(self, node, word, index):
        char = word[index]
        if not node:
            node = TSTNode(char)
        if char < node.char:
            node.left = self._insert(node.left, word, index)
        elif char > node.char:
            node.right = self._insert(node.right, word, index)
        else:
            if index + 1 < len(word):
                node.middle = self._insert(node.middle, word, index + 1)
            else:
                node.is_end = True
        return node

    def __len__(self):
        return self._size


