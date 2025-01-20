import os
import shutil
from generation import (
    clean_directory,
    transfer_static_to_public,
    generate_pages_recursive
    
)

static = "./static"
destination = "./public"
index_dest = "./public/"
template = "./template.html"
source = "./content/"
def main():
    clean_directory(static, destination)
    transfer_static_to_public(static, destination)
    generate_pages_recursive(source, template, index_dest)




main()