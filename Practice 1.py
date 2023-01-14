
year_born = int(input("What year were you born?"))

def get_age(year_born):
    '''
    '''
    age = (2022 - year_born)
    age_old = (100 - age)
    years_left = (2022 + age_old)
    print("In year:", years_left, "you will be 100 years old!")
    return

get_age(year_born)
    
