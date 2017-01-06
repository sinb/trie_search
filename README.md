build a search engine with trie tree (prefix tree).

support whole word search and prefix search, and keyword search.

## example
```
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

```
