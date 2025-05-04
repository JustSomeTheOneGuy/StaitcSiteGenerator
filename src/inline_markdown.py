import re
from textnode import TextType, TextNode

def text_to_textnodes(text):
    # first makes a TextNode out of text inputted
    nodes = [TextNode(text, TextType.TEXT)]
    print(f"nodes: {nodes}")
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    print(f"nodes after CODE: {nodes}")
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    print(f"nodes after BOLD: {nodes}")
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    print(f"nodes after ITALIC: {nodes}")
    nodes = split_nodes_image(nodes)
    print(f"nodes after IMAGE: {nodes}")
    nodes = split_nodes_link(nodes)
    print(f"nodes after LINK: {nodes}")
    return nodes

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
    # this is supposed to input a list of nodes, go through each node then split by markdown image 
    new_list = []

    # seperate each node in old_nodes list, if the node is not a text type, append to new list
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue
           
        node_list = [] 
            
        # uses extraction functions to pull out image_alt and image_link
        extracted_images = extract_markdown_images(old_node.text)
        # if no images add node to the new_list
        if not extracted_images:
            new_list.append(old_node)
            continue

        # copy of split node that I can alter without breaking extracted_images
        copy_old_node = old_node
        
        for i in range(len(extracted_images)):
            image_alt = extracted_images[i][0]
            image_link = extracted_images[i][1]

            # split the copy of old_node by firsty image in string for this iteration
            split_node = copy_old_node.text.split(f"![{image_alt}]({image_link})", 1)

            # if the 1st index of split node is not empty, add to node_list
            if split_node[0]:
                node_list.append(TextNode(split_node[0], TextType.TEXT))
            # then add the extracted image we just split by    
            node_list.append(TextNode(image_alt, TextType.IMAGE, image_link))

            # on the last loop, add trailing text if there is any
            if i == len(extracted_images) - 1 and split_node[1]:
                node_list.append(TextNode(split_node[1], TextType.TEXT))

            # set split_node to the remainder of the split text to run through again
            copy_old_node.text = split_node[1]

        # add node_list to the end of new_list
        new_list.extend(node_list)
    return new_list

def split_nodes_link(old_nodes):
     # this is supposed to input a list of nodes, go through each node then split by markdown link 
    new_list = []

    # seperate each node in old_nodes list, if the node is not a text type, append to new list
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_list.append(old_node)
            continue
           
        node_list = [] 
            
        # uses extraction functions to pull out
        extracted_links = extract_markdown_links(old_node.text)
        # if no images add node to the new_list
        if not extracted_links:
            new_list.append(old_node)
            continue

        # copy of split node that I can alter without breaking extracted_links
        copy_old_node = old_node
        
        for i in range(len(extracted_links)):
            link_text = extracted_links[i][0]
            link_url = extracted_links[i][1]

            # split the copy of old_node by first link in string for this iteration
            split_node = copy_old_node.text.split(f"[{link_text}]({link_url})", 1)

            # if the 1st index of split node is not empty, add to node_list
            if split_node[0]:
                node_list.append(TextNode(split_node[0], TextType.TEXT))
            # then add the extracted link we just split by    
            node_list.append(TextNode(link_text, TextType.LINK, link_url))

            # on the last loop, add trailing text if there is any
            if i == len(extracted_links) - 1 and split_node[1]:
                node_list.append(TextNode(split_node[1], TextType.TEXT))

            # set split_node to the remainder of the split text to run through again
            copy_old_node.text = split_node[1]

        # add node_list to the end of new_list
        new_list.extend(node_list)
    return new_list

def extract_markdown_images(text):
        # finds every alt text and url in text then returns a list of tuples ("alt_text", "url")
        matches = list(re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
        return matches

def extract_markdown_links(text):
        # finds links then returns a list of tuples ("link_text, "url")
        matches = list(re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text))
        return matches











    