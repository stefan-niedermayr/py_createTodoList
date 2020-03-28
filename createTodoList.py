#!python3
# createTodoList.py
# ------------------------------------------------------------------------------
# File          createTodoList.py
# Date          28-03-2020
# Author        Stefan Niedermayr
# Version       1.0.0
# Python-Ver.   3.8.1
# License       GNU GPLv3
# Description   Creates a Todo-List in a simple text file.
# ------------------------------------------------------------------------------
import os, sys, argparse
from datetime import datetime
from datetime import date
from datetime import timedelta
# ------------------------------------------------------------------------------
# GLOBAL VARIABLE DEFINITIONS
# ------------------------------------------------------------------------------
# Todolist Settings
tlSet = {
    "width": 80,
    "headSep": "#",
    "legdSep": "-",
    "taskSep": "-",
    "bodySep": "#",
    "lstSymb": "[][]",

    "dirPath": os.getcwd(),

    "creationDate": datetime.now().strftime("%d-%m-%Y"),
    "creationDateStr": datetime.now().strftime("%Y%m%d_"),

    "startWeekDate": "",
    "endWeekDate": "",
    "calendarWeek": "",

    "ftitle": "todolist",
    "fileExt": ".txt",
}

# Todolist String
tlStr = (
    tlSet["headSep"] * tlSet["width"] + "\n" +          # Header Start
    "Todo-List\n" +                                     # Header Title
    "Created on: " + tlSet["creationDate"] + "\n" +     # Header Creation Date
    "Last change: " + tlSet["creationDate"] + "\n" +    # Header Last Change
    "Calendar Week: calendarWeek\n" +                   # Header Calendar Week 
    "Date: startWeekDate until endWeekDate\n" +         # Header Start-End Date
    tlSet["headSep"] * tlSet["width"] + "\n" +          # Header End
    "Legend:\n" + tlSet["legdSep"] * 7 + "\n" +         # Legend Descr. Start
    "[ ][task-type] empty task\n" +
    "[X][task-type] completed task\n" + 
    "[.][task-type] task in progress\n" +
    "[?][task-type] task that needs clarification\n" +
    "[-][task-type] task that have been canceld\n" + 
    tlSet["legdSep"] * tlSet["width"] + "\n" +           # Lengend Desc. End
    "Tasks:\n" + tlSet["taskSep"] * 6 + "\n" +           # Body Start
    (tlSet["lstSymb"] + "\n")*10 +                       # Body Start
    tlSet["bodySep"] * tlSet["width"] + "\n"             # Body End                                
)

#-------------------------------------------------------------------------------
# FUNCTION DECLARATIONS
#-------------------------------------------------------------------------------
## printLine()
#  Function to print a line in the console at a constant length.
def printLine():
    print(tlSet["width"] * "-")
# END printLine

## printHeader()
#  Function to print header of script.
def printHeader():
    printLine()
    print("createTodoList.py")
    printLine()
# END printHeader

## calcStartEndWeekDate(dateStr)
#  Function to calculate the start- and end-date of a calendar-week. 
#  Dates are determined from a date-string in the format "DD-MM-YYYY"
#
#  param dateStr    Date string in format "DD-MM-YYYY"
#  return           startWeekDate, endWeekDate
def calcStartEndWeekDate(dateStr=None):
    if dateStr==None:
        # If no specific date is passed, use creation date.
        dateStr = tlSet["creationDate"]

    # Convert to datetime object.
    dateObj = datetime.strptime(dateStr, '%d-%m-%Y')
    startWeekDate = dateObj - timedelta(days=dateObj.weekday())
    endWeekDate = startWeekDate + timedelta(days=6)
    # Reformatting start- and endweek dates.
    startWeekDate = startWeekDate.strftime("%d-%m-%Y")
    endWeekDate = endWeekDate.strftime("%d-%m-%Y")

    return startWeekDate, endWeekDate
# END calcStartEndWeekDate

