from html.parser import HTMLParser

# HTML parser for scraping image link from GitHub repository
class ParseOSCrepo(HTMLParser):
    token: str = None

    def handle_starttag(self, tag: str, attrs: str):
        if self.token:
            return
        if tag != "meta":
            return
        token = None
        for (index, (i, j)) in enumerate(attrs):
            if i == "content":
                token = j
            if all([i == "property", j == "og:image"]):
                if token:
                    self.token = token
                    return
                for (inner_index, (ni, nj)) in enumerate(attrs, start=index):
                    if ni == "content":
                        self.token = nj
                        return
