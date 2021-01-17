from bs4 import BeautifulSoup
import requests

html_data = requests.get('https://www.exprtview.com/')

# create instance of BeautifulSoup

soup = BeautifulSoup(html_data.text,'html.parser')


# soup.title
# soup.head
# soup.head
# soup.find('div')  find all the div's present in the DOM

# el = soup.find(class_='navbar-default')  find html element based on class

# el = soup.find_all(class_='value')  if you have many element with same classes then this method returns a list
# el = soup.select('.item')  you can also select class like this (but this will return a list)

# el = soup.find(class_='description').get_text()   get only text data from  a html element
# el = soup.find(class_='description').find_parent()
# el = soup.find(class_='description').find_previous_sibling()  return the previous element
# el = soup.find(class_='description').find_next_sibling()


print(el)
