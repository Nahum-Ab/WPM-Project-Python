import time
import random
import math

texts = [
    'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity.',
    'Thr only limit to our realization of tomorrow will be our doubts of today.',
    'The sun dipped below the horizon, painting the sky in hues of orange and pink, while the gentle breeze whispered through the leaves, creating a symphony of nature that soothed the soul.',
    'Water, a vital substance for life on Earth, boils at 100 degrees Celsius at sea level, a fact that is fundamental to understanding thermodynamics and the behavior of liquids under varying atmospheric pressures.',
    'The mitochondria, often referred to as the powerhouse of the cell, plays a crucial role in converting nutrients into energy through a process called cellular respiration, which is essential for the survival of all aerobic organisms.',
    "The Declaration of Independence, signed on July 4, 1776, marked a pivotal moment in American history, as it formally proclaimed the thirteen colonies' separation from British rule and laid the groundwork for the values of freedom and democracy that the nation would strive to uphold.",
    "The Amazon Rainforest, often referred to as the lungs of the planet, is an incredibly diverse ecosystem that spans across several countries in South America and is home to countless species of plants and animals, many of which are found nowhere else on Earth.",
    "Mount Everest, standing at an impressive height of 8,848 meters above sea level, is recognized as the highest mountain in the world and attracts climbers from all over the globe who seek to conquer its challenging peaks and experience its breathtaking views.",
    "In the middle of every difficulty lies opportunity, a profound statement by Albert Einstein that encourages us to view challenges as chances for growth and innovation rather than insurmountable obstacles.",
    "I told my computer that I needed a break, and now it won’t stop sending me beach wallpapers, a funny reminder of how our devices sometimes interpret our requests in unexpected ways",
    "Write about a mysterious forest filled with ancient trees, their gnarled roots twisting through the earth, while shafts of sunlight pierce through the dense canopy, illuminating the hidden paths and the whispers of the creatures that call this magical place home.",
    "Octopuses are remarkable creatures with three hearts and blue blood, adaptations that allow them to thrive in deep ocean environments, showcasing the incredible diversity of life found beneath the waves."
]

def calculate_WPM(start_time, end_time, words_typed):
    time_taken = end_time - start_time
    minutes_taken = time_taken/60
    wpm = words_typed/minutes_taken

    if minutes_taken > 0:
        return wpm
    else:
        return 0

def WPM_game():
    # Select a random text
    text_to_type = random.choice(texts)

    print('Type the following text as quickly and accurately as you can: \n')
    print(text_to_type)
    print('\nPress Enter to start...')

    input() # Waiting for the user to press a key :)

    start_time = time.time() # start the timer
    user_input = input('\nStart typing: ') # capture the users input :)
    end_time = time.time() # End the timer

    # calculate_WPM
    words_typed = len(user_input.split())
    wpm = round(calculate_WPM(start_time, end_time, words_typed))


    # calculate accuracy
    correct_words = sum(1 for a, b in zip(user_input.split(),
                    text_to_type.split()) if a == b)

    accuracy = round((correct_words/len(text_to_type.split()))*100)

    # Display results

    print(f'\nYour WPM: {wpm: 2f}')
    print(f'Accuracy: {accuracy: 2f}%')


if __name__ == "__main__":
    WPM_game()