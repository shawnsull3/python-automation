#! /usr/bin/env python3
# lucky.py - Opens several Google search results for a specific search term
import requests, sys, webbrowser, bs4

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
print('Googling...') # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]), headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

links = soup.select('div .g > div > div > a')

numOpen = min(3, len(links))
for i in range(numOpen):
    print(links[i]['href'])
    webbrowser.open(links[i].get('href'))