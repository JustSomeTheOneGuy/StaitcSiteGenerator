import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from textnode import TextType, TextNode


class TestSplitNodes(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        node2 = TextNode("Two `code` block words `this` time", TextType.TEXT)
        result2 = split_nodes_delimiter([node2], "`", TextType.CODE)

        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            result,
        )

        self.assertIsInstance(result, list)
        print(result)
        print(result2)

    def test_bold_split(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        node2 = TextNode("Two **bold** words **this** time", TextType.TEXT)
        result2 = split_nodes_delimiter([node2], "**", TextType.BOLD)

        self.assertIsInstance(result, list)
        self.assertIsInstance(result2, list)
        print(result)
        print(result2)

    def test_italic_split(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        node2 = TextNode("Two _italic_ words _this_ time", TextType.TEXT)
        result2 = split_nodes_delimiter([node2], "_", TextType.ITALIC)

        self.assertIsInstance(result, list)
        self.assertIsInstance(result2, list)
        print(result)
        print(result2)

    def test_multiple_node_split(self):
        node = TextNode("This is text **with** a **italic** word", TextType.TEXT)
        node2 = TextNode("This is text with a **bold** word", TextType.TEXT)
        node3 = TextNode("This is text with a **code block** word", TextType.TEXT)
        result = split_nodes_delimiter([node, node2, node3], "**", TextType.BOLD)

        self.assertIsInstance(result, list)
        print(result)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        matches2 = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches2)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )

        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_nodes_image(self):
        node = TextNode(
        "This is text with one image ![image](https://linktoimage.png) isn't that cool?",
        TextType.TEXT,
        )
        result = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with one image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://linktoimage.png"),
                TextNode(" isn't that cool?", TextType.TEXT),

            ],
            result,
        )
    def test_split_nodes_multiple_images(self):
        node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
        )
        
        result = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            result,
        )

    def test_split_nodes_no_image(self):
        node = TextNode(
        "There is no image in this text!",
        TextType.TEXT,
        )
        result = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("There is no image in this text!", TextType.TEXT),
                
            ],
            result,
        )

    def test_split_nodes_multi_node(self):
        node = TextNode(
            "More than two ![monkey](https://linktomonkey.png) images ![banana](https://linktobanana.jpg)![images back to back!](https://bamdidntexpectthat.rar)",
            TextType.TEXT,
        )
        node2 = TextNode(
            "This is text with one image ![image](https://linktoimage.png) isn't that cool?",
        TextType.TEXT,
        )
        result = split_nodes_image([node, node2])

        self.assertListEqual(
            [
                TextNode("More than two ", TextType.TEXT),
                TextNode("monkey", TextType.IMAGE, "https://linktomonkey.png"),
                TextNode(" images ", TextType.TEXT),
                TextNode("banana", TextType.IMAGE, "https://linktobanana.jpg"),
                TextNode("images back to back!", TextType.IMAGE, "https://bamdidntexpectthat.rar"),
                TextNode("This is text with one image ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://linktoimage.png"),
                TextNode(" isn't that cool?", TextType.TEXT),
            ],
            result,
        )

    def test_split_node_link(self):
        node = TextNode(
            "This is text with one link [link city](https://linktolinkcity.com) isn't that rad?",
            TextType.TEXT,
        )
        result = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text with one link ", TextType.TEXT),
                TextNode("link city", TextType.LINK, "https://linktolinkcity.com"), 
                TextNode(" isn't that rad?", TextType.TEXT),
            ],
            result,
        )
        
    def test_split_node_multi_link(self):
        node = TextNode(
            "This is text with more than one link [link village](https://linktolinkvillage.edu) don't forget [link town](https://linktolinktown.com)",
            TextType.TEXT,
        )
        result = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text with more than one link ", TextType.TEXT),
                TextNode("link village", TextType.LINK, "https://linktolinkvillage.edu"),
                TextNode(" don't forget ", TextType.TEXT),
                TextNode("link town", TextType.LINK, "https://linktolinktown.com"),
            ],
            result,
        )

    def test_split_node_no_link(self):
        node = TextNode(
            "There is no link here!",
            TextType.TEXT
        )
        node2 = TextNode(
            "Wait, isn't this an ![image](https://omganimage!.png)",
            TextType.IMAGE
        )
        result = split_nodes_link([node, node2])

        self.assertListEqual(
            [
                TextNode("There is no link here!", TextType.TEXT),
                TextNode("Wait, isn't this an ![image](https://omganimage!.png)", TextType.IMAGE),
            ],
            result,
        )

if __name__ == "__main__":
    unittest.main()
