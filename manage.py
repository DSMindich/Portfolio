import utils
import sys

#print("This is argv:", sys.argv)
def main():
    if len(sys.argv) == 1:
        print("Usage:")
        print("Rebuild site: python manage.py build")
        print("Create new page: python manage.py new")
    else:
        command = sys.argv[1]
        if command == "build":
            print("Build was specified")
            utils.initiate()
        elif command == "new":
            print("New page was specified")
            open("content/new.html", "w+").write("<h1>New Content!</h1> <p>New content...</p>")
        else:
            print("Please specify ’build’ or ’new’")


if __name__ == "__main__":
    main()