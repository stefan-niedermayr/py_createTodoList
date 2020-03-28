#! python3
# createTodoList.py - Creates template for Todo-List (Textfile), with legend
# Usage:                + py.exe createTodoList <Path (opt.)> <Name of List (opt.)>
#                       + No <Name of List> --> No Title, Generic Filename
#                       + No <Path> --> 



import os, sys, shutil, datetime

def createTodoList(pathOfList, title="todoList"):
    creationDate = datetime.datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
    creationDateFilename = datetime.datetime.now().strftime("%Y%m%d_")

    todoListSettings = {
        "width": 80,
        "headerSep": "#",
        "legendSep": "-",
        "checkListSymbol": "[ ]",
        "title": title,
        "pathOfList": pathOfList,
        "fileName": creationDateFilename + title + ".txt",
        "creationDate": creationDate
    }
    pathOfListWithFilename = os.path.join(todoListSettings["pathOfList"], todoListSettings["fileName"])
    if os.path.exists(pathOfListWithFilename):
        raise Exception("File already exists. Abort.")
    todoListFile = open(pathOfListWithFilename, 'w')

    todoListString = (
                    "#"*todoListSettings["width"] + "\n" +                                              # Header Start
                    "Todo-List: " + todoListSettings["title"] + "\n" +      # Header Title
                    "Created on: " + todoListSettings["creationDate"] + "\n" +                          # Header Creation Date
                    "Last change:\n" +                                                                  # Header Last Change
                    "#" * todoListSettings["width"] + "\n" +                                            # Header End
                    "Legend:\n" + "-"*7 + "\n" +                                                        # Legend Descr. Start
                    "[ ] empty task\n" +
                    "[X] completed task\n" + 
                    "[.] task in progress\n" +
                    "[?] task that needs clarification\n" +
                    "[-] task that have been canceld\n" + 
                    "#"*todoListSettings["width"] + "\n" +                                              # Lengend Desc. End
                    "Tasks:\n" +                                                                        # Body Start
                    (todoListSettings["checkListSymbol"] + "\n")*10 +                                   # Body Start
                    "#"*todoListSettings["width"] + "\n"                                                # Bodys End                                
    )

    todoListFile.write(todoListString)
    todoListFile.close()

if len(sys.argv) < 2:
    createTodoList(os.getcwd())                             # create todo list in current path without title
elif len(sys.argv) == 2:
    createTodoList(sys.argv[1])                             # create todo list in path with generic title
elif len(sys.argv) == 3:
    createTodoList(sys.argv[1], sys.argv[2])                # create todo list in path with title   
