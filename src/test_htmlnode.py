import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        test_dict = {"test": "testagain", "test2": "testagain2"}
        node = HTMLNode("tag", "value", "children", test_dict)
        node2 = HTMLNode()
        node3 = HTMLNode("tag")
        leafnode = LeafNode("tag", "value", test_dict)
        leafnode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        parentnode = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        parentnode2 = ParentNode(
        "d",
        [
            leafnode2
        ],
        )

        parentnode3 = ParentNode("b", None)
        parentnode4 = ParentNode(
            "c",
            [
                parentnode,
                parentnode2,
            ],
        )
    
        parentnode5 = ParentNode(
            "a",
            [
                parentnode,
                leafnode2,
                parentnode2
            ],
            {"class": "container", "id": "main"}
                                 
                                 
        )

        #parentnode.to_html()
        #parentnode2.to_html()
        #parentnode3.to_html()
        #parentnode4.to_html()
        #parentnode5.to_html()
        #print(parentnode.to_html())
        #print(parentnode2.to_html())
       # node.props_to_html()
       # node2.props_to_html()
       # node3.props_to_html()
       # leafnode.to_html()
       # print(node.props_to_html())
        #print(node2)
       # print(node3)

        #print(leafnode.to_html())
        #print(leafnode2.to_html())