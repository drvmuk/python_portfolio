# -*- coding: utf-8 -*-
"""
Created on Sat May  1 10:57:22 2021

@author: Dhruv
"""

'''Documentation of Beautifulsoup:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

HTML = HyperText Markup language
XML = Extensible Markup Language
'''

# Import libraries

from bs4 import BeautifulSoup

with open("resources/website.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
# Get title tag
print(soup.title)
print(soup.title.string) # Shows the actual string in title tag

# Prettified version of the HTML code
print(soup.prettify())

# Get first instance of tags
print(soup.a)
print(soup.p)
print(soup.li)

# Find all tags
print(soup.find_all(name='a'))
print(soup.find_all(name='p'))
print(soup.find_all(name='li'))

# Get only text of the anchor tags
all_anchor_tags = soup.find_all(name='a')

for a in all_anchor_tags:
    print(a.getText())
    
## get href
for a in all_anchor_tags:
    print(a.get('href'))

# Filter by id
heading = soup.find(name = 'h1', id = 'name')
print(heading)

# Filter by class
heading = soup.find(name = 'h3', class_ = 'heading')
print(heading)

# Navigate use drilldown selector /  css selector
company_url = soup.select_one(selector = "p a")
print(company_url)

## Select ID
name = soup.select_one(selector='#name')
print(name)

## Select Class
heading = soup.select('.heading')
print(heading)

# Get attributes
data = '''
<form method="get" action="/search/">
 <input type="text" name="q" maxlength="255" value=""></input>
</form> 
'''

soup = BeautifulSoup(data, 'html.parser')

form_tag = soup.find('input')
print(form_tag.get('maxlength'))

# Scraping live website























    
