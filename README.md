# Reddit---Upwork-Job-Finder
A powerful job finder for Reddit &amp; Upwork with texting capabilities

This simple project text you by Facebook Messenger whenever there is a new interesting job on Reddit or Upwork

**Example** : 

![Alt text](example.png "Title")

# Reddit:
There's a preselected list of subreddit to look for jobs, it takes 15 newest jobs in the subreddit that contains a word in your keyword list (see : Config part)

The subreddits are : 
- r/WorkOnline
- r/remotepython
- r/remotejs
- r/WFH

`Every time a new job is sent by messenger, the job link is added to reddit.txt file which serves as a simple database for previous sent jobs, this avoid sending the same job twice .`

**Tip:** You can add more to this list in the `main.py` file

*TODO* : Add keyword filtering with regex or NLTK

# Upwork
*Not Done*

It should get 15 newest jobs on each keyword with less than 5 applicants and text them to you on Messenger

Scraping Upwork should use Selenium and NLTK to extract best jobs based on keywords

# How to use

- Install python 2.7
- Clone this project
- Run `pip install -r requirements.txt` to install the dependencies
- Go to data.json and edit the list of keywords you want to include, each keyword should be between double quotes and keywords must be comma separated , like a JSON list
- The max parameter represent the number of jobs per keyword to look for in Upwork
- in email put your Facebook user email
- in pass put your facebook password, this is used by FbChat to send you a message

# Todo :

- Add upwork scraping
- Add smarter keyword filters for reddit using NLTK or Regex
- Use a scheduler to run this every hour
- Include other job hubs : Indeed, Craiglist...


# Disclaimer : 

This project is for personal use only, and should not be used to compete with Reddit or Upwork or for commercial uses.
