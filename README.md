# Horoscope Calculator
Welcome to the Horoscope Calculator! 
The Horoscope Calculator is a simple Python program that allows users to get their horoscope predictions based on their birthdate and star sign. The program provides horoscope readings for each zodiac sign.
Whether you're seeking guidance, curious about what the stars have in store for you, or just want to explore the mystical realm of astrology, the Horoscope Calculator has you covered.

[The live link for the website can be found here](https://horoscope-calculator-42ae9e82fc7b.herokuapp.com/)

![Horoscope enter name](/assets/images/screenshots/am_i_responsive.png)


## Features
### Exisiting Features
- Enter your name
   - Start by providing your name when prompted.
   - This allows the Horoscope Calculator to create a personalized connection with you, ensuring that your horoscope readings are not only accurate but also resonate with your individuality.

![Horoscope enter name](/assets/images/screenshots/entername.png)

- Discover your star sign:
  - Input your birthdate (month and day), and let the program calculate your precise zodiac sign.
  - With this information, the Horoscope Calculator can delve into the specific characteristics, traits, and tendencies associated with your sign, uncovering profound insights about your personality and life journey.

![Horoscope input birthday and welcome message](/assets/images/screenshots/welcomemessage.png)

- The calculator will then determine your star sign based on the month and the day that you input and will progress into asking whether you would like to know your horoscope or not.

![calculating the star sign](/assets/images/screenshots/star_sign.png)
      
- Flexible Forecast Options
    - Choose between today's horoscope or get a sneak peek into what tomorrow holds.
    - This flexibility allows you to plan ahead and make informed decisions based on astrological insights

![Horoscope ask today or tomorrow](/assets/images/screenshots/todayortomorrow.png)

- Motivational Horoscope revealed
    - At the end of the interactive questionnaire, the horoscope calculator reveals your personalized horoscope, adding an exciting touch to the user experience.
    - Whether you seek encouragement, guidance, or simply enjoy reading about astrology, the personalized horoscope feature adds an extra dimension of engagement to the horoscope calculator.
 
![Horoscope](/assets/images/screenshots/horoscopeprediction.png)
 
- The calculator gives the user the option to read another star sign at the end.
- It also does not give you the opportunity to input a false birthday or zodiac sign - this is so you don't get a miscalculated horoscope! 

![invalid month message](/assets/images/screenshots/invalidresponse.png)


## Data Model
- In my horoscope calculator, I have several elements that make up the data model. First, there is a dictionary called HOROSCOPES, where I describe two different horoscopes for each zodiac sign (today and tomorrow). I also have DAYS_OF_MONTHS which helps me validate the number of days in each month. It ensures that the user enters a valid day for their birthdate.
- Next, I have a list called star_signs that contains tuples representing the different star signs and their corresponding date ranges. This list allows me to determine the user's star sign based on their birthdate.
- I store the user's name in a variable called name. It's a string that the user enters when they start using the calculator. This helps me personalize their horoscope experience.
- For collecting the user's birthdate, I use the variables month_input and day_input. These variables hold the user's input for the month and day of their birth, respectively. I validate these inputs and convert them to integers if needed.
- To calculate the day of the year corresponding to the user's birthdate, I use the variable day_of_year. It represents the sum of the days of each month leading up to the user's birth month, plus the day of their birth.
- The variable star_sign is a string that represents the user's star sign based on their birthdate. I determine this by checking the date range for each star sign in the star_signs list.
- When asking the user if they want to know their horoscope, their response is stored in the variable response. It's a string that the user enters to indicate their preference.
- To accommodate the user's choice of the day (today or tomorrow) for which they want to know their horoscope, I have the variable horoscope_day. It's a string that represents their selection.
- Once I have the user's inputs, I retrieve the horoscope prediction for the given star sign and day. I store this prediction in the variable prediction, which is a string.
- Overall, this data model encompasses the variables and structures I use to collect user input, validate dates, calculate star signs, and display horoscope predictions. It allows me to provide a personalized and accurate horoscope experience for each user.


## Testing
I have manually tested this project by doing the following:
   - Passed the code through a PEP8 linter and confirmed there are no problems.
   - Manually given invalid inputs to see what the outcome is.
   - Manually given valid inputs to see what the outcome is.


### Bugs
#### Solved Bugs
I encountered a few bugs while working on the horoscope calculator code, but I was able to fix them.
- One bug was related to validating the user's birth month. Previously, the code only checked if the month input was an integer, but it came up with in invalid response when the user entered the month as a name. To fix this, I added a check for month names in a list and converted them to the corresponding integer value. This ensured that both numeric and name inputs for the month were accepted.

![Int solved bug](/assets/images/screenshots/Solved_bug_int.png)

- I addressed the issue of the long line of code by using double quotes ("") to break the line into multiple lines for improved readability. Instead of having a single long line, I split it into smaller segments, each enclosed within double quotes. This allows the code to span across multiple lines while maintaining the string's integrity. By doing so, I made the code more organized and easier to understand.

![long line code](/assets/images/screenshots/long_line_string.png)
  
- I made the horoscope calculator clearer by adding a function called clear_screen(). This function uses a module called subprocess to clear the previous questions from the screen. By importing the subprocess module, I was able to access its features.
     - Inside the clear_screen() function, I used the subprocess.run() method to run a system command that clears the screen. The specific command I used depends on the operating system. For example, on non-Windows systems, the command is "clear", and on Windows systems, it is "cls".
     - Whenever I call the clear_screen() function, it executes the system command and clears the screen, making the calculator interface cleaner and easier to read. This way, the previous questions are hidden, and the user can focus on entering new inputs without any distractions.

![clear function](/assets/images/screenshots/def_clear_fuction.png)

- I encountered a bug where entering an invalid date would still provide a star sign, even though the date was not valid. To fix this issue, I made modifications to the get_star_sign() function.
     - First, I added a validation check using the is_valid_date() function. This check ensures that the entered date is valid before proceeding with determining the star sign. If the date is not valid, the function returns an "Invalid date" message instead of a star sign.
     - By incorporating the validation step, I ensured that only valid dates are considered for determining the star sign. This fix prevents the calculator from providing a star sign based on invalid or incorrect dates, improving the accuracy and reliability of the horoscope predictions.
 
 ![valid date](/assets/images/screenshots/valid_date.png)      

### Validator Testing
- PEP8
  - No errors were returned form PEP8online.com

### Unfixed Bugs
No unfixed bugs

## Deployment
This project was deployed on Heruko, Code Institute's mock terminal.
- Deployment steps
     - Cone the respository from github pages.
     - Create a new Heroku app
     - Set the buildbacks to Python and NodeJS in that order
     - Click on Deploy

## Credits
- Horoscope calculator idea come from [this website](https://stackoverflow.com/questions/40275866/pycharm-shows-pep8-expected-2-blank-lines-found-1) and [this website](https://hackernoon.com/want-to-learn-python-lets-do-it-with-horoscopes-raq44oo)
- inspiration and guidance taken from [this youtube video](https://www.youtube.com/watch?v=8ext9G7xspg)
- Python help for horoscope generator came from [this youtube video](https://www.youtube.com/watch?v=Utvt8hKEoJU)
  
