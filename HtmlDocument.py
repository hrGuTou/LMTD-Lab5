
class HtmlDocument:
    def __init__(self, title):
        self.template = """
<html>
<head>
<title>{0}</title>
</head>
<body>
%s
</body>
</html>
""".format(title)

    def getTemplate(self):
        return self.template
