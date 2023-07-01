import os
import subprocess
import textwrap

HOROSCOPES = {
    'aries': [
        "Aries, today is a day of new beginnings and fresh starts. "
        "Embrace the opportunities that come your way "
        "with confidence and enthusiasm. Trust your instincts and "
        "take decisive actions. Your energy and determination will "
        "help you overcome any challenges. Embrace the day with courage "
        "and let your inner warrior shine. ",
        "Exciting opportunities await, Aries! Tomorrow brings new "
        "possibilities. Embrace change with optimism and boldness. "
        "Trust your instincts and take calculated risks. Your dynamic "
        "nature and passion will attract favourable circumstances. "
        "Embrace challenges with confidence and determination, and your inner "
        "warrior will guide you to success. "
    ],
    'taurus': [
        "Taurus, today is a day of stability and grounding. Focus on "
        "building a solid foundation for your goals and dreams. Trust "
        "your practicality and determination. Your patience and persistence "
        "will help you overcome any challenges. Embrace the day with "
        "resilience and let your inner builder thrive. ",
        "Exciting opportunities await, Taurus! Tomorrow brings stability "
        "and growth. Embrace change with steadiness and determination. "
        "Trust your practical mindset and stay committed to your goals. Your "
        "perseverance and hard work will attract favorable circumstances. "
        "Embrace challenges with resilience and determination, and your "
        "inner builder will lead you to fulfillment. "
    ],
    'gemini': [
        "Gemini, today is a day of communication and intellectual pursuits. "
        "Engage in stimulating conversations and seek knowledge. Trust your "
        "curiosity and adaptability. Your wit and versatility will help you "
        "overcome any challenges. Embrace the day with openness and let your "
        "inner communicator shine. ",
        "Exciting opportunities await, Gemini! Tomorrow brings intellectual "
        "growth and social connections. Embrace change with curiosity and "
        "adaptability. Trust your communication skills and seek new knowledge."
        " Your versatility and quick thinking will attract favorable "
        "circumstances. Embrace challenges with openness and creativity, "
        "and your inner communicator will guide you to fulfillment. "
    ],
    'cancer': [
        "Cancer, today is a day of emotional depth and intuition. Connect "
        "with your emotions and trust your intuition. Pay attention to your "
        "inner voice. Your sensitivity and nurturing nature will help you "
        "overcome any challenges. Embrace the day with compassion and let your"
        " inner nurturer thrive.",
        "Exciting opportunities await, Cancer! Tomorrow brings emotional "
        "growth and harmony. Embrace change with intuition and compassion. "
        "Trust your nurturing instincts and listen to your inner voice. Your "
        "empathy and sensitivity will attract favorable circumstances. Embrace"
        " challenges with love and understanding, and your inner nurturer will"
        " lead you to fulfillment. "
    ],
    'leo': [
        "Leo, today is a day of self-expression and creativity. Let your "
        "unique personality shine and embrace your creativity. Trust your "
        "inner fire and passion. Your confidence and leadership will help you "
        "overcome any challenges. Embrace the day with enthusiasm and let "
        "your inner performer thrive. ",
        "Exciting opportunities await, Leo! Tomorrow brings self-expression "
        "and creativity. Embrace change with confidence and passion. Trust "
        "your inner fire and let your creativity soar. Your charisma and "
        "leadership will attract favorable circumstances. Embrace challenges "
        "with enthusiasm and determination, and your inner performer will "
        "guide you to success. "
    ],
    'virgo': [
        "Virgo, today is a day of organization and attention to detail. "
        "Focus on practical matters and pay attention to the finer points. "
        "Trust your analytical mind and methodical approach. Your diligence "
        "and efficiency will help you overcome any challenges. Embrace the "
        "day with precision and let your inner perfectionist thrive. ",
        "Exciting opportunities await, Virgo! Tomorrow brings organization "
        "and growth. Embrace change with attention to detail and practicality."
        " Trust your analytical mind and focus on efficiency. Your methodical "
        "approach and attention to detail will attract favourable "
        "circumstances. Embrace challenges with precision and dedication, "
        "and your inner perfectionist will lead you to fulfillment. "
    ],
    'libra': [
        "Libra, today is a day of balance and harmony. Seek peace and fairness"
        " in all your interactions. Trust your sense of justice and diplomacy."
        " Your charm and ability to compromise will help you overcome any "
        "challenges. Embrace the day with grace and let your inner diplomat "
        "shine. ",
        "Exciting opportunities await, Libra! Tomorrow brings balance and "
        "harmony. Embrace change with fairness and diplomacy. Trust your sense"
        " of justice and seek peace in all your interactions. Your charm and "
        "ability to compromise will attract favorable circumstances. Embrace "
        "challenges with grace and diplomacy, and your inner diplomat will "
        "guide you to fulfillment. "
    ],
    'scorpio': [
        "Scorpio, today is a day of transformation and intensity. Embrace your"
        " inner power and let go of what no longer serves you. Trust your "
        "instincts and embrace change. Your determination and resilience will "
        "help you overcome any challenges. Embrace the day with passion and "
        "let your inner warrior thrive. ",
        "Exciting opportunities await, Scorpio! Tomorrow brings transformation"
        " and intensity. Embrace change with determination and resilience. "
        "Trust your instincts and let go of what no longer serves you. Your "
        "inner power and intensity will attract favorable circumstances. "
        "Embrace challenges with passion and determination, and your inner "
        "warrior will guide you to success. "
    ],
    'sagittarius': [
        "Sagittarius, today is a day of adventure and expansion. Seek new "
        "experiences and broaden your horizons. Trust your inner wisdom "
        "and embrace change. Your optimism and enthusiasm will help you "
        "overcome any challenges. Embrace the day with adventure and let "
        "your inner explorer thrive. ",
        "Exciting opportunities await, Sagittarius! Tomorrow brings adventure "
        "and expansion. Embrace change with optimism and curiosity. Trust "
        "your inner wisdom and seek new experiences. Your enthusiasm and "
        "optimism will attract favorable circumstances. Embrace challenges "
        "with adventure and openness, and your inner explorer will lead you "
        "to fulfillment. "
    ],
    'capricorn': [
        "Capricorn, today is a day of discipline and ambition. Focus on your "
        "long-term goals and take practical steps towards success. Trust your "
        "perseverance and determination. Your hard work and responsibility "
        "will help you overcome any challenges. Embrace the day with "
        "discipline and let your inner achiever thrive. ",
        "Exciting opportunities await, Capricorn! Tomorrow brings discipline "
        "and ambition. Embrace change with perseverance and practicality. "
        "Trust your long-term goals and take responsible actions. Your "
        "determination and hard work will attract favorable circumstances. "
        "Embrace challenges with discipline and focus, and your inner "
        "achiever will guide you to success. "
    ],
    'aquarius': [
        "Aquarius, today is a day of innovation and humanitarianism. Embrace "
        "your unique perspective and think outside the box. Trust your "
        "intuition and embrace change. Your humanitarian efforts and "
        "intellectual insights will help you overcome any challenges. Embrace "
        "the day with innovation and let your inner reformer thrive. ",
        "Exciting opportunities await, Aquarius! Tomorrow brings innovation "
        "and humanitarianism. Embrace change with intuition and intellectual "
        "curiosity. Trust your unique perspective and think outside the box. "
        "Your innovative ideas and humanitarian efforts will attract favorable"
        " circumstances. Embrace challenges with innovation and compassion, "
        "and your inner reformer will guide you to fulfillment. "
    ],
    'pisces': [
        "Pisces, today is a day of imagination and spirituality. Connect "
        "with your inner self and explore your dreams. Trust your intuition "
        "and embrace change. Your empathy and sensitivity will help you "
        "overcome any challenges. Embrace the day with creativity and let "
        "your inner dreamer thrive. ",
        "Exciting opportunities await, Pisces! Tomorrow brings imagination "
        "and spirituality. Embrace change with intuition and empathy. Trust "
        "your dreams and connect with your inner self. Your creativity and "
        "sensitivity will attract favorable circumstances. Embrace "
        "challenges with imagination and spirituality, and your inner "
        "dreamer will lead you to fulfillment. "
    ]
}

