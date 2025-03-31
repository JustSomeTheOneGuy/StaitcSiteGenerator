import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue

        if old_node.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Markdown Syntax")
        
        node_list = []
        split_node = old_node.text.split(delimiter)

        for index, item in enumerate(split_node):
            if item == "":
                continue
            if index % 2 == 0:
                node_list.append(TextNode(item, TextType.TEXT))
            else:
                node_list.append(TextNode(item, text_type))

        new_list.extend(node_list)

    return new_list

def split_nodes_image(old_nodes):
     new_list = []

     for old_node in old_nodes:
          if old_node.text_type != TextType.TEXT:
               new_list.append(old_node)
               continue
          

        # below won't work for nodes with multiple images included.

        # creates a list of tuples for images found in old_node.text
          extracted_image = extract_markdown_images(old_node.text)

        # asking for an index over a each tuple in extract image
          for i, tuple in enumerate(extracted_image):
               image_alt = 
          image_alt = extracted_image[0][0]
          print(f"image_alt: {image_alt}")
          image_link = extracted_image[1][1]
          print(f"image_link: {image_link}")
          continue
          

def split_nodes_link(old_nodes):
     pass

def extract_markdown_images(text):
        # finds every alt text and url in text then returns a list of tuples ("alt_text", "url")
        matches = list(re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
        return matches

def extract_markdown_links(text):
        
        matches = list(re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
        return matches


    








    