from bs4 import BeautifulSoup

# opens a file and saves it as a variable
with open('home.html', 'r') as html_file:
    #grabs the text of the file
    content = html_file.read()
    
    # we are scraping content using the parser method lxml,
    # not using default html parser because that does not work broken html 
    soup = BeautifulSoup(content, 'lxml')
    
    # find function returns the first occurrence and stops looking for additional occurrences
    # find_all returns a list of all occurrences and the whole line is returned
    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)

    # collects all occurrences of div that has its class equal to 'card'
    # h5 holds the course name while the a tag is the button that holds the price
    # the button tag gets split so that we can extract the price from it
    course_cards = soup.find_all('div', class_='card') 
    for c in course_cards:
        course_name = c.h5.text
        course_price = c.a.text.split()[-1]

        print(f'{course_name} {course_price}')