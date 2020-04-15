# createTodoList.py

Simple script to create todolists in textfile format.

## Installation

Copy the createTodoList.py script in a local user directory and directly run it
 from there.

## Usage example

Change into the directory where the createTodoList.py script is located.

Get help for using this script:

```sh
python createTodoList.py --help
```

Create a Todo-List with standard filename (YYMMDD_todolist.txt):

```sh
python createTodoList.py
```

Create a Todo-List in an argument provided path.

```sh
python createTodoList.py -dir "~/home/stefan-e495/Temp/"
```

Create a Todo-List with a user specific filename, following the "YYMMDD_" string.

```sh
python createTodoList.py -ftitle "myTodo"
```

Create a Todo-List for certain calenderweek. The user provides a date of a calender week. Start- and end-date are calculated and inserted in the Todo-Lists date section. Date must be provided "DD-MM-YYYY"

```sh
python createTodoList.py -datestr "24-04-2020"
```

## Release History

* 1.0.0
  * First proper release
