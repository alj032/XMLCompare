import difflib
import os
import sys
import filecmp
import webbrowser
from tkinter import Tk
from tkinter.filedialog import askdirectory


mainFolder = askdirectory(title='Select Master Folder')
compareFolder = askdirectory(title='Select Compare Folder')

for file in os.listdir(mainFolder):
    src = mainFolder + '\\' + file
    dst = mainFolder + '\\' + file[:-3] + 'txt'
    os.rename(src, dst)

for file in os.listdir(compareFolder):
    src = compareFolder + '\\' + file
    dst = compareFolder + '\\' + file[:-3] + 'txt'
    os.rename(src, dst)
    

result  =  filecmp.dircmp(mainFolder, compareFolder)


for file in os.listdir(mainFolder):
    src = mainFolder + '\\' + file
    dst = mainFolder + '\\' + file[:-3] + 'xml'
    os.rename(src, dst)

for file in os.listdir(compareFolder):
    src = compareFolder + '\\' + file
    dst = compareFolder + '\\' + file[:-3] + 'xml'
    os.rename(src, dst)



htmFile = open("SummaryReport.html","w")
htmFile.write("""
                    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
                            "http://www.w3.org/TR/html4/loose.dtd">
                    <html>
                    <head>
                        <title>Zebra</title>
                        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
                        <style>
* {
  box-sizing: border-box;
}

.row {
  display: flex;

}
.row:nth-child(odd) {
  background-color: gray;
}

/* Create two equal columns that sits next to each other */
.column {
  flex: 50%;
  padding: 10px;
  text-align: center;
}
html {
        background-color: #B0B0B0;
        height: 50%;
        overflow: scroll;
        }
.row {
         
         }
</style>
                    </head>
                    <body>
                    <h1 align=center> Zebra Datawedge Comparison Report</h1>
                    <div class='row'>
                    """)

htmFile.flush()

print(len(result.left_list))
print(len(result.right_list))

print('Folder Comparison Reporter Version 1.0\n')



#
# MASTER FILE LIST START
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='column'>
                    <h1>Files in Master folder: [""" + str(len(result.left_list)) + """]</h1>
                        <select multiple="multiple" size=auto>
                """ )
htmFile.flush()


mainfolderfilelist = result.left_list
#This means the same file name existed in both folders but the contents of the file is slightly different.

for file in mainfolderfilelist:
    
    htmFile = open("SummaryReport.html","a")
    htmFile.write('<option>' + file + '</option>' + '<br>')
    htmFile.flush()


htmFile = open("SummaryReport.html","a")
htmFile.write("""</select>
                    </div>""" )
htmFile.flush()

#
# MASTER FILE LIST END
#




#
# COMPARE FILE LIST START
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='column'>
                    <h1>Files in Compare Folder: [""" + str(len(result.right_list)) + """]</h1>
                        <select multiple="multiple" size=auto>
                """ )
htmFile.flush()


comparefolderfilelist = result.right_list
#This means the same file name existed in both folders but the contents of the file is slightly different.

for file in comparefolderfilelist:
    
    htmFile = open("SummaryReport.html","a")
    htmFile.write('<option>' + file + '</option>' + '<br>')
    htmFile.flush()


htmFile = open("SummaryReport.html","a")
htmFile.write("""</select>
                    </div>
                    </div>""" )
htmFile.flush()

#
# COMPARE FILE LIST END
#

#
# CREATE NEW DIV TO STORE FILE ONLY FOUND IN X FOLDER
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='row'>
                """ )
htmFile.flush()


#
# FILE ONLY IN MASTER FOLDER LIST START
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='column'>
                    <h1>Files in Master but NOT in Compare: [""" + str(len(result.left_only)) + """]</h1>
                    <ul>
                """ )
htmFile.flush()

mainfolderonly = result.left_only
#This means the same file name existed in both folders but the contents of the file is slightly different.

for file in mainfolderonly:
    
    htmFile = open("SummaryReport.html","a")
    htmFile.write('<li > <a href="' + (mainFolder + '\\' + file) + '">' + (mainFolder + '\\' + file) + '</a> </li>')
    htmFile.flush()


htmFile = open("SummaryReport.html","a")
htmFile.write("""</ul>
                    </div>
                    """ )
htmFile.flush()

#
# FILE ONLY IN MASTER FOLDER LIST END
#



