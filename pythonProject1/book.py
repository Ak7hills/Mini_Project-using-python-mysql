class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def view(self):
        print("book title",self.title,"book author",self.author,"book price",self.price)

a=book("merchant of venice","shakespeare",3000)
a.view()