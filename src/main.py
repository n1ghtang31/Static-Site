import os
import shutil
from generation import (
    clean_directory,
    transfer_static_to_public,
    generate_page
    
)

static = "./static"
destination = "./public"
index_dest = "./public/index.html"
template = "./template.html"
source = "./content/index.md"
def main():
    clean_directory(static, destination)
    transfer_static_to_public(static, destination)
    generate_page(source, template, index_dest)




main()