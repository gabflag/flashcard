import random
from datetime import date
import calendar

class Card_insert:
    
    def __init__(self):
        self.today = date.today()
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.last_feb_day = 28

        # Correction in the month of February if the year is a leap year
        if calendar.isleap(self.year):
            self.last_feb_day = 29
        
        self.days_in_month = {
            1: 31,
            2: self.last_feb_day,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

    def generate_sql_inserts_prior_today(self, number_cards_began, number_cards_end):
        '''
        Receives an integer indicating the number of insert'a you want to create with dates prior to today.
        '''

        for i in range(number_cards_began, number_cards_end):
            random_month = random.randint(1, self.month)

            if random_month == self.month:
                random_day = random.randint(1, self.day)
            else:
                random_day = random.randint(1, self.days_in_month[self.month])
                
            if random_month >= 10:
                insert = (f"INSERT INTO card (question, answer, datecheck, createdate)" \
                        f"VALUES ('Question contained in the {i}° card', 'Answer to the {i}° card', '2023/{random_month}/{random_day}', '2023/{random_month}/{random_day}');")
            else:
                insert = (f"INSERT INTO card (question, answer, datecheck, createdate)" \
                        f"VALUES ('Question contained in the {i}° card', 'Answer to the {i}° card', '2023/0{random_month}/{random_day}', '2023/0{random_month}/{random_day}');")
            
            print(insert)

    def generate_sql_inserts_after_today(self, number_cards_began, number_cards_end):
        '''
        Receives an integer indicating the number of insert'a if you want to create with a date after today.
        '''

        for i in range(number_cards_began, number_cards_end):
            random_month = random.randint(self.month, 12)

            if random_month == self.month:
                if self.day+1 <= self.days_in_month[self.month]:
                    random_day = random.randint(self.day+1, self.days_in_month[self.month])
                else:
                    random_day = 1
                    if  random_month < 12:
                        random_month += 1
                    else:
                        random_month = 1
                        self.year += 1
            else:
                random_day = random.randint(1, self.days_in_month[self.month])
            
            if random_month >= 10:
                insert = (f"INSERT INTO card (question, answer, datecheck, createdate)" \
                        f"VALUES ('Question contained in the {i}° card', 'Answer to the {i}° card', '{self.year}/{random_month}/{random_day}', '{self.year}/{random_month}/{random_day}');")
            else:
                insert = (f"INSERT INTO card (question, answer, datecheck, createdate)" \
                        f"VALUES ('Question contained in the {i}° card', 'Answer to the {i}° card', '{self.year}/0{random_month}/{random_day}', '{self.year}/0{random_month}/{random_day}');")
                
            print(insert)

obj = Card_insert()
obj.generate_sql_inserts_prior_today(1, 21)
obj.generate_sql_inserts_after_today(21, 101)

