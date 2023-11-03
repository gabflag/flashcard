from tkinter import *
import tkinter.messagebox
import measurements
from flashcardcontroller import card_controller

controller = card_controller.FlashCardController()

class Cardview:

    def __init__(self):

        self.screen = measurements.Measurements(0,0)
        self.root = Tk()
        self.root.title(self.screen.name)
        self.root.geometry(f"{self.screen.width}x{self.screen.height}+{self.screen.position_x}+{self.screen.position_y}")
        self.root.resizable(self.screen.resizable, self.screen.resizable)
        
        # LOGIN
        self.img_background_login = PhotoImage(file="view\\images\\login\\background_login.png")
        self.img_button_entry = PhotoImage(file="view\\images\\login\\button_entry.png")

        # SISTEMA
        self.img_background_card = PhotoImage(file="view\\images\\card\\background_card.png")
        self.img_button_rigth = PhotoImage(file="view\\images\\card\\button_rigth.png")
        self.img_button_wrong = PhotoImage(file="view\\images\\card\\button_wrong.png")
        self.img_button_answer = PhotoImage(file="view\\images\\card\\button_answer.png")

        # BACKGROUND
        self.lab_background = Label(self.root, image=self.img_background_login)
        self.lab_background.pack()

        self.bt_entry = Button(self.root, bd = 0, image=self.img_button_entry, command=self.vw_check_user)
        self.bt_entry.place(width=141.739, height=58.428, x=912.808, y=550.469)

        self.en_user_name = Entry(self.root,  bd = 0, font=("Calibri", 14), justify=LEFT, bg="white")      
        self.en_user_name.place(width= 293.347, height=41.611, x=832.293, y=295.216)

        self.en_password = Entry(self.root, show="*", bd = 0, font=("Calibri", 14), justify=LEFT, bg="white")      
        self.en_password.place(width= 293.347, height=41.611, x=832.497, y=385.802)

    def start(self):
        self.root.mainloop()

    def vw_check_user(self):    
        '''
        Function that checks the user's credentials in the database. If positive, 
        execute the program, otherwise, an error message will be displayed on 
        the screen.
        '''
        user = self.en_user_name.get()
        password = self.en_password.get()
        return_check_user = controller.cr_check_user(user, password)
        
        if return_check_user  == True:
            print("Opening sytem")
            self.open_system()
        else:
            self.en_user_name.delete('0', END)
            self.en_password.delete('0', END)
            tkinter.messagebox.showerror("ERRO", "With this credentials you can execute the system")
    
    def vw_login(self):
        '''
        Rebuilds the login screen and destroys restricted system functionality.
        '''
        self.bt_answer.destroy()
        self.bt_wrong.destroy()
        self.bt_right.destroy()
        self.menubar.destroy()
        self.txt_answer.destroy()
        self.txt_question.destroy()
        self.txt_results.destroy()
        self.lab_background.configure(image=self.img_background_login)    

        self.bt_entry = Button(self.root, bd = 0, image=self.img_button_entry, command=self.vw_check_user)
        self.bt_entry.place(width=141.739, height=58.428, x=912.808, y=550.469)

        self.en_user_name = Entry(self.root,  bd = 0, font=("Calibri", 14), justify=LEFT, bg="white")      
        self.en_user_name.place(width= 293.347, height=41.611, x=832.293, y=295.216)

        self.en_password = Entry(self.root, show="*", bd = 0, font=("Calibri", 14), justify=LEFT, bg="white")      
        self.en_password.place(width= 293.347, height=41.611, x=832.497, y=385.802)

    
    def open_system(self):
        '''
        Sends the execution signal to the system functionality screen. Refresh the screen with these features
        '''

        self.bt_entry.destroy()
        self.en_user_name.destroy()
        self.en_password.destroy()

        self.lab_background.configure(image=self.img_background_card)    

        self.bt_right = Button(self.root, bd = 0, image=self.img_button_rigth, command=self.vw_right)
        self.bt_right.place(width=117.568, height=53.496, x=965.142, y=646.108)

        self.bt_wrong = Button(self.root, bd = 0, image=self.img_button_wrong, command=self.vw_wrong)
        self.bt_wrong.place(width=117.568, height=53.496, x=283.291, y=646.108)
        
        self.bt_answer = Button(self.root, bd = 0, image=self.img_button_answer, command=self.vw_show_answer)
        self.bt_answer.place(width=134.104, height=50.189, x=615.948, y=336.856)

        # Dropdown Menu
        self.menubar = Menu(self.root)
        self.file_menu = Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.vw_add_card)
        self.file_menu.add_command(label="Edit", command=self.vw_edit_card)
        self.file_menu.add_command(label="Delete", command=self.vw_delete_card)
        self.file_menu.add_command(label="Exit", command=self.vw_login)

        self.menubar.add_cascade(label="Options", menu=self.file_menu)
        self.root.config(menu=self.menubar)

        self.txt_question = Text(self.root, bd=0, bg="white", font=("Calibri", 18))
        self.txt_question.tag_configure("center", justify='center')
        self.txt_question.place(width=826, height=136, x=269, y=176)
        
        self.txt_answer = Text(self.root, bd=0, bg="white", font=("Calibri", 18))
        self.txt_answer.tag_configure("center", justify='center')
        self.txt_answer.place(width=826, height=136, x=269, y=409)

        self.txt_results = Text(self.root, bd=0, bg="white", font=("Calibri", 14))
        self.txt_results.tag_configure("center", justify='center')
        self.txt_results.place(width=363, height=76, x=510, y=634)

        # Executes this block so that when the program starts, there are already questions available.
        self.exist_card = self.vw_exist_cards_to_see()
        if self.exist_card == FALSE:
            self.vw_not_cards()
        else:
            card_of_the_time = controller.cr_get_card()
            self.txt_question.delete('1.0', END)
            self.txt_question.insert(INSERT, str(card_of_the_time[1]))
            self.vw_show_number_cards_to_see()

    def vw_show_question(self):
        '''
        Updates the 'question' field with card information. The 'results' field is]
        also updated with the number of cards available for review
        '''

        self.vw_clean_fields()
        list_of_card = self.vw_exist_cards_to_see()
        if list_of_card == TRUE:
            card_of_the_time = controller.cr_get_card()
            self.txt_question.delete('1.0', END)
            self.txt_question.insert(INSERT, str(card_of_the_time[1]))
            self.vw_show_number_cards_to_see()
        else:
            self.vw_not_cards()

    def vw_show_answer(self):
        '''
        Updates the 'answer' field with card information.
        '''

        list_of_card = self.vw_exist_cards_to_see()
        if list_of_card == TRUE:  
            self.txt_answer.delete('1.0', END)
            self.txt_answer.insert(INSERT, str(controller.cr_show_answer()))
        else:
            self.vw_not_cards()
        
    def vw_right(self):
        '''
        Sends the signal to the controller that the user got the answer right.
        '''

        self.vw_clean_fields()
        list_of_card = self.vw_exist_cards_to_see()
        if list_of_card == TRUE:  
            controller.cr_right_update()
            self.vw_clean_fields()
            self.vw_show_question()
        else:
            self.vw_not_cards()
    
    def vw_wrong(self):  
        '''
        It sends the signal to the controller that the user made a mistake in the answer.
        '''

        self.vw_clean_fields
        list_of_card = self.vw_exist_cards_to_see()
        if list_of_card == TRUE:  
            controller.cr_wrong_update()
            self.vw_clean_fields()
            self.vw_show_question()
        else:
            self.vw_not_cards()

    def vw_exist_cards_to_see(self):
        '''
        Checks if there are cards to be reviewed today. Returns a boolean
        '''
        retorno = FALSE
        len_list = controller.cr_get_len_list_of_cards()

        if len_list > 0:
            retorno = TRUE
        else:
            retorno = FALSE
        return retorno

   # ************** MENU FUNCTIONS
    def vw_add_card(self):
        '''
        It takes the current data present in the 'question' and 'answer' 
        fields and sends it to the controller to create a new card.
        A success or failure message will be displayed
        '''

        try:
            question = str(self.txt_question.get("1.0", END))
            answer = str(self.txt_answer.get("1.0", END))

            if (len(question) > 1) and (len(answer) > 1):
                result = controller.cr_create_card(question, answer)
                self.vw_clean_fields()
                self.vw_show_message_box("NEW CARD", result)
                self.vw_show_question()   
            else:
                self.unfiled_fields("ADD CARD")
                self.vw_show_question() 

        except ValueError:
            self.vw_clean_fields()
            self.txt_results.delete('1.0', END)
            self.txt_results.insert(INSERT, "Erro in creat a new card", "center")

    def vw_edit_card(self):
        '''
        Sends the execution signal to the controller to update the card
        being displayed. It takes the current data present in the 'question'
        and 'answer' fields A success or failure message will be displayed.
        '''

        try:
            question = str(self.txt_question.get("1.0", END))
            answer = str(self.txt_answer.get("1.0", END))

            if (len(question) > 1) and (len(answer) > 1):
                result = controller.cr_update_card(question, answer)
                self.vw_show_message_box("UPDATE CARD", result)
                self.vw_show_question() 
            else:
                self.unfiled_fields("EDIT CARD")
                self.vw_show_question()

        except ValueError:
            self.txt_results.delete('1.0', END)
            self.txt_results.insert(INSERT, "Erro in update this card", "center")

    def vw_delete_card(self):
        '''
        Sends the execution signal to the controller to delete the card
        being displayed. A success or failure message will be displayed.
        '''

        try:
            self.vw_clean_fields()
            result = controller.cr_delete_card()
            self.vw_show_message_box("DELETED", result)
            self.vw_show_question()

        except ValueError:
            self.txt_results.delete('1.0', END)
            self.txt_results.insert(INSERT, "Erro in delete this card", "center")


    # ************** INFORMATIVES
    def vw_show_message_box(self, Title, message):
        '''
        Displays a generic message box to be used in different situations,
        receives the object itself, title and message as a parameter.
        '''

        current_x = self.root.winfo_x()
        current_y = self.root.winfo_y()

        top = Toplevel(self.root)
        top.title(Title)
        top.geometry(f"500x200+{current_x}+{current_y}")
        top.resizable(False, False)
        top.grab_set()
        top.focus_set()
        
        label = Label(top, text=message, font=("Helvetica", 14), borderwidth=0, justify="center")
        label.pack(fill="both", expand=True)
        
        self.root.wait_window(top)

    def vw_show_number_cards_to_see(self):
        '''
        Shows the number of cards left to see. Update message field in view
        '''
        number_cards = controller.cr_get_len_list_of_cards()
        self.txt_results.delete('1.0', END)
        self.txt_results.insert(INSERT, f"You have {number_cards} cards to review now :D", "center")

    def vw_not_cards(self):
        '''
        Updates the program's message box when it has no cards to review        
        '''
        self.txt_results.delete('1.0', END)
        self.txt_results.insert(INSERT, "Doens't exist card to review", "center")

    def vw_clean_fields(self):
        '''
        Clears all text fields used for outputting results
        '''
        self.txt_question.delete('1.0', END)
        self.txt_answer.delete('1.0', END)
        self.txt_results.delete('1.0', END)

    def unfiled_fields(self, erro_name):

        '''
        Displays a message box when the question and answer fields are not filled in,
        receives the object itself and title.
        '''       
        tkinter.messagebox.showerror(f"ERRO {erro_name}", "Both fields need to be filled!")

