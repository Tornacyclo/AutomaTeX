# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:39:36 2024

@author: berth
"""

import os
import shutil
import re



def sanitize_folder_name(folder_name):
    # Replace invalid characters with an underscore
    return re.sub(r'[<>:"/\\|?*]', '_', folder_name)

def create_folder(folder_name):
    """Creates a new folder if it doesn't exist."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")

def copy_files(folder_name, language):
    """Copies to the newly created folder."""
    # Define paths to the source files
    if language == 'EN':
        tex_src = "EN.tex"
    elif language == 'FR':
        tex_src = "FR.tex"
    else:
        raise ValueError("Language must be 'EN' or 'FR'.")

    # Define the destination paths in the newly created folder
    tex_dst = os.path.join(folder_name, os.path.basename(tex_src))

    # Copy the files
    shutil.copy(tex_src, tex_dst)
    print(f"Copied {tex_src} to {tex_dst}")
    
    return tex_dst

def modify_(**kwargs):
    """Modifies."""
    with open(kwargs['tex_path'], 'r') as file:
        content = file.read()

    # Replace placeholders
    content = content.replace(r"\setkomavar{city}{}", f"\\setkomavar{{city}}{{{kwargs['city']}}}")
    content = content.replace(r"\setkomavar{person}{}", f"\\setkomavar{{person}}{{{kwargs['person']}}}")

    # Write the modified content back to the file
    with open(kwargs['tex_path'], 'w') as file:
        file.write(content)
    
    print(f"Modified {kwargs['tex_path']} with the new city and person.")

def compile_tex_file(tex_file_path):
    """Compiles the .tex file using XeLaTeX, MakeIndex, and BibTeX."""
    
    os.system(f"texify.exe --pdf --engine=xetex --synctex=1 --clean {tex_file_path}")
    
    print(f"Compiled {tex_file_path} using XeLaTeX+MakeIndex+BibTeX.")


def main():
    # Read the number of test cases
    T = int(input())

    # Loop over each test case
    for t in range(1, T + 1):
        person_city = input().strip()
        # person, city = person_city.split(' ', 1)  # Split based on the first space
        person, city, language = person_city.split(' ')

        folder_name = sanitize_folder_name(f"{person}_{city.replace(' ', '_')}")
        
        create_folder(folder_name)

        # Copy based on language
        tex_path = copy_files(folder_name, language)

        # Modify with variables
        modify_(tex_path=tex_path, city=city, person=person)

        # Compile both .tex files using XeLaTeX, MakeIndex, and BibTeX
        original_dir = os.getcwd()
        os.chdir(f"./{folder_name}")
        compile_tex_file(os.path.basename(tex_path))
        os.chdir(original_dir)


if __name__ == "__main__":
    main()
