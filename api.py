#The Insert Server Download Asset System..
import base64,requests,robloxapi,time
from flask import Flask,request,jsonify

app = Flask(__name__)

def getRequest():
    return request
##end

#Landing Page (also detects if an id was entered into the address bar and downloads if it is)
@app.route('/')
def index():
    page = """
    <p id='change' class='red3 center ta_c'>Here you will find links to the Reference Documents</p>
    <p class='red3 center'>
        <!--BEGIN DOCUMENTS PAGES-->
        Reference Documents:<br>
        - <a href='/info.asp'>Info</a><br>
        - <a href='/server.py'>Server</a><br>
        - <a href='/terms.asp'>Terms & Conditions</a><br>
        - <a href='/contact.asp'>Contact</a><br>
        <!--END DOCUMENT PAGES-->
    </p>
    """
    theid = None
    asset_type = None
    myQuery = getParams(str(request.url))
    if (myQuery!=None):
        idq = str(myQuery[0])
        tyq = None
        if (len(myQuery)>1):
            tyq = str(myQuery[1])
        ##endif
        if (idq!=None):
            if (tyq==None or tyq=='type=model'):
                theid = int(idq.split('=')[1])
                asset_type = 'rbxm'
                if (theid!=None):
                    page = """
                    <p id='change' class='red3 center ta_c'>AssetId automatically detected. Downloading..</p>
                    <script>
                        setTimeout(function(){
                            document.location.replace('/')
                        },2000)
                    </script>
                    """
                    insertserver.downloadAsset(theid)
                ##endif
            ##endif
        ##endif
    ##endif
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Cloud API - Welcome</title>
        <link rel='icon' href='/images/favicon.ico'/>
        <link rel='stylesheet' href='/css/styles-main.css'/>
    </head>
    <body>
	<div id='page_content' class='center a_up'>
	    <h1 class='red1 center'>Welcome!</h1>
	    <h2 class='red2 center ta_c'>Welcome to the Insert Cloud landing page!</h2>
	    """+page+"""
	</div>
    </body>
</html>
"""
##end

#DOWNLOADER API
@app.route('/api/')
def api():
    theid = None
    asset_type = None
    myQuery = getParams(str(request.url))
    if (myQuery!=None):
        idq = str(myQuery[0])
        tyq = None
        if (len(myQuery)>1):
            tyq = str(myQuery[1])
        ##endif
        if (idq!=None):
            if (tyq==None or tyq=='type=model'):
                theid = int(idq.split('=')[1])
                asset_type = 'rbxm'
                if (theid!=None):
                    insertserver.downloadAsset(theid)
                ##endif
            ##endif
        ##endif
    ##endif
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Cloud API - Asset Downloader</title>
        <link rel='icon' href='/images/favicon.ico'/>
        <link rel='stylesheet' href='/css/styles-main.css'/>
    </head>
    <body>
        <h1 class='red1'>Insert Cloud API Server: </h1>
        <h2 class='red2'>Download Asset Request Recieved.</h2>
        <p class='red3'>Asset Location: <a href='/assets/v1/"""+str(theid)+"""'>/assets/v1/"""+str(theid)+"""</a></p>
    </body>
</html>
"""
##end

#<!--BEGIN DOCUMENTS PAGES-->
@app.route('/info.asp')
def info():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Cloud - Use and Info</title>
        <link rel='icon' href='/images/favicon.ico'/>
        <link rel='stylesheet' href='/css/styles-main.css'/>
        <script src='/js/insertcloud_info.js'></script>
    </head>
    <body>
        <h1 class='red2'>Insert Cloud API, An open-sourced alternative to the InsertService.</h1>
        <h3 class='red1'>The Insert Cloud API Is an open-sourced, dynamic, alternative to the insert service.<br>
            This API allows you to load any public / uncopylocked model into the game and is versitile in many ways.<br>
            When used in conjuction with a properly configured webserver, is quite dynamic and can load models quickly<br>
            and efficiently.
            <br>
            <br>
            This API functions by first sending a request from a game to the webserver (which you will have to set up).<br>
            That will then process the request and download the model.<br>
            The very next thing that happens is the server sends a request to the ROBLOX API acting as if the owner has bought or<br>
            'taken' the model and then sends a request back to the game allowing the game to compile and load the model.
        </h3>
        <br>
        <h1 class='red2'>How it works:</h1>
        <br>
        <div id='normal'>
            <img src='/images/diagram.svg' style='width: 20%'></img>
        </div>
        <div id='bigger' hidden>
            <img src='/images/diagram.svg' style='width: 40%'></img>
        </div>
        <br>
    </body>
