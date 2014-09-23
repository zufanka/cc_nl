from bs4 import BeautifulSoup as BS
import mechanize

url = "https://imgur.com/signin?minimal"

browser = mechanize.Browser()
browser.open(url)
for form in browser.forms():
  if form.attrs['id'] == 'login':
    browser.form = form
    break
# browser.select_form(id = "login")
print browser.form
browser.form['username'] = "thisisnotarobot"
browser.form['password'] = "lickmybattery"
browser.submit()

for link in browser.links():\
  print link
