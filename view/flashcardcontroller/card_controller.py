from .model import script_db_card
from datetime import date, timedelta
import random

database = script_db_card.Database('localhost', 'dbcardcrud', '-', '-')

class FlashCardController:

    def __init__(self):

        self.card = []

    def cr_check_user(self, user_name, key_pass):
        '''
        Check the user's credentials against the database
        '''

        result_query = database.check_credencials_user_in_database(user_name, key_pass)
        if len(result_query) > 0:
            return True
        else:
            return False
    
    def cr_get_len_list_of_cards(self):
        '''
        Returns the number (int) of cards available for review today
        '''
        result_query = database.get_all_card_before_today()
        return len(list(result_query))

    def cr_get_card(self):
        '''
        Returns a list with card information to be used. The card that is returned is random
        '''
        result_query = database.get_all_card_before_today()
        len_list = len(result_query)

        if len_list > 0:
            random_card = random.randrange(0, len_list)
            result_query_in_list = list(result_query[random_card])
            self.card = result_query_in_list
            return result_query_in_list

    def cr_show_answer(self):
        '''
        Returns the answer that is in position two of the turn card list.
        '''
        return (self.card[2])

    def cr_right_update(self):
        '''
        Update datecheck in database when the answer is right. No return
        '''
        card_of_the_time = self.card
        date_for_card_update = (date.today() + (date.today() - card_of_the_time[4])) + timedelta(1)
        database.update_card_datecheck_by_id(int(card_of_the_time[0]), date_for_card_update)
    
    def cr_wrong_update(self):
        '''
        Update datecheck in database when the answer is wrong.
        '''
        card_of_the_time = self.card
        date_for_card_update = date.today() - ((date.today() - card_of_the_time[4])/2)

        if date_for_card_update > date.today():
            # Sucessul update - date is still less than today
            database.update_card_createdate_by_id(int(card_of_the_time[0]), date_for_card_update)
            
        if date_for_card_update < date.today():
            # Sucessul update - date would be greater than today
            database.update_card_createdate_by_id(int(card_of_the_time[0]), date.today())
        
        # IF THE SAME AS TODAY DOES NOTHING
    
    # ************************** MENU
    def cr_create_card(self, question, answer):  
        '''
        Checks if it is possible add a card to the database. Returns a String
        '''
        database.create_card(question, answer)
        return "Card was successfully created! Now it's on your study list,\nClick the X button to continue your studies."


    def cr_update_card(self, question, answer):
        '''
        Checks if it is possible to update the card in the database. Returns a String
        '''
        database.update_card_by_id(int(self.card[0]), question, answer)
        return "Card has been updated successfully!\nClick the X button to continue your studies."

    def cr_delete_card(self):
        '''
        Calls the function to delete a card from the database. Returns a String 
        '''
        database.delete_by_id(int(self.card[0]))
        return "Card has been deleted successfully!"
    