#
# FILE ONLY IN COMPARE FOLDER LIST START
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='column'>
                    <h1>Files in Compare but NOT in Master: [""" + str(len(result.right_only)) + """]</h1>
                    <ul>
                """ )
htmFile.flush()

comparefolderonly = result.right_only
#This means the same file name existed in both folders but the contents of the file is slightly different.

for file in comparefolderonly:
    
    htmFile = open("SummaryReport.html","a")
    htmFile.write('<li > <a href="' + (compareFolder + '\\' + file) + '">' + (compareFolder + '\\' + file) + '</a> </li>')
    htmFile.flush()


htmFile = open("SummaryReport.html","a")
htmFile.write("""</ul>
                    </div>
                    </div>""" )
htmFile.flush()

#
# FILE ONLY IN COMPARE FOLDER LIST END
#



#
# CREATE NEW DIV TO STORE FILE ONLY FOUND IN X FOLDER
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='row'>
                """ )
htmFile.flush()



#
# FILE ONLY IN MASTER FOLDER LIST START
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='column'>
                    <h1>Common Files: [""" + str(len(result.common_files)) + """]</h1>
                    <select multiple="multiple" size=auto>
                """ )
htmFile.flush()

commonfiles = result.common_files
#This means the same file name existed in both folders but the contents of the file is slightly different.

for file in commonfiles:
    
    htmFile = open("SummaryReport.html","a")
    htmFile.write('<option>' + file + '</option>' + '<br>')
    htmFile.flush()


htmFile = open("SummaryReport.html","a")
htmFile.write("""</select>
                    </div>
                    """ )
htmFile.flush()

#
# FILE ONLY IN MASTER FOLDER LIST END
#

#
# FILE ONLY IN MASTER FOLDER LIST START
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='column'>
                    <h1>Identical Files: [""" + str(len(result.same_files)) + """]</h1>
                    <select multiple="multiple" size=auto>
                """ )
htmFile.flush()

samefiles = result.same_files
#This means the same file name existed in both folders but the contents of the file is slightly different.

for file in samefiles:
    
    htmFile = open("SummaryReport.html","a")
    htmFile.write('<option>' + file + '</option>' + '<br>')
    htmFile.flush()


htmFile = open("SummaryReport.html","a")
htmFile.write("""</select>
                    </div>
                    """ )
htmFile.flush()

#
# FILE ONLY IN MASTER FOLDER LIST END
#

#
# FILE ONLY IN MASTER FOLDER LIST START
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='column'>
                    <h1>Changes Detected on File: [""" + str(len(result.diff_files)) + """]</h1>
                    <select multiple="multiple" size=auto>
                """ )
htmFile.flush()

difffiles = result.diff_files
#This means the same file name existed in both folders but the contents of the file is slightly different.

for file in difffiles:
    
    htmFile = open("SummaryReport.html","a")
    htmFile.write('<option>' + file + '</option>' + '<br>')
    htmFile.flush()


htmFile = open("SummaryReport.html","a")
htmFile.write("""</select>
                    </div>
                    </div>
                    """ )
htmFile.flush()

#
# FILE ONLY IN MASTER FOLDER LIST END
#


if not os.path.exists('Reports'):
    os.makedirs('Reports')


#
# CREATE NEW DIV TO STORE FILE ONLY FOUND IN X FOLDER
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='row'>                 
                """ )
htmFile.flush()



htmFile = open("SummaryReport.html","a")
htmFile.write("""<div class='column'>
                    <h1>Difference Report: [""" + str(len(result.diff_files)) + """]</h1>
                    <ul list-style="none">
                """ )
htmFile.flush()


difffiles = result.diff_files 
#This is where we print out the different url paths to the two different folders
for file in difffiles:

    mainURL = mainFolder + '\\' + file
    compareURL = compareFolder + '\\' + file

    first_file = mainURL

    second_file = compareURL

    first_file_lines = open(first_file).readlines()
    second_file_lines = open(second_file).readlines()

    difference = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines, first_file, second_file)
    
    difference_report = open('Reports\\' + file[:-4] + 'XML_Diff_Report.html', 'w')
    difference_report.write(difference)
    difference_report.close()

    

    mainstring = mainURL
    comparestring = compareURL

    htmFile = open("SummaryReport.html","a")
    htmFile.write('<li > <a href="'+ 'Reports\\' + file[:-4] + 'XML_Diff_Report.html' + '">' + (file[:-4] + 'XML_Diff_Report.html') + '</a> </li>' )
    htmFile.flush()
    
    
    


    print(mainURL, compareURL)

    
#
# CREATE NEW DIV TO STORE FILE ONLY FOUND IN X FOLDER
#
htmFile = open("SummaryReport.html","a")
htmFile.write("""
                </ul> 
                </div>                 
                """ )
htmFile.flush()











htmFile = open("SummaryReport.html","a")
htmFile.write("""
            </body>
            </html>

            """)
htmFile.close()


webbrowser.open('SummaryReport.html')






