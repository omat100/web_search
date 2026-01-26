from ddgs import DDGS

class Web:
    def __init__(self):
        pass

    def search_from_arrays(self, sentence, max_results=7):
        """
        Takes arrays of nouns and adjectives
        Searches DuckDuckGo
        Returns structured results
        """

        results = {}

        with DDGS() as ddgs:
            search_results = []
            for r in ddgs.text(sentence,max_results=max_results):
                search_results.append([
                    r["title"],
                    r["href"],
                    r["body"],
                ])
                results[sentence] = search_results
            '''''
            for noun in nouns:
                for adj in adjectives:
                    query = f"{adj} {noun}"
                    search_results = []

                    for r in ddgs.text(query, max_results=max_results):
                        search_results.append({
                            "title": r["title"],
                            "url": r["href"],
                            "snippet": r["body"]
                        })

                    results[query] = search_results
                    '''
        return results
