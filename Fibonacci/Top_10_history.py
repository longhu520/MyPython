import sys
import pathlib
import sqlite3
from tkinter import Tk, Frame, Text, filedialog, messagebox, END

"""
# Get history file Path
try :
    historyFilePath = pathlib.Path(sys.argv[1])
except IndexError :
    sys.exit("Please enter one path in parameter")
"""
app = Tk()
app.title('Top 10 sites visit')
window = Frame(app, height= 50, width=100)
textZone = Text(window, height=50, width=100)
textZone.pack()
window.pack()

historyFilePath = filedialog.askdirectory()
if not historyFilePath :
    sys.exit(0)

historyFile = pathlib.Path(historyFilePath) / "History.db"

# Check File exist
if not historyFile.is_file() :
    # sys.exit("File not exist :" + str(historyFile))
    messagebox.showwarning(
        "Error",
        "Can not find history file!"
    )
    sys.exit(0)

# Database connexion
connexion = sqlite3.connect(historyFile)
cursor = connexion.cursor()

request = """
    select url,visit_count from history_items
order by visit_count desc
"""

result = cursor.execute(request)
for site,count in list(result)[0:10] :
    # print(site, ":", count)
    line = site + " : " + str(count) + " visits \n"
    textZone.insert(END,line)

app.mainloop()