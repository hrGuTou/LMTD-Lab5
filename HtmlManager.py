
from HtmlDocument import HtmlDocument


class HtmlManager:
    def __init__(self, title):
        self.title = title
        self.template = ""
        self.init()

    def init(self):
        self.html = HtmlDocument(self.title)
        self.template = self.html.getTemplate()

    def addTag(self, tag, word):
        self.template = self.template %"<%s>%s</%s>\n%s" %(tag, word, tag, "%s")

    def saveHTML(self):
        tmp = self.template %("")

        tmp = tmp.split("\n")
        tmp = [line for line in tmp if line.strip() != ""]

        res = ""
        for line in tmp:
            res += line + "\n"

        filename = self.title + ".html"
        try:
            with open(filename, 'w') as f:
                f.write(res)
        except Exception as e:
            print(e)
        else:
            f.close()
            print("File saved")

# DEBUG CODE
"""
if __name__ == "__main__":
    app = HtmlManager("i")
    app.addTag("a","d")
    app.addTag("b","a")
    app.saveHTML()
"""