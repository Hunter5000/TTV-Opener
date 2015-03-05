import easygui as eg
import webbrowser
import os

def openChat(url, chat, quality):
	check1 = url.find("http")
	qual = " source"
	if quality.find("au") != -1:
		qual = " audio"
	if quality.find("hi") != -1:
		qual = " high"
	if quality.find("lo") != -1:
		qual = " low"
	if quality.find("me") != -1:
		qual = " medium"
	if quality.find("mo") != -1 or quality.find("wo") != -1:
		qual = " mobile"
	ch = False
	if chat.find("y") != -1:
		ch = True
	if check1 != -1:
		newurl = (url + "/chat")
		if ch == True:
			webbrowser.open_new(newurl)
		os.system("livestreamer " + newurl + qual)
		return "Stream closed"	
	check2 = url.find("twitch.tv")
	if check2 != -1:
		newurl = ("http://" + url + "/chat")
		if ch == True:
			webbrowser.open_new(newurl)
		os.system("livestreamer " + newurl + qual)
		return "Stream closed"
	if check1 == -1 and check2 == -1:
		newurl = ("http://twitch.tv/" + url + "/chat")
		if ch == True:
			webbrowser.open_new(newurl)
		os.system("livestreamer " + newurl + qual)
		return "Stream closed"		
	return "Error"

while 1:
    msg = "Open the given stream using Livestreamer and its chat in a new browser tab"
    title = "TTV Opener"
    fieldNames = ["Stream", "Chat (y/n)", "Quality"]
    fieldValues = []
    fieldValues = eg.multenterbox(msg,title, fieldNames)

    message = openChat(fieldValues[0],fieldValues[1], fieldValues[2])

    eg.msgbox(message)

    msg = "Open new stream?"
    title = "Choose action"
    if eg.ccbox(msg, title):
        pass  # user chose Continue
    else:
        sys.exit(0)
