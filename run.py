import os
import random
import subprocess
import textwrap

#horoscopes
HOROSCOPES = {
    'aries': [
        "Aries, you'll experience a boost of energy and motivation. Embrace this dynamic drive and use it to fuel your ambitions. "
        "Trust your instincts and take bold action towards your goals. Your natural leadership abilities will shine, "
        "propelling you towards success. Approach the day with confidence and determination.",
        "Exciting opportunities await, Aries! Unexpected possibilities will present themselves. Embrace change and step outside "
        "your comfort zone. Trust your intuition and take calculated risks. Your fearlessness and determination will help you "
        "overcome any challenges that arise. Stay focused on your objectives and let your adventurous spirit guide you to "
        "new horizons."
    ],
    'taurus': [
        "Taurus, you'll feel a sense of stability and determination. Embrace this grounded energy and focus on your goals. "
        "Trust your practical instincts as you make decisions. Your patience and persistence will pay off, leading you to success. "
        "Stay rooted in your values and make steady progress towards your aspirations.",
        "Exciting opportunities await, Taurus! Unexpected possibilities will come your way. Embrace change with confidence and "
        "open-mindedness. Trust your instincts and take calculated steps towards new ventures. Your reliability and dedication "
        "will help you navigate any challenges that arise. Stay true to your goals and let your steady nature guide you to "
        "fruitful outcomes."
    ],
    'cancer': [
        "Cancer, you'll experience a sense of emotional harmony and intuition. Embrace this nurturing energy and trust your instincts. "
        "Connect with your emotions and those around you on a deeper level. Your compassion and sensitivity will guide you in making "
        "supportive decisions. Embrace the day with love and care.",
        "Exciting opportunities await, Cancer! Unexpected possibilities will come knocking on your door. Embrace change with an "
        "open heart and receptive mindset. Trust your intuition and follow your gut feelings. Your nurturing nature will help you "
        "navigate any challenges that arise. Stay true to your dreams and let your emotional intelligence guide you to fulfillment."
    ],
    'gemini': [
        "Gemini, you'll experience a surge of intellectual energy and communication skills. Embrace this mental clarity and "
        "express yourself with confidence. Trust your instincts and engage in meaningful conversations. Your versatility and "
        "quick thinking will help you navigate any situation. Embrace the day with curiosity and embrace new ideas.",
        "Exciting opportunities await, Gemini! Unexpected possibilities will come your way. Embrace change with adaptability and "
        "an open mind. Trust your instincts and follow your curiosity. Your versatility and wit will help you navigate any "
        "challenges that arise. Stay true to your interests and let your communication skills shine."
    ],
    'leo': [
        "Leo, you'll experience a surge of confidence and passion. Embrace this fiery energy and let it fuel your ambitions. "
        "Trust your instincts and take bold actions towards your goals. Your natural charisma and leadership abilities will shine "
        "brightly. Seize the day with enthusiasm and let your inner lion roar.",
        "Exciting opportunities await, Leo! Unexpected possibilities will come your way. Embrace change with courage and optimism. "
        "Trust your intuition and follow your heart's desires. Your magnetic personality will attract favorable circumstances. "
        "Embrace challenges with confidence, and your creativity and charisma will guide you towards success. Stay true to your "
        "passions and let your inner fire light the way."
    ],
    'virgo': [
        "Virgo, you'll feel a sense of practicality and efficiency. Embrace this organized energy and focus on your goals. "
        "Trust your analytical mind as you make decisions. Your attention to detail and hard work will pay off, leading you to "
        "success. Stay dedicated and disciplined in your endeavors.",
        "Exciting opportunities await, Virgo! Unexpected possibilities will present themselves. Embrace change with adaptability "
        "and precision. Trust your instincts and take calculated steps towards new ventures. Your meticulous nature and "
        "discerning eye will help you navigate any challenges that arise. Stay true to your goals and let your practicality "
        "guide you to fruitful outcomes."
    ],
    'libra': [
        "Libra, you'll experience a sense of balance and harmony. Embrace this harmonious energy and seek peace in all areas of your life. "
        "Trust your intuition as you make decisions. Your diplomatic nature and sense of justice will guide you in resolving conflicts. "
        "Embrace the day with grace and find equilibrium within yourself.",
        "Exciting opportunities await, Libra! Unexpected possibilities will present themselves. Embrace change with poise and "
        "openness. Trust your instincts and seek harmony in all endeavors. Your charm and tact will help you navigate any challenges "
        "that arise. Stay true to your values and let your balanced nature guide you to rewarding outcomes."
    ],
    'scorpio': [
        "Scorpio, you'll feel a surge of intensity and passion. Embrace this powerful energy and embrace your transformative nature. "
        "Trust your instincts and follow your desires. Your determination and resourcefulness will help you overcome any obstacles. "
        "Seize the day with courage and let your inner strength guide you.",
        "Exciting opportunities await, Scorpio! Unexpected possibilities will come your way. Embrace change with resilience and "
        "assertiveness. Trust your instincts and follow your passions. Your magnetic aura will attract favorable circumstances. "
        "Embrace challenges with confidence, and your perseverance and intuition will lead you to success. Let your inner fire "
        "ignite your path."
    ],
    'sagittarius': [
        "Sagittarius, you'll feel a sense of adventure and optimism. Embrace this free-spirited energy and explore new horizons. "
        "Trust your intuition as you embark on new journeys. Your enthusiasm and open-mindedness will guide you in embracing "
        "opportunities. Seize the day with optimism and let your inner explorer thrive.",
        "Exciting opportunities await, Sagittarius! Unexpected possibilities will present themselves. Embrace change with "
        "enthusiasm and an adventurous spirit. Trust your instincts and take bold steps towards new experiences. Your optimism "
        "and curiosity will help you navigate any challenges that arise. Stay true to your dreams and let your inner fire guide "
        "you to exciting horizons."
    ],
    'capricorn': [
        "Capricorn, you'll experience a sense of determination and ambition. Embrace this driven energy and focus on your goals. "
        "Trust your instincts as you make important decisions. Your disciplined nature and practical mindset will lead you to success. "
        "Stay committed to your path and embrace the day with confidence.",
        "Exciting opportunities await, Capricorn! Unexpected possibilities will come your way. Embrace change with patience and "
        "strategic thinking. Trust your instincts and take calculated steps towards your goals. Your hard work and dedication "
        "will help you navigate any challenges that arise. Stay true to your aspirations and let your ambition guide you to "
        "achievements."
    ],
    'aquarius': [
        "Aquarius, you'll feel a surge of innovative energy and intellectual stimulation. Embrace this creative flow and express "
        "yourself authentically. Trust your intuition and follow your unique ideas. Your visionary thinking and humanitarian "
        "nature will guide you in making a positive impact. Embrace the day with inventiveness and let your inner rebel shine.",
        "Exciting opportunities await, Aquarius! Unexpected possibilities will come your way. Embrace change with adaptability and "
        "originality. Trust your instincts and take calculated risks. Your progressive mindset and innovative ideas will help you "
        "navigate any challenges that arise. Stay true to your values and let your intellectual prowess guide you to new frontiers."
    ],
    'pisces': [
        "Pisces, you'll experience a sense of intuition and compassion. Embrace this intuitive energy and trust your inner guidance. "
        "Connect with your emotions and those around you on a deeper level. Your empathy and imagination will guide you in making "
        "supportive decisions. Embrace the day with love and kindness.",
        "Exciting opportunities await, Pisces! Unexpected possibilities will come your way. Embrace change with an open heart and "
        "receptive mindset. Trust your intuition and follow your dreams. Your artistic nature and spiritual depth will help you "
        "navigate any challenges that arise. Stay true to your passions and let your intuition lead you to fulfillment."
    ]
}

