import os
import random
import subprocess


HOROSCOPES = {
    'aries': [" Aries, you'll experience a boost of energy and motivation. Embrace this dynamic drive and use it to fuel your ambitions. Trust your instincts and take bold action towards your goals. Your natural leadership abilities will shine, propelling you towards success. Approach the day with confidence and determination.", "Exciting opportunities await, Aries! Unexpected possibilities will present themselves. Embrace change and step outside your comfort zone. Trust your intuition and take calculated risks. Your fearlessness and determination will help you overcome any challenges that arise. Stay focused on your objectives and let your adventurous spirit guide you to new horizons."],
    'taurus': ["Taurus, you'll feel a sense of stability and determination. Embrace this grounded energy and focus on your goals. Trust your practical instincts as you make decisions. Your patience and persistence will pay off, leading you to success. Stay rooted in your values and make steady progress towards your aspirations.", "Exciting opportunities await, Taurus! Unexpected possibilities will come your way. Embrace change with confidence and open-mindedness. Trust your instincts and take calculated steps towards new ventures. Your reliability and dedication will help you navigate any challenges that arise. Stay true to your goals and let your steady nature guide you to fruitful outcomes."],
    'cancer': ["Cancer, you'll experience a sense of emotional harmony and intuition. Embrace this nurturing energy and trust your instincts. Connect with your emotions and those around you on a deeper level. Your compassion and sensitivity will guide you in making supportive decisions. Embrace the day with love and care.", "Exciting opportunities await, Cancer! Unexpected possibilities will come knocking on your door. Embrace change with an open heart and receptive mindset. Trust your intuition and follow your gut feelings. Your nurturing nature will help you navigate any challenges that arise. Stay true to your dreams and let your emotional intelligence guide you to fulfillment."],
    'leo': ["Leo, you'll experience a surge of confidence and passion. Embrace this fiery energy and let it fuel your ambitions. Trust your instincts and take bold actions towards your goals. Your natural charisma and leadership abilities will shine brightly. Seize the day with enthusiasm and let your inner lion roar.", "Exciting opportunities await, Leo! Unexpected possibilities will come your way. Embrace change with courage and optimism. Trust your intuition and follow your heart's desires. Your magnetic personality will attract favorable circumstances. Embrace challenges with confidence, and your creativity and charisma will guide you towards success. Stay true to your vision and let your vibrant spirit shine."],
    'virgo': ["Virgo, you'll experience a sense of practicality and organization. Embrace this grounded energy and focus on the details. Trust your analytical mind as you make decisions. Your diligence and attention to detail will lead to success. Stay methodical in your approach and make progress towards your goals.", "Exciting opportunities await, Virgo! Unexpected possibilities will come your way. Embrace change with a discerning eye and a logical mindset. Trust your instincts and take calculated steps towards new ventures. Your reliability and meticulousness will help you navigate any challenges that arise. Stay true to your goals and let your practical nature guide you to fruitful outcomes."],
    'libra': ["Libra, you'll experience a sense of balance and harmony. Embrace this peaceful energy and seek equilibrium in your life. Trust your intuition as you make decisions. Your diplomatic nature will help you navigate any conflicts gracefully. Embrace the day with poise and kindness.", " Exciting opportunities await, Libra! Unexpected possibilities will come your way. Embrace change with grace and open-mindedness. Trust your instincts and consider all perspectives. Your charm and ability to find common ground will lead to favorable outcomes. Embrace challenges with balance, and your sense of harmony will guide you towards success. Stay true to your vision and let your diplomatic spirit shine."],
    'scorpio': ["Scorpio, you'll experience a surge of intensity and intuition. Embrace this powerful energy and trust your gut instincts. Dive deep into your emotions and embrace your inner strength. Your determination and resourcefulness will help you overcome any obstacles. Embrace the day with passion and unwavering focus.", "Exciting opportunities await, Scorpio! Unexpected possibilities will come your way. Embrace change with confidence and a sharp mind. Trust your instincts and follow your instincts. Your resilience and ability to adapt will help you navigate any challenges that arise. Stay true to your desires and let your transformative spirit guide you to success."],
    'sagittarius': ["Sagittarius, you'll experience a surge of optimism and adventure. Embrace this adventurous energy and let your curiosity lead the way. Trust your intuition and take bold steps towards your aspirations. Your free-spirited nature will attract exciting opportunities. Embrace the day with enthusiasm and embrace the thrill of the unknown.", "Exciting opportunities await, Sagittarius! Unexpected possibilities will come knocking on your door. Embrace change with an open mind and a sense of wonder. Trust your instincts and follow your passions. Your optimism and adaptability will help you navigate any challenges that arise. Stay true to your dreams and let your adventurous spirit guide you to new horizons."],
    'capricorn': ["Capricorn, brace yourself for an unexpected twist in your professional life. A hidden opportunity is set to resurface, bringing a surge of excitement and potential. Embrace this chance to showcase your skills and let your ambition shine. However, exercise caution and refrain from divulging your plans prematurely. Keep a guarded approach and let your actions speak for themselves. Success awaits if you stay focused and take calculated risks.", "Capricorn, the focus of tomorrow shifts towards finding balance and harmony in your personal relationships. It's time to mend any strained connections and foster a deeper understanding with your loved ones. Extend an olive branch to someone with whom you've had disagreements. Embrace empathy, compromise, and the power of forgiveness. By doing so, you can create a stronger foundation for long-lasting friendships and love. Communication plays a vital role, so express your thoughts and emotions openly and honestly."],
    'aquarius': ["Aquarius, you'll experience a surge of positivity and creativity. Embrace this energy and let your innovative ideas shine. Trust your intuition as you make important decisions, and don't be afraid to take bold steps towards your goals. Your unique perspective will lead you to exciting opportunities", "Get ready for an adventurous day, Aquarius! Unexpected opportunities will come your way, and it's time to embrace change. Your adaptability and open-mindedness will be your greatest assets. Stay true to your vision, and you'll overcome any challenges that come your way. Be open to new experiences and let your free spirit guide you to success"],
    'pisces': ["Pisces, you'll experience a surge of positive energy and inspiration. Embrace this creative flow and trust your intuition. Take courageous steps towards your dreams and watch them manifest into reality. Your compassionate nature will guide you towards meaningful connections and opportunities for growth.", " Get ready for exciting possibilities, Pisces! Unexpected opportunities will come knocking on your door. Embrace change and go with the flow. Trust your instincts and follow your heart's desires. Your adaptable and empathetic nature will help you navigate any challenges that arise. Stay true to your dreams and embrace the journey ahead."]
}

