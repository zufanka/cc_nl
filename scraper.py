from bs4 import BeautifulSoup as BS
import mechanize

url = "https://imgur.com/signin?minimal"

browser = mechanize.Browser()
browser.open()
browser.select_form(nr = 0)
browser.form['username'] = thisisnotarobot
browser.form['password'] = Lickmybattery
browser.submit()
