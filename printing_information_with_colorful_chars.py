import colorama
import random

# Initialize colorama
colorama.init()

# Function to print text in rainbow colors with bold formatting
def print_rainbow_bold(text):
    colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN, colorama.Fore.CYAN, colorama.Fore.BLUE, colorama.Fore.MAGENTA]
    rainbow_text = ''
    for char in text:
        rainbow_text += random.choice(colors) + char
    print(colorama.Style.BRIGHT + rainbow_text + colorama.Style.RESET_ALL)

# Main program
if __name__ == "__main__":

    # Prompt user to input their name
    name = input("Enter your name: ")

    # Prompt user to input their gender
    gender = input("Enter your gender: ")

    # Prompt user to input their favorite quote
    fav_quote = input("Enter your favorite quote: ")

    # Prompt user to input their dream job
    dream_job = input("Enter your dream job: ")

    # Print name 
    print("\nYour name:")
    print_rainbow_bold(name)

    # Print gender
    print("\nYour gender:")
    print_rainbow_bold(gender)

    # Print favorite quote
    print("\nYour favorite quote:")
    print_rainbow_bold(fav_quote)

    # Print dream job 
    print("\nYour dream job: ")
    print_rainbow_bold(name)