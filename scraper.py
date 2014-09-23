from bs4 import BeautifulSoup as BS
import mechanize

browser = mechanize.Browser()
browser.open()
browser.select_form(nr = 0)
browser.form['username'] = USERNAME
browser.form['password'] = PASSWORD
browser.submit()
