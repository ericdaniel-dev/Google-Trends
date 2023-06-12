import requests
import json
from datetime import date

class Trends:
	def __init__(self):
		self.todaysDate = date.today()
		self.API = "https://trends.google.co.id/trends/api/dailytrends?hl=in&tz=-420&geo=ID&ns=15"
	
	def todayTrends(self):
		print(f"Getting Todays Google Trends Keyword, date:{self.todaysDate}")
		date = str(self.todaysDate).replace("-", "")
		req = requests.get(self.API+"&ed="+date, allow_redirects=False)
		self.response = str(req.text).replace(")]}',", "")
		data = self.parseJson()
		print(f" These are the most trending keywords in Indonesia today ({self.todaysDate})")
		for i in data:
			print(f"-> {i}")
		prompt = input("Want me to save these data for you? [Y/N]")
		if prompt!="N":
			fname = "Keyowords"+str(self.todaysDate)+".txt"
			for i in data:
				with open(fname, "a") as savedata:
					savedata.write(str(i)+"\n")

	def parseJson(self):
		parsingJson = json.loads(self.response)
		keywords = []
		for i in parsingJson['default']['trendingSearchesDays']:
			for j in i['trendingSearches']:
				keys = j['title']['query']
				keywords.append(keys)
		return keywords

if __name__ == "__main__":
	GoogleTrends = Trends()
	GoogleTrends.todayTrends()