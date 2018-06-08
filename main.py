from selenium import webdriver
import json
import praw
import fbchat
from chat import *
import pdb 

CLIENT_ID = ""
SECRET = ""

def get_data():
	data = json.loads(open("data.json","r").read())
	return data
def generate_url(key):
	return "https://www.upwork.com/o/jobs/browse/?q=" + key

def checkRedditJobs(red,keywords):
	subs = ["WorkOnline","remotepython","remotejs","hiring","WFH"]
	jobs_list = []
	full_list = []
	pdb.set_trace()
	for s in subs:
		#Get 15 recent jobs
		sub = red.subreddit(s)

		#Jobs is a temp local list for jobs in each sub
		jobs = []
		for post in sub.new(limit = 15):
			jobs.append(post) 
		jobs_list = jobs_list + jobs
	for post in jobs_list:
		print post.title
		full_list.append({"title" : post.title, "link": post.shortlink})
	print full_list
	return full_list




def run():
	#Run this everyday
	#Go to upwork
	#wd = webdriver.Firefox()
	data = get_data()
	reddit = praw.Reddit(client_id = CLIENT_ID,client_secret = SECRET, user_agent = "Reddigest by Hugeburger")
	jobs = {}
	"""
	for word in data["keywords"]:
		#url = generate_url(word)
		#wd.get(url)
		
		#jobs["upwork"].append(getUpworkJobs(word))
	"""
	jobs["reddit"] = checkRedditJobs(reddit,data["keywords"])
	if len(jobs["reddit"]) > 0:
		sendReddit(jobs["reddit"])
	


run()
