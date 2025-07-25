from newsapi import NewsApiClient
import requests
import random
import json

def fetch_news(category):
	try:
		r = requests.get(f"https://newsapi.org/v2/everything?q={category}&language=en&apiKey=d70b4ef7d25143daaef85faa81ad5eb0")
	except:
		print("Check internet connection.")
		return False
		
	news = json.loads(r.text)
	articles = news['articles']
	titles = [article['title'] for article in articles]
	return random.choice(titles)

try:
	api_key_file = open('NewsAPIkey.txt', 'r')
except:
	print("API key not found with 'NewsAPIkey.txt' file.")
	exit()
api_key = api_key_file.read()
newsapi = NewsApiClient(api_key=api_key)

newstype = ['sports', 'business', 'health', 'youtube', 'technology']
interest = [0.1/len(newstype) for _ in newstype]
likes = {category: 0 for category in newstype}
is_liked = False
fetched_news = ""
current_category = None
starter = True
user_input = 'n'

print("'n' to next\n'l' to like or dislike\n'exit' to exit")

while True:
	if not starter:
		user_input = input("-> ").lower()
	starter = False
	if user_input == 'exit':
		print("Have a good day!")
		exit()
	elif user_input == 'n':
		is_liked = False
		current_category = random.choices(newstype, weights=interest, k=1)[0]
		fetched_news = fetch_news(current_category)
		if fetched_news:
			print('\n', fetched_news)
	elif user_input == 'l':
		if fetched_news is False:
			print("Check internet connection")
			continue
		if not is_liked:
			likes[current_category] += 1
			interest[newstype.index(current_category)] += 1/len(interest)
			interest = [round(num, 2) for num in interest]
			is_liked = True
			print("Liked successfully")
			if likes[current_category] >= 5:
				print(f"You are most interested in {current_category} news.")
		else:
			likes[current_category] -= 1
			interest[newstype.index(current_category)] -= 1/len(interest)
			interest = [round(num, 2) for num in interest]
			is_liked = False
			print("Like removed")
	else:
		continue
		