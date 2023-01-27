import urllib.request
import bs4 as bs 

def get_html_soup(url:str) -> bs.BeautifulSoup:
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = bs.BeautifulSoup(html, "html.parser")
    return soup

def get_title_words(html:bs.BeautifulSoup) -> str:
    title = html.title.string
    return title.split("|")[0].split()

def get_course_code(title:list) -> str:
    return title[0].lower() + title[1]

def get_course_credits(title:list) -> int:
    return int(title[-2].strip("("))

def get_course_name(title:list) ->str:
    return " ".join(title[2:-2])

def get_terms(html:bs.BeautifulSoup) -> list:
    string = str(html.find_all("p",class_="catalog-terms")[0])
    string = string.removeprefix("<p class=\"catalog-terms\">")
    string = string.removesuffix("</p>")
    string = string.strip()
    string = string.removeprefix("Terms:")
    return string.strip().split(",")

if __name__ == "__main__":
    course = get_html_soup("https://www.mcgill.ca/study/2022-2023/courses/math-240")
    title = get_title_words(course)
    print(get_course_code(title))
    print(get_course_credits(title))
    print(get_course_name(title))
    print(get_terms(course))
    pass
