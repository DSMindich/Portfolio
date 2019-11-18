from jinja2 import Template

def generate_list():
    import glob
    all_html_files = glob.glob("content/*.html")
    
    
    pages=[]
    for file in all_html_files:
        import os
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
def apply_new_template():
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
        print(output)
########
generate_list()
apply_new_template()

