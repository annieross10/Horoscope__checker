# Horoscope Calculator
Welcome to the Horoscope Calculator! 
The Horoscope Calculator is a simple Python program that allows users to get their horoscope predictions based on their birthdate and star sign. The program provides daily horoscope readings for each zodiac sign.
Whether you're seeking guidance, curious about what the stars have in store for you, or just want to explore the mystical realm of astrology, the Horoscope Calculator has you covered.

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
      
- Flexible Forecast Options
    - Choose between today's horoscope or get a sneak peek into what tomorrow holds.
    - This flexibility allows you to plan ahead and make informed decisions based on astrological insights

- Motivational Horoscope revealed
    - At the end of the questions, your personalised horoscope is revealed! Do what you wish with the information.
 
![Horoscope](/assets/images/screenshots/horoscopeprediction.png)
 
- Option to read another star sign at the end.
- Does not give you the oppertunity to input a false birthday.

![invalid month message](/assets/images/screenshots/invalidresponse.png)


## Data Model
- In my horoscope calculator, I have several elements that make up the data model. First, there is a dictionary called DAYS_OF_MONTHS which helps me validate the number of days in each month. It ensures that the user enters a valid day for their birthdate.
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


### Bugs
#### Solved Bugs
I encountered a few bugs while working on the horoscope calculator code, but I was able to fix them. One bug was related to validating the user's birth month. Previously, the code only checked if the month input was an integer, but it came up with in invalid response when the user entered the month as a name. To fix this, I added a check for month names in a list and converted them to the corresponding integer value. This ensured that both numeric and name inputs for the month were accepted.


### Validator Testing
- PEP8
  - No errors were returned form PEP8online.com


 
### Unfixed Bugs
No unfixed bugs

## Deployment
After preparing the site for deployment, the next step was to host it on GitHub pages. I followed these steps to deploy:



## Credits
### Content
