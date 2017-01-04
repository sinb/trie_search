# -*- coding: utf-8 -*-


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
        self.data = None
        self.key = None


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string, data):
        string = string.decode("utf-8")
        current_node = self.root
        for char in string:
            node = current_node.children.get(char)
            if not node:
                node = TrieNode()
                current_node.children[char] = node
            current_node = node
        current_node.is_end = True
        current_node.data = data
        current_node.key = string

    def whole_search(self, string):
        string = string.decode("utf-8")
        current_node = self.root
        for char in string:
            node = current_node.children.get(char)
            if not node:
                return None
            current_node = node
        if current_node.is_end:
            return current_node.data
        else:
            return None

    def prefix_search(self, string):
        string = string.decode("utf-8")
        current_node = self.root
        for char in string:
            node = current_node.children.get(char)
            if not node:
                return None
            current_node = node
        result = []
        self.forward(node, result)
        return result

    def forward(self, node, result):
        if len(node.children) > 0:
            if node.is_end:
                result.append((node.key, node.data))
            for char in node.children.keys():
                this_node = node.children.get(char)
                if this_node.children:
                    for tmp_node in this_node.children.values():
                        self.forward(tmp_node, result)
                else:
                    result.append((this_node.key, this_node.data))
        else:
            result.append((node.key, node.data))


def build_trie_test_data(filename):
    trie = TrieTree()
    with open(filename, "rb") as f:
        for line in f:
            data = line.split("\t")
            if len(data) == 2:
                trie.insert(data[0].strip(), data[1].strip())
    return trie

if __name__ == "__main__":
    trie = build_trie_test_data("data.tsv")
    ## whole word search
    print(trie.whole_search("禾盛新材:第四届董事会第十一次会议决议公告"))
    ## prefix search
    results = trie.prefix_search("金一文化")
    if results:
        for result in results:
            print(result[0]),
            print(result[1])