## createFileName()
#  Function to compose the filename.
#  Default format: YYYYMMDD_<ftitle><fileExt>
def createFileName(ftitle=None):
    # Check if a user defined ftitle is provided.
    if ftitle != None:
        # Update ftitle with user provided one.
        tlSet["ftitle"] = str(ftitle)

    # Compose fileName.
    fileName = tlSet["creationDateStr"] + tlSet["ftitle"] + tlSet["fileExt"]

    return fileName
# END createFileName

## createTodoList()
#  Function that creates the Todo-List.
#
#  param dirPath    Path of a directory where Todo-List should be created.
#                   Default is the current working directory.
#  param ftitle     Customizable file title. Prefix (YYYYMMDD_) and file 
#                   file extensions are not influenced by this parameter.
#  param dateStr    Datestring can be provided in the format "DD-MM-YYYY"
#                   This may be used, for creating Todo-Lists in advance.
#                   If a date in a certain calendar week is provided, the
#                   list will be generated for this calendar week.
#  return           Returns 0 if everything went OK. Returns 1 if creation
#                   failed.
def createTodoList(dirPath=None, ftitle=None, dateStr=None):
    # Check if a dirPath has been passed.
    if dirPath != None:
        if os.path.exists(dirPath):
            # dirPath is an existing directory. Update tlSet["dirPath"]
            tlSet["dirPath"] = dirPath
        else:
            # dirPath is not an existing directory. Fall back to current dir.
            tlSet["dirPath"] = os.getcwd()

    # Check if a date str (format "DD-MM-YYYY") has been passed.
    if dateStr == None:
        # No dateStr passed, use today's date.
        tlSet["calendarWeek"] = str(date.today().isocalendar()[1])
    else:
        # Create date object.
        tmpDate = datetime.strptime(dateStr, "%d-%m-%Y")
        # Get calendar week and store it in settings.
        tlSet["calendarWeek"] = str(tmpDate.isocalendar()[1])

    # Create filename.
    fileName = createFileName(ftitle)

    # Create absolute filepath.
    filePath = os.path.join(tlSet["dirPath"], fileName)

    # Check if todolist already exists in filepath.
    if os.path.exists(filePath):
        # Todolist already exists, return 1.
        print("Todolist already exists in filepath. Exit.")
        return 1

    # Update todolist string with calendar week.
    tmp_tlStr1 = tlStr.replace("calendarWeek", tlSet["calendarWeek"])

    # Calculate start- and end-date of a calendar week.
    tlSet["startWeekDate"], tlSet["endWeekDate"] = calcStartEndWeekDate(dateStr)

    # Update todolist string with start- and end dates of a given week.
    tmp_tlStr2 = tmp_tlStr1.replace("startWeekDate", tlSet["startWeekDate"])
    tmp_tlStr3 = tmp_tlStr2.replace("endWeekDate", tlSet["endWeekDate"])

    # Create todolist file.
    tlFile = open(filePath, 'w')

    # Write last modified tlStr (tmp_tlStr3) to tlFile.
    tlFile.write(tmp_tlStr3)
    
    tlFile.close()

    print("Todo-List created: " + filePath)

    return 0
# END createTodoList

# ------------------------------------------------------------------------------
# MAIN ROUTINE
# ------------------------------------------------------------------------------
# Parser
parser = argparse.ArgumentParser(description=r'''createTodoList.py''',
        formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-dir", help="Path where todolist should be written " + 
                    "to.", type=str)
parser.add_argument("-ftitle", help="Defines the title of the file. General " +
                    " filename style: YYYYMMDD_ftitle.txt", type=str)
parser.add_argument("-datestr", help="Date-String in format \"DD-MM-YYYY\". " +
                    "Given date is used to calculate calendar week and " + 
                    "start- and end-date of given calendar week.", type=str)
args = parser.parse_args()
# Print Header
printHeader()
# Create TodoList
createTodoList(args.dir, args.ftitle, args.datestr)