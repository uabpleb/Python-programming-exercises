
class Foo:
    def __init__(self) -> None:
        self.word = ""

    def getString(self) -> str:
        self.word = input("Enter a word: ")

    def printString(self) -> None:
        print(self.word)

def testFoo():
    foo = Foo()
    
    foo.getString()
    foo.printString()

testFoo()