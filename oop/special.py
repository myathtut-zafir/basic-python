class Sample():
    def __init__(self,title):
        self.title=title
    def __str__(self):
        return f"{self.title} is here"

sam=Sample("testing")
# del sam //delete the varible from mermory
print(sam)