# days of the month
DAYS_OF_MONTHS = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}


# valid date
def is_valid_date(month, day):
    if month in DAYS_OF_MONTHS and day <= DAYS_OF_MONTHS[month]:
        return True
    return False


# star signs
def get_star_sign(month, day):
    star_signs = [
        ('Capricorn', (1, 1), (1, 19)),
        ('Aquarius', (1, 20), (2, 18)),
        ('Pisces', (2, 19), (3, 20)),
        ('Aries', (3, 21), (4, 19)),
        ('Taurus', (4, 20), (5, 20)),
        ('Gemini', (5, 21), (6, 20)),
        ('Cancer', (6, 21), (7, 22)),
        ('Leo', (7, 23), (8, 22)),
        ('Virgo', (8, 23), (9, 22)),
        ('Libra', (9, 23), (10, 22)),
        ('Scorpio', (10, 23), (11, 21)),
        ('Sagittarius', (11, 22), (12, 21)),
        ('Capricorn', (12, 22), (12, 31))
    ]

    if not is_valid_date(month, day):
        return "Invalid date"

    date = (month, day)

    for sign, (start_month, start_day), (end_month, end_day) in star_signs:
        if (start_month, start_day) <= date <= (end_month, end_day):
            return sign

    return "Invalid star sign"


