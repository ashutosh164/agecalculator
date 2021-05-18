import datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def age(self):
        today = datetime.date(2021, 5, 18)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_day = (today - dob).days
        age_in_year = age_in_day / 365
        return int(age_in_year)


user = User('ashu', '19970416')
print('Hello', user.name, 'You are ', user.age(),'years old !')


