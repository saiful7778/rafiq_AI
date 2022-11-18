from essential_function import tokenize, find_common, list_to_str, last_word
from word2number import w2n
from features_function.search_and_scrape import open_links
try:
    import pywhatkit
except:
    pass

def search_on_google(query):
    try:
        search_google = int(len(query)-query[::-1].index("google"))
        lenth = int(len(query))
        list = query[search_google:lenth]
        if len(list) == 0:
            query = list_to_str(query)
            query = query.replace(" on google", "").replace(" search in google", "").replace(" search on google", "").replace(" in google", "").replace(" search", "")
            pywhatkit.search(query)
        else:
            try:
                common = ['first','fast','last']
                first = ['first','fast']
                find_common = [element for element in list if element in common]
                find_common = str(''.join(find_common))
                query = query[0:search_google]
                query = list_to_str(query)
                query = query.replace(" search in", "").replace(" search on", "")
                if find_common in first:
                    find_first = list.index(find_common)
                    web_num = find_first + 1
                    web_num = list[web_num]
                    if isinstance(web_num, int):
                        open_links(query, web_num)
                    else:
                        numder = w2n.word_to_num(web_num)
                        open_links(query, numder)
                else:
                    last = list.index(find_common)
                    web_num = last + 1
                    web_num = list[web_num]
                    if isinstance(web_num, int):
                        open_links(query, web_num)
                    else:
                        numder = w2n.word_to_num(web_num)
                        open_links(query, numder)
            except:
                pass
    except:
        pass