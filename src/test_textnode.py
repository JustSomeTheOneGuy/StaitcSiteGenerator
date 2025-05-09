import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.BOLD, "https://www.fakeurl.com/imfake")
       # self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This says this", TextType.BOLD)
        node2 = TextNode("That says this", TextType.ITALIC)
       # self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_normal_text(self):
        node = TextNode(text="Normal Text", text_type=TextType.TEXT)
        result = text_node_to_html_node(node)

        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, None)
        self.assertEqual(result.value, "Normal Text")
        self.assertEqual(result.props, {})

    def test_bold_text(self):
        node = TextNode(text="Bold Text", text_type=TextType.BOLD)
        result = text_node_to_html_node(node)

        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "b")
        self.assertEqual(result.value, "Bold Text")
        self.assertEqual(result.props, {})

    def test_italic_text(self):
        node = TextNode(text="Italic Text", text_type=TextType.ITALIC)
        result = text_node_to_html_node(node)

        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "i")
        self.assertEqual(result.value, "Italic Text")
        self.assertEqual(result.props, {})

    def test_code_text(self):
        node = TextNode(text="Code Text", text_type=TextType.CODE)
        result = text_node_to_html_node(node)

        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "code")
        self.assertEqual(result.value, "Code Text")
        self.assertEqual(result.props, {})

    def test_link_text(self):
        node = TextNode(text="Link Text", text_type=TextType.LINK, url="https://www.boot.dev")
        result = text_node_to_html_node(node)

        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "a")
        self.assertEqual(result.value, "Link Text")
        self.assertEqual(result.props, {"href": "https://www.boot.dev"})

    def test_image(self):
        node =TextNode(text="Alt Text", text_type=TextType.IMAGE, url="https://en.wikipedia.org/wiki/Bread#/media/File:Korb_mit_Brötchen.JPG")
        result = text_node_to_html_node(node)

        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "img")
        self.assertEqual(result.value, "")
        self.assertEqual(result.props, {"src": "https://en.wikipedia.org/wiki/Bread#/media/File:Korb_mit_Brötchen.JPG", "alt": "Alt Text"})

if __name__ == "__main__":
    unittest.main()