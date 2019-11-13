# Functions/Lists
pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "About Me",
        "active": "{{active_home}}"
    },
    {
        "filename" : "content/blog.html",
        "output" : "docs/blog.html",
        "title" : "Blog",
        "active": "{{active_blog}}"
    },
    {
        "filename" : "content/port.html",
        "output" : "docs/port.html",
        "title" : "Portfolio",
        "active": "{{active_port}}"
    },
]
    #saves out each webpage
def main():
    full_page = apply_base()
    web_page = page["output"]
    open(web_page, 'w+').write(full_page)

    #adds the header and footer to each content page
def apply_base():
    active_page = apply_active()
    page_name = page["filename"]
    content = open(page_name).read()
    full_page = active_page.replace("{{content}}", content)
    return full_page

    #adds the title to each webpage
def apply_title():
    base_html = open("templates/base.html").read()
    page_tile = page["title"]
    entitled_page = base_html.replace("{{title}}", page_tile)
    return entitled_page

    #makes the active page black in the nav
def apply_active():
    entitled_page = apply_title()
    activator = page["active"]
    active_page= entitled_page.replace(activator, "active")
    return active_page

    #apologizes in terminal for not putting arguments in my other functions
def argument(name,msg):
    print("Sorry", name, ",", msg, "figure out where an argument made sense in my other functions.")    

# Script

for page in pages:
     apply_title()
     apply_active()
     apply_base()
     if __name__ == "__main__":
        main()
argument("Teach", "I couldn't")