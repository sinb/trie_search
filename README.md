build a search engine with trie tree (prefix tree).

support whole word search and prefix search.

## example
```
    trie = build_trie_test_data("data.tsv")
    ## whole word search
    print(trie.whole_search("禾盛新材:第四届董事会第十一次会议决议公告"))
    ## prefix search
    results = trie.prefix_search("汇金")
    if results:
        for result in results:
            print(result[0]),
            print(result[1])
```
