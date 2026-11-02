'''
Pretty Table Example
prettytable wiki documentation: 
https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
'''

# Import Python Standard Libraries
import os
import sys
import time
import webbrowser

# Import 3rd Party Library
from prettytable import PrettyTable, TableStyle

# Create Prettytable with Heading
my_table = PrettyTable(['File Name', 'Type', 'File Size', 'Last Modified', 'Epoch'])

DIRECTORY = "."
# set a directory to scan
try:
    # Get a list of files    
    file_list = os.listdir(DIRECTORY)
    
    # Loop through each file
    for each_file in file_list:
        # Get the full path
        path = os.path.join(DIRECTORY, each_file)
        
        if os.path.isfile(path):
            file_type = "File"
        elif os.path.isdir(path):
            file_type = "Dir"
        elif os.path.islink(path):
            file_type = "Link"
        else:
            file_type = "Unknown"
            
        # obtain the stats 
        file_stats = os.stat(path)
        
        # Extract required properties
        file_size = file_stats.st_size
        last_mod_as_unix_epoch = file_stats.st_mtime
        last_modified = time.ctime(last_mod_as_unix_epoch)
        
        # add a row to the table for each file
        my_table.add_row([path, file_type, file_size, last_modified, last_mod_as_unix_epoch])
        
except Exception as err:
    sys.exit("Error: "+str(err))
     
my_table.align='l'
my_table.hrules=1
my_table.set_style(TableStyle.SINGLE_BORDER)

output = my_table.get_string()

# View Ways to Sort the Data

# output = my_table.get_string(sortby='Type')
#output = my_table.get_string(sortby='Epoch', reversesort=True)
#output = my_table.get_string(sortby='File Size', reversesort=True)

print(output)


# Some Simple CSS
css = """
<style>
  :root {
    --bg: #0b1020;
    --text: #e7eaf3;
    --header: #1b2a57;
    --row-even: #0f1730;
    --row-odd: #0c1328;
    --border: transparent;
  }

   body{
    background-color: var(--bg);
    color: var(--text);
    font-family: sans-serif;
   }

  h1 {
    margin: 1em auto;
    text-align: center;
  }

  table {
    width: 80%;
    border-spacing: 0;
    margin: auto;
  }

  th, td {
    padding: 1em;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    white-space: nowrap;
  }

  th {
    background: var(--header);
    color: var(--text);
    text-align: left;
  }

  tbody tr:nth-child(odd) td { background: var(--row-odd); }
  tbody tr:nth-child(even) td { background:  var(--row-even); }
  

  .center {
      margin: auto;
      text-align: center;
  }
  
  .m-1  {
    margin: 1em
  }
  
  .half-width{
      width: 50%;
  }
  
  .rounded-edges {
      border-radius: 1em;
  }
</style>
"""

html_table = my_table.get_html_string(sortby='File Size', reversesort=True)


html = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
    </head>
    {css}
    <body>
        <h1>Image Processing Results</h1>
        {html_table}
        <p class="m-1 center">Here's a picture for your viewing pleasure:</p>
        <div class="m-1 center">
            <img class="half-width rounded-edges" src="../images/Turtle.jpg" alt="Turtle posing for the camera underwater."">
        </div>
    </body>
</html>"""


HTML_FILE_LOCATION = "../docs/table.html"
with open(HTML_FILE_LOCATION, 'w') as f:
    f.write(html)

webbrowser.open('file://' + os.path.realpath(HTML_FILE_LOCATION))
