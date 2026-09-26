def get_hint(guess):
    if guess < 1000:
        return "enter a 4 digit number"

    elif guess >= 10000:
        return "enter a 4 digit number"

    elif 1000 <= guess <= 1999:
        return "try a much higher number"

    elif 2000 <= guess <= 3999:
        return "try higher, around 5000+"

    elif 4000 <= guess <= 4999:
        return "try higher, around 5000+"

    elif 5000 <= guess <= 5549:
        return "try a bit higher"

    elif 5551 <= guess <= 5600:
        return "try a bit lower"

    elif 5601 <= guess <= 6000:
        return "try a bit lower, under 5600"

    elif 6001 <= guess <= 8000:
        return "try a much lower number"

    elif 8001 <= guess <= 9999:
        return "try much lower"