</html>
    """
##end
@app.route('/server.py')
def server():
    ver = '1.0.0'
    page="""
<p id='code' class='red1'>
    Version: """+ver+"""
</p>
"""
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Cloud - Server Info</title>
        <link rel='icon' href='/images/favicon.ico'/>
        <link rel='stylesheet' href='/css/styles-main.css'/>
        <script src='/js/insertcloud_info.js'></script>
    </head>
    <body>
        <h1 class='red2'>Insert Cloud API Server: </h1>
        """+page+"""
    </body>
</html>
    """
##end
@app.route('/terms.asp')
def terms():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Cloud - Terms</title>
        <link rel='icon' href='images/favicon.ico'/>
        <link rel='stylesheet' href='/css/styles-main.css'/>
    </head>
    <body>
        <h1 class='red1 center ta_c'>Terms and Conditions: </h1>
        <br>
        <h2 class='red2 center ta_c'>Insert Cloud is a useful and adaptive API,<br>However there are some rules to the use of the API.</h2>
        <br>
        <p class='red1 center ta_c'><u>Roblox Appropriate Content</u></p>
        <ul class='red3 center ta_c'>
            <li class='red3 center ta_c'>- If anything against <a href='https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Standards'>Roblox Community Standards</a> is inserted using Insert Cloud API,<br>The API will be suspended from use by EVERYONE.</li>
            <li class='red3 center ta_c'>- All Requests are logged, if anything that is in violation of Insert Cloud Terms and Conditions is found, <br>It will be blacklisted.</li>
            <li class='red3 center ta_c'>- Attempts to insert blacklisted assets will result in suspension of the API.</li>
        </ul>
        <br>
        <p class='red1 center ta_c'><u>Insert Cloud API Rules.</u></p>
        <ul class='red3 center ta_c'>
            <li class='red3 center ta_c'>- The Insert Cloud API is Open-Sourced but we prohibit the use of external URLs to load the API.</li>
        </ul>
    </body>
</html>
"""
##end
@app.route('/contact.asp')
def contactPage():
    page = """
<p class='red3'>Contacts: <br>
    GitHub: @Captian-obvious<br>
    Mobile: @undefined<br>
    PythonAnywhere: @CaptianObvious<br>
</p>
"""
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Cloud - Contact Me</title>
        <link rel='icon' href='images/favicon.ico'/>
        <link rel='stylesheet' href='/css/styles-main.css'/>
    </head>
    <body>
        <h1 class='red2'>Contact Developer: </h1>
        """+page+"""
    </body>
</html>
"""
##end
#<!--END DOCUMENT PAGES-->

#COMPILER
@app.route('/compiler')
def compiler():
    myQuery = getParams(request.url)
    b64_decoded = None
    if (myQuery!=None):
        param1 = myQuery[0]
        if (param1!=None):
            data = param1
            d = data.encode('ascii')
            s = base64.b64decode(d)
            b64_decoded = str(s.decode('ascii'))
        ##endif
    ##endif
    return """
{
    'tree':{
        {
            'ClassName':'class';
            'Parent': 'parent';
            'Children': {

            };
        };
    };
}
"""
##end

#some server info below here
def getParams(url):
    if (len(url.split('?'))>1):
        query = url.split('?')[1]
        params = query.split('&')
        return params
    ##endif
##end

class insertserver:
    def downloadAsset(assetid):
        url = 'https://assetdelivery.roblox.com/v1/asset/?id='+str(assetid)
        REQUEST = requests.get(url)
        if (REQUEST.status_code<400):
            rawData = REQUEST.content
            asset = open('assets/v1/'+str(assetid), "wb")
            asset.write(bytearray(rawData))
            #asset.write(str(rawData))
            return asset
        else:
            print('REQUEST_ERROR: '+str(REQUEST.status_code))
            return {'STATUS_CODE':REQUEST.status_code,'ERROR_MESSAGE':'REQUEST_ERROR: '+str(REQUEST.status_code)}
        ##endif
    ##end
    def downloadAudio(assetid):
        url = 'https://api.hyra.io/audio/'+str(assetid)
        REQUEST = requests.get(url)
        if (REQUEST.status_code<400):
            rawData = REQUEST.content
            asset = open('assets/v1/mp3/'+str(assetid)+".mp3", "w")
            asset.write(str(rawData))
            return asset
        else:
            print('REQUEST_ERROR: '+str(REQUEST.status_code))
            return {'STATUS_CODE':REQUEST.status_code,'ERROR_MESSAGE':'REQUEST_ERROR: '+str(REQUEST.status_code)}
        ##endif
    ##end
##end
