from typing import Dict, Generator, List
import re


def get_words(article) -> List[str]:
    title = article["title"]
    description = article["description"]
    return title.split(" ") + description.split(" ")


def filter_words(words: List[str]):
    for word in words:
        result = re.sub(r"[^a-zA-Z]", "", word)
        if len(result) > 2:
            yield result


def get_article_count(article) -> Dict[str, int]:
    result = {}
    for word in filter_words(get_words(article)):
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def merge_word_counts(fst: Dict[str, int], snd: Dict[str, int]) -> Dict[str, int]:
    lesser, bigger = (fst, snd) if len(fst.keys()) < len(snd.keys()) else (snd, fst)
    for word, count in lesser.items():
        if word in bigger:
            bigger[word] = bigger[word] + count
        else:
            bigger[word] = count
    return bigger


def sort_count_descending(original: Dict[str, int]) -> Dict[str, int]:
    return {
        k: v
        for k, v in sorted(original.items(), key=lambda item: item[1], reverse=True)
    }


def proccess_articles(response) -> Dict[str, int]:
    if "articles" not in response:
        return {}
    result = {}
    for article in response["articles"]:
        result = merge_word_counts(result, get_article_count(article))
    return sort_count_descending(result)