#days of the month
DAYS_OF_MONTHS = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

#star signs
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

    date = (month, day)

    for sign, (start_month, start_day), (end_month, end_day) in star_signs:
        if (start_month, start_day) <= date <= (end_month, end_day):
            return sign

    return "Invalid star sign"


#predictions for either today or tomorrow
def get_prediction(day_of_year, horoscope_day):
    if day_of_year in HOROSCOPES:
        horoscopes = HOROSCOPES[day_of_year]
        if horoscope_day == 'today':
            return horoscopes[0]
        elif horoscope_day == 'tomorrow':
            return horoscopes[1]
    return "No prediction available for the given day."

#get birthday information
def get_birthday():
    month_input = input("Please enter the month you were born (name or number):\n")
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
    clear_screen()
    day = int(input("Now enter the day:\n"))
    return month, day


def convert_to_day_of_year(month, day):
    days_in_month = DAYS_OF_MONTHS[month]
    return sum(DAYS_OF_MONTHS[i] for i in range(1, month)) + day

#clear screen from previous question
def clear_screen():
    subprocess.run(["clear" if os.name != "nt" else "cls"], shell=True)

#calculate star sign
if __name__ == "__main__":
    while True:
        birthday = get_birthday()
        day_of_year = convert_to_day_of_year(birthday[0], birthday[1])
        star_sign = get_star_sign(birthday[0], birthday[1])
        clear_screen()
        print(f"Your star sign is: {star_sign}")

        #ask user if they want their horoscope read
        response = input("Do you want to know your horoscope? (yes/no):\n")

        if response.lower() == 'yes':
            clear_screen()
            horoscope_day = input("Which day would you like to know your horoscope? (today/tomorrow):\n")
            print()
            clear_screen()

            if horoscope_day.lower() == 'today' or horoscope_day.lower() == 'tomorrow':
                prediction = get_prediction(star_sign.lower(), horoscope_day.lower())
                wrapped_prediction = textwrap.fill(prediction, width=80) 
                print(f"Your horoscope prediction for {horoscope_day} is:")
                print(wrapped_prediction)
            else:
                print("Invalid input. Please try again.")
        else:
            print("Okay, maybe next time!")

        #ask user if they want to start again
        repeat_response = input("Would you like another horoscope read? (yes/no):\n")

        if repeat_response.lower() != 'yes':
            break
        clear_screen()

    print("Thank you for using the horoscope service. Goodbye!")

