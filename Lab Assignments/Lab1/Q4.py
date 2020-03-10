from bs4 import BeautifulSoup
import requests

url = "https://catalog.umkc.edu/course-offerings/graduate/comp-sci/"
# Getting the webpage, creating a Response object.
response = requests.get(url)
text = response.text
soup = BeautifulSoup(text, "html.parser")  # parsing HTML content
print(soup.title.get_text() + '\n')   # fetching title
# print(text)
title_list = soup.findAll('span', {'class': "title"})   # checking for all course title
overview_list = soup.findAll('p', {'class': "courseblockdesc"})   # checking for all course overview
for i in range(len(title_list)):
    if title_list[i] != " " and overview_list[i] != " ":  # checking for null values
        print("Course title: ", title_list[i].get_text())
        print("Course overView: ", overview_list[i].get_text())
    print('\n')