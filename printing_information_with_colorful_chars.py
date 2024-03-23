import colorama

# Initialize colorama
colorama.init()

# Function to print text in rainbow colors with bold formatting
def print_rainbow_bold(text):
    colors = [colorama.Fore.RED, colorama.Fore.YELLOW, colorama.Fore.GREEN, colorama.Fore.CYAN, colorama.Fore.BLUE, colorama.Fore.MAGENTA]
    rainbow_text = ''
    
# Main program
    # Prompt user to input their name
name = input("Enter your name: ")

    # Prompt user to input their dream job
dream_job = input("Enter your dream job: ")

    # Print name 
print("\nYour name:", name)

    # Print dream job 
print("\nYour dream job: ", dream_job)