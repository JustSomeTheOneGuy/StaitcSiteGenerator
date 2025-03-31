from textnode import TextNode, TextType

def main():

    a = TextNode("hello, how are you?", TextType.BOLD_TEXT)
    b = TextNode("I ate my shoes!", TextType.ITALIC_TEXT)
    c = TextNode("I hate this website!", TextType.LINK, "https://boot.dev")
    print(a)
    print(b)
    print(c)


main()