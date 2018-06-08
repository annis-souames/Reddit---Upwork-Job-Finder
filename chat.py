from fbchat import Client
from fbchat.models import *

 
data = json.loads(open("data.json","r").read())
usr_pass = data["pass"]
usr_email = data["email"]

def sendReddit(post_list):
	cl = Client(usr_email,usr_pass)
	if not cl.isLoggedIn():
		cl.login(usr_email,usr_pass)
	with open("reddit.txt","a+") as f_reddit:
		content = f_reddit.readlines()
		content = [x.strip() for x in content]
		print content
		
		for post in post_list:
			#Check if post has been sent yet or not
			if post["link"] not in content:
				msg_txt = "NEW JOB ON REDDIT : " + post["title"] + " - link : " + post["link"]
				msg = Message(text = msg_txt)
				message_id = cl.send(msg, thread_id=cl.uid, thread_type=ThreadType.USER)
				f_reddit.write(post["link"] + "\n")
				print "Job " + post["title"] + " Has been sent"
			else:
				continue
		


# Test data
test = [
	{"title" : "Python Job System", "link" : "http://reddit.com"},
	{"title" : "Python Job System 2", "link" : "http://reddit.com/hi"},
	{"title" : "Python Job System 3", "link" : "http://reddit.com/hi5"},
	{"title" : "Python Job System 4", "link" : "http://reddit.com/hi4"}


]
#sendReddit(test)





