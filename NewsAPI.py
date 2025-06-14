from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='d70b4ef7d25143daaef85faa81ad5eb0')

newstype = ["sports", "technology", "science", "health", "business", "general", "entertainment"]

print("Welcome to My News Program.")

while True:
	print("\nWhat news you want:")
	for news in newstype:
		print(news.capitalize())
	print("or 'quit'")

	choice = input("--> ").lower()
	if choice == 'quit':
		print("Thanks for using our program.")
		break
	elif choice in newstype:
		try:
			non = int(input("How many articles to fetch: "))
			if non <= 0:
				print("Invalid input, enter positive number.")
				continue
		except ValueError:
			print("Invalid input, not a number.")
			continue
		top_headlines = newsapi.get_top_headlines(category=choice,
		language='en')
		for index, article in enumerate(top_headlines['articles']):
			if index >= non:
				break
			print(f"{index+1}. {article['title']}")
	else:
		print("Invalid input, try again.")