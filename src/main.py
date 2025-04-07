from textnode import TextNode, TextType

def main():
    tn = TextNode("Example link text", TextType.LINK, "https://example.com")
    print(repr(tn))

main()