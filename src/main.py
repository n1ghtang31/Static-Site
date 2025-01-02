from textnode import TextNode, TextType

def main():
    text = TextNode("This is my test", TextType.NORMAL, "http://www.google.com")

    print(text)

main()