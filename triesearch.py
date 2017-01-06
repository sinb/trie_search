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
        self.node_map = {}

    def insert(self, string, data):
        string = string.decode("utf-8")
        current_node = self.root
        for char in string:
            node = current_node.children.get(char)
            if not node:
                node = TrieNode()
                current_node.children[char] = node
                if not self.node_map.get(char):
                    self.node_map[char] = set()
                    self.node_map[char].add(current_node)
                else:
                    self.node_map[char].add(current_node)
            current_node = node
        current_node.is_end = True
        current_node.data = data
        current_node.key = string

    def whole_search(self, string):
        string = string.decode("utf-8")
        current_node = self.root
        result = []
        for char in string:
            node = current_node.children.get(char)
            if not node:
                return []
            current_node = node
        if current_node.is_end:
            result.append((string, current_node.data))
            return result
        else:
            return []

    def prefix_search(self, string):
        string = string.decode("utf-8")
        current_node = self.root
        for char in string:
            node = current_node.children.get(char)
            if not node:
                return []
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

    def prefix_search_from_node(self, string, current_node):
        for char in string:
            node = current_node.children.get(char)
            if not node:
                return []
            current_node = node
        result = []
        self.forward(node, result)
        return result

    def keyword_search(self, string):
        string = string.decode("utf-8")
        char = string[0]
        nodes = self.node_map.get(char)
        result = []
        if nodes:
            for node in nodes:
                result += self.prefix_search_from_node(string, node)
        return result


def build_trie_test_data(filename):
    trie = TrieTree()
    with open(filename, "rb") as f:
        for line in f:
            data = line.split("\t")
            if len(data) == 2:
                trie.insert(data[0].strip(), data[1].strip())
    return trie


def print_result(data):
    for item in data:
        print(item[0]),
        print(item[1])

if __name__ == "__main__":
    trie = build_trie_test_data("data.tsv")
    ## whole word search
    results = trie.whole_search("禾盛新材:第四届董事会第十一次会议决议公告")
    print_result(results)

    ## prefix search
    results = trie.prefix_search("金一文化")
    print_result(results)

    ## keyword search
    results = trie.keyword_search("文化")
    print_result(results)