# clear screen from previous question
def clear_screen():
    subprocess.run(["clear" if os.name != "nt" else "cls"], shell=True)


def get_name():
    name = input("Please enter your name:\n")
    return name


# predictions for either today or tomorrow
def get_prediction(day_of_year, horoscope_day):
    if day_of_year in HOROSCOPES:
        horoscopes = HOROSCOPES[day_of_year]
        if horoscope_day == 'today':
            return horoscopes[0]
        elif horoscope_day == 'tomorrow':
            return horoscopes[1]
    return "No prediction available for the given day."


# get birthday information
def get_birthday():
    clear_screen()
    month_input = input("Please enter the month you were \
born (name or number):\n")
    month = None

    if month_input.isdigit():
        month = int(month_input)
    else:
        month_names = [
            'january', 'february', 'march', 'april',
            'may', 'june', 'july', 'august',
            'september', 'october', 'november', 'december'
        ]
        month_input_lower = month_input.lower()

        if month_input_lower in month_names:
            month = month_names.index(month_input_lower) + 1

    if month is None or month < 1 or month > 12:
        print("Invalid month entered. Please try again.")
        return get_birthday()
    while True:
        day_input = input("Now enter the day:\n")
        if day_input.isdigit():
            day = int(day_input)
            if is_valid_date(month, day):
                break
            else:
                print("Invalid day entered. Please try again.")
        else:
            try:
                day = int(day_input[:-2])
                if is_valid_date(month, day):
                    break
                else:
                    print("Invalid day entered. Please try again.")
            except ValueError:
                print("Invalid day entered. Please try again.")

    return month, day


def convert_to_day_of_year(month, day):
    days_in_month = DAYS_OF_MONTHS[month]
    return sum(DAYS_OF_MONTHS[i] for i in range(1, month)) + day


# calculate star sign
if __name__ == "__main__":
    while True:
        name = get_name()
        print(f"\nWelcome, {name}!")

        while True:
            birthday = get_birthday()
            day_of_year = convert_to_day_of_year(birthday[0], birthday[1])
            star_sign = get_star_sign(birthday[0], birthday[1])
            clear_screen()
            print(f"Your star sign is: {star_sign}")

            # Ask user if they want their horoscope read
            response = input("Do you want to know your horoscope? (yes/no):\n")

            if response.lower() == 'yes':
                clear_screen()
                horoscope_day = input("Which day would you like to know your "
                                      "horoscope? (today/tomorrow):\n")
                print()
                clear_screen()

                if horoscope_day.lower() == 'today' or \
                   horoscope_day.lower() == 'tomorrow':
                    prediction = get_prediction(star_sign.lower(),
                                                horoscope_day.lower())
                    wrapped_prediction = textwrap.fill(prediction, width=80)
                    print(f"{name}... Your horoscope prediction for \
{horoscope_day} is...\n")
                    print(wrapped_prediction)
                else:
                    print("Invalid input. Please try again.")
            else:
                print("Okay, maybe next time!")

            # Ask user if they want to start again
            repeat_response = input("\nWould you like another horoscope read? "
                                    "(yes/no):\n")

            if repeat_response.lower() != 'yes':
                break
            clear_screen()
        print("Thank you for using the horoscope service. Goodbye!")
