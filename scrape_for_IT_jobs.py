import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/jobs')
res2 = requests.get('https://news.ycombinator.com/jobs?next=28923699')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titlelink')
athing = soup.select('.athing')
links2 = soup2.select('.titlelink')
athing2 = soup2.select('.athing')

mega_links = links + links2
mega_athing = athing + athing2

def create_custom_hn(links, athing):
  hn = []
  job = input("Search for a job: ")
  for idx, item in enumerate(links):
    title = item.getText().lower()
    href = item.get('href', None)
    if job.lower() in title:
      hn.append({'title': title, 'link': href})
  if len(hn) == 0:
    print("No jobs found. :(")
  return hn
 
print(create_custom_hn(mega_links, mega_athing))
