from bs4 import BeautifulSoup as BS
import mechanize

url = "https://imgur.com/signin?minimal"

browser = mechanize.Browser()
print browser.open(url)

browser.select_form(nr = 0)
browser.form['username'] = "thisisnotarobot"
browser.form['password'] = "lickmybattery"
browser.submit()

for link in browser.links():\
  print link
