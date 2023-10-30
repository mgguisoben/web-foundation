import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
archive = response.text

soup = BeautifulSoup(archive, "html.parser")

movie_titles = soup.find_all(name="h3", class_="title")
movie_titles = [title.getText() for title in movie_titles]

with open("100 Movies to Watch.text", "w", encoding="UTF-8") as file:
    file.write("\n".join(title for title in movie_titles[::-1]))

print("Done!")
