# standard modules
import re
from datetime import datetime
from urllib import parse, request, error

# community modules
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup


# Generate a csv of code title and numeric order
# page = request.urlopen('https://www.portlandoregon.gov/citycode/37436').read()
# soup = BeautifulSoup(page, features="html.parser")
# titles = {
#     'subject_index': [],
#     'subject_index_url': [],
# }

# # #Scrape the website to get the titles from the provided link
# for title in soup.find_all('h2')[1:]:
#     url = title.find('a')['href'] #collects the url from all the h2's after the first 3 because they are not part of city code
#     titles['subject_index_url'].append(url) #collects the url of the titles
#     titles['subject_index'].append(title.text) #collects the name of titles
#     print('{} of {} loaded'.format(len(titles['subject_index']), len(soup.find_all('h2')[1:])))
# print(titles)

# #Saves Titles dictionary list to csv
# policy_subject = pd.DataFrame(titles)
# policy_subject.to_csv('city_policy_subjects.csv', index=False)

# section_data = pd.read_csv('city_policy_subjects.csv')

# categories = {
#     'lvl 2 category': [],
#     'lvl 2  code': [],
#     'lvl 3 category': []
# }

# index = 0

# for x in section_data['subject_index_url']:
#     # print('https://www.portlandoregon.gov/{}'.format(x))
#     try:
#         page = request.urlopen('https://www.portlandoregon.gov/{}'.format(x))
#         soup = BeautifulSoup(page, features="html.parser")
#         index += 1
#     except error.HTTPError:
#         index += 1
#         continue
#     for y in soup.find('a'):
#         cate = re.findall(r'\w*[A-Z]\w*[A-Z]\w*[A-Z]\w*', y)
#         print(cate[0])
        # if cate:
        #     print(cate)
            # categories['lvl 2 category'].append(section_data['subject_index'][index-1])
            # categories['lvl 2 code']
            # categories['level 3 category'].append(y.text)
        # else:
        #     pass
    # print('{} loaded'.format(x))

# #Saves Titles dictionary list to csv
# policy_section = pd.DataFrame(sections)
# policy_section.to_csv('city_policy_sections.csv', index=False)

# data = pd.read_csv('city_policy_sections.csv')
# categories = {
#     'lvl2': [],
#     'lvl3code': [],
#     'lvl3cate': []
# }

# for row in range(len(data['name'])):
#     cate = re.findall(r'\w*[A-Z]\w*[A-Z]\w*[A-Z]\w*', str(data['name'][row]))
#     if cate:
#         print(cate[0])
#         categories['lvl3code'].append(cate[0])
#         categories['lvl2'].append(data['subject'][row])
#         categories['lvl3cate'].append(data['name'][row])
#     else:
#         categories['lvl3code'].append(' ')
#         categories['lvl2'].append(data['subject'][row])
#         categories['lvl3cate'].append(data['name'][row])

# policy_section = pd.DataFrame(categories)
# policy_section.to_csv('city_policy_categories.csv', index=False)

page = request.urlopen('https://www.portlandoregon.gov/citycode/26819').read()
soup = BeautifulSoup(page, features="html.parser")

sub_categories = {
    'lvl3code': [],
    'lvl2': [],
    'lvl3cate': []
}

data = soup.findAll('div',attrs={'id':'main-content'})

for title in data:
    links = title.findAll('a')
    cate = re.findall(r'\w*[A-Z]\w*[A-Z]\w*[A-Z]\w*', title.text)
    for a in links:
        if cate:
            sub_categories['lvl3code'].append(cate[0]) 
            sub_categories['lvl2'].append('Administrative Services') 
            sub_categories['lvl3cate'].append(a.text) 
            print('{} of {} loaded'.format(len(sub_categories['lvl2']), len(soup.find_all('h2')[1:])))
        else:
            pass
print(sub_categories)

#Saves Titles dictionary list to csv
policy_subject = pd.DataFrame(sub_categories)
policy_subject.to_csv('city_policy_subcategories.csv', index=False)

    

# print(len(sections['id']))
# print(len(sections['chapter']))
# print(len(sections['number']))
# print(len(sections['title']))
# print(len(sections['url']))
# print(len(sections['text']))