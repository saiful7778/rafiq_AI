import os
import shutil

global htmlfile, cssfile, jsfile

pathoftemplate = "H:\\Rafiq-a.i\\website template"

def website(query):
    try:
        os.chdir(pathoftemplate)
        foldername = str(query)
        os.makedirs(foldername)
        # html file
        global htmlfile 
        htmlfile = pathoftemplate+"\\"+foldername+"\\index.html"
        f = open(htmlfile, "x")
        childpath = pathoftemplate+"\\"+foldername
        os.chdir(childpath)
        cssfolder = "css"
        jsfolder = "js"
        imgfolder = "img"
        # css folder
        os.makedirs(cssfolder)
        # style.css file
        global cssfile
        cssfile = childpath+"\\"+cssfolder+"\\style.css"
        f = open(cssfile, "x")
        # js folder
        os.makedirs(jsfolder)
        # script.js file
        global jsfile
        jsfile = childpath+"\\"+jsfolder+"\\script.js"
        f = open(jsfile, "x")
        # img folder
        os.makedirs(imgfolder)
        # favicon folder
        os.makedirs(imgfolder+"\\"+'favicon')
        # copy favicon
        favicon = "H:\\Rafiq-a.i\\database\\features_function\\web_template\\favicon\\favicon.ico"
        dirfavicon = pathoftemplate+"\\"+foldername+"\\"+imgfolder+"\\"+'favicon'
        shutil.copy(favicon, dirfavicon)
        # import scratch founction
        fromScratch()
    except:
        print("no")

def fromScratch():
    global htmlfile
    with open("H:/Rafiq-a.i/database/features_function/web_template/demo.html", "r", encoding="utf-8") as r:
        html = r.read()
    with open(htmlfile, 'w') as h:
        h.write(html)
        h.close()
    global cssfile
    with open(cssfile, "a") as c:
        defaultStyle = "@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');*{margin: 0; padding: 0; font-family: 'Poppins';}"
        c.write(defaultStyle)
        c.close()
    
