#imports
from jinja2 import Template
import glob
import os

#Functions
    #Initiates script
def main():
    generate_list()
    apply_template()

    #generates web page list 
def generate_list():
    all_html_files = glob.glob("content/*.html")

    pages=[]
    for file in all_html_files:
        file_path = file
        file_name = os.path.basename(file_path)
        name_only, extension = os.path.splitext(file_name)

        pages.append(
            {
            "filename" : file_path,
            "title" : name_only,
            "output" : "docs/"+file_name,
            },
        )
    return pages 

    #Updates final site with updates from content/header/footer, adds titles
def apply_template():
    for page in generate_list():
        page_title = page["title"]
        final_file = page["output"]
        content_path = page["filename"]

        content_html = open(content_path).read()
        template_html = open("templates/base.html").read()
        template = Template(template_html)

        output = template.render(
            title= page_title,
            content=content_html,
            )

        open(final_file, 'w+').write(output)
# Script
if __name__ == "__main__":
    main()



