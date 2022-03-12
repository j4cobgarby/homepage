import jinja2
from os import listdir, stat
import datetime

file_list = [[
        p, 
        datetime.date.fromtimestamp(stat("posts/"+p).st_ctime)
    ] for p in listdir("./posts")]
print(file_list)

page = jinja2.Environment(loader=jinja2.FileSystemLoader("./")).get_template("template.html")

with open("index.html", "w") as f:
    f.write(page.render(file_list=file_list))