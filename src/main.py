import os
import shutil

LOGGING = 1
source = "./static"
destination = "./public"

def main():
    transfer_static_to_public(source, destination)

def extra_log(text, variable_key):
    if LOGGING == 0:
        return
    elif LOGGING == 1:
        return print(f"{text}: {variable_key}")
    else:
        raise ValueError("LOGGING Value is set incorrectly")


def transfer_static_to_public(source, destination):
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


main()