DAYS_OF_MONTHS = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}


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


def get_prediction(day_of_year, horoscope_day):
    if day_of_year in HOROSCOPES:
        horoscopes = HOROSCOPES[day_of_year]
        if horoscope_day == 'today':
            return horoscopes[0]
        elif horoscope_day == 'tomorrow':
            return horoscopes[1]
    return "No prediction available for the given day."


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
    # Convert month and day to the day of the year
    days_in_month = DAYS_OF_MONTHS[month]
    return sum(DAYS_OF_MONTHS[i] for i in range(1, month)) + day

def clear_screen():
    subprocess.run(["clear" if os.name != "nt" else "cls"], shell=True)

if __name__ == "__main__":
    birthday = get_birthday()
    day_of_year = convert_to_day_of_year(birthday[0], birthday[1])
    star_sign = get_star_sign(birthday[0], birthday[1])
    clear_screen()

    print(f"Your star sign is: {star_sign}")
    response = input("Do you want to know your horoscope? (yes/no):\n")

    if response.lower() == 'yes':
        clear_screen()
        horoscope_day = input("Do you want to know your horoscope for today or tomorrow? (today/tomorrow):\n")
        print()
        clear_screen()

        if horoscope_day.lower() == 'today' or horoscope_day.lower() == 'tomorrow':
            prediction = get_prediction(star_sign.lower(), horoscope_day.lower())
            print(f"Your horoscope prediction for {horoscope_day} is: {prediction}")
        else:
            print("Invalid input. Please try again.")
    else:
        print("Okay, maybe next time!")