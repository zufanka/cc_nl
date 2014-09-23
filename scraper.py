from bs4 import BeautifulSoup as BS
import mechanize

url = "http://sijeme.sk/wp-login.php"

def login(url):
  browser = mechanize.Browser()
  browser.open(url)
  
  print [form for form in browser.forms()][0]
  
  browser.select_form(nr = 0)
  browser.form['TextControl'] = "thisisnotarobot"
  browser.form['PasswordControl'] = "lickmybattery"
  
  browser.submit()

  for link in browser.links():
    print link
    
login(url)

#from jabbapylib.filesystem import fs
#USERNAME = fs.read_first_line('/home/jabba/secret/project_euler/username.txt')
#PASSWORD = fs.read_first_line('/home/jabba/secret/project_euler/password.txt')
