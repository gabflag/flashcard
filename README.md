<h1>FLASHCARD</h1>

# Technologies used:

  - Python 3.9.7 and its libraries TkInter, mysql.connector, calendar, datetime, random
  - MySQL Workbench
  - InkScape

# About the program:
  Flashcard is a memorization card software that employs spaced repetition technique to maximize information retention. Through an algorithm, the program calculates optimal review intervals for each card. In the project's main page, you'll find the script needed to create the database with test inserts. If desired, you can modify the script.

# Objectives:

  * Query, creation, update, and deletion of cards in the database;
  * Demonstrate how to integrate a database with a functional program;
  * Demonstrate how to create and use message boxes with TkInter;
  * Demonstrate the creation of a graphical interface and navigation between screens;
  * Implementation of a spaced repetition algorithm.

# How to use:

  - Run the 'main.py' file in the 'view' folder;
  - Log in using the user root:root OR admin:admin and click the 'ENTRY' button;
  - When the card screen opens, the current card will be displayed. You can click the 'ANSWER' button to reveal the answer, click the 'RIGHT' button if you know the answer, or 'WRONG' if you don't. Note that you can press the 'RIGHT' and 'WRONG' buttons even without displaying the answer with the 'ANSWER' button to expedite the review process;
  - If you have no cards to review, the dialog between the 'ANSWER' and 'WRONG' buttons will display the message 'Doesn't exist card to review';
  - If you have cards to review, the dialog between the 'ANSWER' and 'WRONG' buttons will display the message 'You have Y cards to review now :D';
  - To add a card, fill in the 'FRONT' fields with the front of the card and the 'ANSWER' field with the answer. After that, click the top-left 'Options' button and then click the 'new' option. A success message will be displayed;
  - To edit a card, when the desired card is displayed on the screen, edit the 'FRONT' fields with the front of the card and the 'ANSWER' field with the updated answer. After that, click the top-left 'Options' button and then click the 'Edit' option. A success message for the action will be displayed;
  - To delete a card, when the desired card is displayed on the screen, click the top-left 'Options' button and then click the 'Delete' option. A success message for the action will be displayed;
  - To exit the program, click the top-left 'Options' button and then click the 'Exit' option. You will be redirected to the login page.

# Areas for improvement:

  - Create a function for encrypting and decrypting data in the database (consider using sha256 or AES);
  - Specific program for testing.

# Relevant information:

  * Graphic arts were created in Inkscape
  * Install MySQL Workbench and configure the 'card_controller.py' file with your credentials;
  * Install and import the following libraries:

    - pip install mysql-connector-python
    - pip install tk

  * If you want to create an executable, I recommend working with a virtual environment. To create the executable:
    - pip install pyinstaller
    - pyinstaller --onefile -w main.py

# Developer's considerations:

  <p>The transition between screens was a challenge to overcome. Initially, the approach was to work with two objects: the login screen and the system screen. With this structure, the only seemingly viable solution was to destroy the login screen upon validating the data to open the system screen. While functional, this led to a somewhat uncomfortable delay in opening. The solution was to work with page updates, deleting and editing object attributes, making the transition smooth.</p>
  <p>Notably, I left a script named "data_base_inserts" for you to update the database for the period you are conducting tests. Simply modify the parameters when executing (check the last two lines of the file - obj.generate_sql_inserts_prior_today(1, 21): obj.generate_sql_inserts_after_today(21, 101)) and update your script with the new cards.</p>

# Observations:

  I consider this project interesting for those looking to solidify concepts and explore how simple it can be to create a CRUD application with Python and MySQL. The spaced repetition algorithm implemented here involves adding the difference between the card's creation date and the review date if the answer is correct. For incorrect answers, the card's creation date receives half the difference between the review date and creation date. If there are any logic errors in the code, spelling mistakes, or better ways to perform the tasks described, I appreciate your understanding and welcome suggestions for improvement.

# Images:
![tela_inicial](https://user-images.githubusercontent.com/95552879/219486776-f0f12e4a-d41b-4ee0-8eb5-1865ba8bd669.png)

![erro_credentials](https://user-images.githubusercontent.com/95552879/219486812-b309cb58-c410-4478-86fa-8f97a9cad545.png)

![tela_sistema](https://user-images.githubusercontent.com/95552879/219486842-7ae02a7c-556e-4a20-a19f-566d92f12c9e.png)

![edit_after](https://user-images.githubusercontent.com/95552879/219486908-5d801172-8a48-49d9-bdd9-2399a0a3ec36.png)

![erro_unfilled](https://user-images.githubusercontent.com/95552879/219486875-3a6b7469-a066-4755-84c0-8f2f7563950c.png)
