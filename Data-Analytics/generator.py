# This is a Python script to generate random people's information in order to perform investigative data analysis
# using different database software. The purpose of these data is to mimic people who crossed the border to come 
# to Canada during the early 20th century; their data can be found at:  https://www.ancestrylibrary.ca/search/categories/40/


import names
import datetime
from datetime import timedelta
import random


# preprocess birthday, constrained to people born after 1840 before 1930 (simulating the year 1930)
start_date = datetime.date(1840, 1, 1)
end_date   = datetime.date(1929, 12, 31)
information = []

def decision(probability):
    return random.random() < probability

def create_list(filename): # a function to extract line in a txt file into a python list. 
    my_list = []
    my_file = open(filename, "r")
    tempData = my_file.read()
    my_list = tempData.split("\n")
    my_file.close()
    return my_list


citizenships = create_list("citizenship.txt") # cr: https://en.wikipedia.org/wiki/List_of_sovereign_states_in_the_1930s
ethinicities = create_list("ethnicity.txt") # cr: https://github.com/cgio/global-ethnicities/blob/master/sources_local/census.txt
cities = create_list("city.txt") # cr: https://github.com/datasets/world-cities/blob/master/data/world-cities.csv
languages = create_list("language.txt") # cr: https://github.com/MarQuisKnox/World-Languages/blob/master/plain-text/languages.txt
destinations = create_list("Canadian-cities.txt") # cr: https://gist.github.com/philcampbell-qhr/48e0e17739536b25ebf7d5e22c117ae1

def generateInformation(k):
    for i in range(k):
        csv_line = ""

        name = names.get_full_name() # name
        num_days = (end_date - start_date).days 
        rand_days = random.randint(1, num_days)
        birthday = start_date + datetime.timedelta(days=rand_days) # birthday
        citizenship = random.choice(citizenships) # citizenship
        ethnicity = random.choice(ethinicities)   # ethnicity
        birthplace = random.choice(cities) # birthplace 
        In_Canada_Before = str(decision(0.8)) # boolean value of if in Canada before 
        language = random.choice(languages) # language 
        destination = random.choice(destinations) # destination in Canada
        relative_in_Canada = str(decision(0.2)) # if this person have relative in Canada
        family_size = random.randrange(1, 10)
        money = random.randrange(0, 1000) # money the person carries
        admission = ""
        if (money > 50): # chance of admission soley determined by money
            admission = str(decision(0.85))
        else:
            admission = str(decision(0.15))



        csv_line += name + "," + str(birthday)  + "," + citizenship + "," + ethnicity + ","  +  birthplace  \
        + "," + In_Canada_Before + "," + language + "," + destination + "," + str(family_size) + "," + relative_in_Canada \
        + "," + str(money) + "," + admission
        
        
        information.append(csv_line)
        # print(csv_line)

def write_to_csv(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            f.write("\n")
        f.close()



if __name__ == "__main__":
    generateInformation(1000)
    write_to_csv("people.txt", information)
