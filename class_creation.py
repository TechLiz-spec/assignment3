class Book:
    def __init__(self , name , pages ,author , year_of_release):
        self.name=name
        self.pages=pages
        self.author=author
        self.year_of_release=year_of_release
    def describe(self):
            print(f"{self.name} {self.pages} pages written by {self.author} in the year {self.year_of_release}")
    def        about(self):
            print(f"{self.name}  is about school  work")


book1=Book("The Samaritan", "116" ,"James Kalahari", "2021")  
book2=Book("Mapambazuko ya macheo", "289","Simba Harati", "2020")

book1.describe()
book1.about()