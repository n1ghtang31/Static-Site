import os
import shutil
from markdown_blocks import markdown_to_html_node

LOGGING = 1

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    with open(template_path, 'r') as file:
        template_content = file.read()
    converted_markdown = markdown_to_html_node(markdown_content).to_html()
    #print(converted_markdown.to_html())
    title_text = extract_title(markdown_content)
    
    final_html = template_content.replace('{{ Title }}', title_text)
    final_html = final_html.replace('{{ Content }}', converted_markdown)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, 'w') as file:
        file.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        extra_log("folder does not exist creating", dest_dir_path)
        os.makedirs(dest_dir_path)

    for item in os.listdir(dir_path_content):

        source_path = os.path.join(dir_path_content, item)
        if item.endswith(".md"):
            item = item.replace(".md", ".html")
        destination_path = os.path.join(dest_dir_path, item)
        if item[0] == ".":
            continue
        
        if os.path.isdir(source_path):
            generate_pages_recursive(source_path, template_path, destination_path)
        else:
            extra_log("Generating page for", item)
            #need to change this to look at items not path
            generate_page(source_path, template_path, destination_path)

def extract_title(markdown):
    split_markdown = markdown.split("\n")
    found = 0
    for line in split_markdown:
        if found == 1:
            continue
        if line.startswith("# "):
            
            return line[2:].strip()
        
    raise Exception("No header present")



def extra_log(text, variable_key):
    if LOGGING == 0:
        return
    elif LOGGING == 1:
        return print(f"{text}: {variable_key}")
    else:
        raise ValueError("LOGGING Value is set incorrectly")


def transfer_static_to_public(source, destination):
    if not os.path.exists(destination):
        extra_log("folder does not exist creating", destination)
        os.makedirs(destination)

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if item[0] == ".":
            continue

        if os.path.isdir(source_path):
            transfer_static_to_public(source_path, destination_path)
        else:
            extra_log("copying file", item)
            shutil.copy(source_path, destination_path)


def clean_directory(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source folder is missing: {source}")
    if not os.path.exists(destination):
        extra_log("folder does not exist creating", destination)
        os.makedirs(destination)
    else:
        # Remove all files in the original destination folder
        for item in os.listdir(destination):
            item_path = os.path.join(destination, item)
            if os.path.isdir(item_path):
                extra_log("removing folder", item_path)
                shutil.rmtree(item_path)
            else:
                extra_log("removing", item_path)
                os.remove(item_path)




