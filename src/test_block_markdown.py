import unittest
from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_block_markdown_3(self):
        text = """
        # This is a heading

        This here is just a body paragraph, just text and what not
        
        - this is an ordered list 
        - look how orderly
        - and cool it is
        """
        result = markdown_to_blocks(text)
        self.assertListEqual(
            [
                "# This is a heading",
                "This here is just a body paragraph, just text and what not"
                "- this is an ordered list\n- look how orderly\n- and cool it is"
            ],
            result
        )

    def test_markdown_to_blocks(self):
        markdown = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
            ],
        )


