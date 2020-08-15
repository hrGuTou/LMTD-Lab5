
from HtmlManager import HtmlManager



if __name__ == "__main__":
    title = input("Input the title for html file: ")
    app = HtmlManager(title)
    app.addTag("h1","Hello World")
    app.addTag("h3", "This is a demo")
    app.saveHTML()
