from collections import defaultdict # Imports the ability to create writable instance variables
from colorama import init, Fore, Back, Style # Imports the ability to color text and characters
import random
import re
import sys

init()

#  Credit to http://patorjk.com/software/taag/

scriptTitle = """
_______________________________________________________________________________________________________________________________ 
       /\_\/\_\ _           / /\              /\ \               _\ \            /\ \             / /\             / /\      
      / / / / //\_\        / /  \            /  \ \____         /\__ \           \ \ \           / /  \           / /  \     
     /\ \/ \ \/ / /       / / /\ \          / /\ \_____\       / /_ \_\          /\ \_\         / / /\ \         / / /\ \__  
    /  \____\__/ /       / / /\ \ \        / / /\/___  /      / / /\/_/         / /\/_/        / / /\ \ \       / / /\ \___\ 
   / /\/________/       / / /  \ \ \      / / /   / / /      / / /             / / /          / / /\ \_\ \      \ \ \ \/___/ 
  / / /\/_// / /       / / /___/ /\ \    / / /   / / /      / / /             / / /          / / /\ \ \___\      \ \ \       
 / / /    / / /       / / /_____/ /\ \  / / /   / / /      / / / ____        / / /          / / /  \ \ \__/  _    \ \ \      
/ / /    / / /       / /_________/\ \ \ \ \ \__/ / /      / /_/_/ ___/\  ___/ / /__        / / /____\_\ \   /_/\__/ / /      
\/_/    / / /       / / /_       __\ \_\ \ \___\/ /      /_______/\__\/ /\__\/_/___\      / / /__________\  \ \/___/ /       
        \/_/        \_\___\     /____/_/  \/_____/       \_______\/     \/_________/      \/_____________/   \_____\/  
By: Ninjer27                                                                                         Art: @http://patorjk.com/       
_______________________________________________________________________________________________________________________________                                                      
"""

print(Fore.BLUE + scriptTitle + Back.RESET + Fore.RESET)


# + '_: Random Story\n'




# Need blank respounce

def inputChecker(userInput):
    if re.match(r'^[a-zA-Z]*$', userInput):
        return True
    else:
        print('hOw DaRe YoU')

        return False

def border():
    print(Fore.BLUE + "_______________________________________________________________________________________________________________________________\n" + Fore.RESET)

def trueLoveQuestionMark():
    # Dictionary contains predetermined words that will be selected at random incase the user doesn't input anything
    noInput = {
        'adjList': ['Amazing', 'FABULOUSE', 'GORGEOUSE', 'GOD SEND'],
        'adverbList': ['really', 'absolutly', 'extremmly', 'sadly'],
        'nounList': ['robin', 'flea', 'dog', 'fly'],
        'verbList': ['mock', 'hate', 'laugh', 'teas'],
        'nameList': ['Jason', 'Tod', 'Danny', 'Ninja'],
        'locationList': ['basement', 'Africa', 'Zimbabewa', 'Makeschool']
    }


    
    
    # Collection of all User Input data collected and pulled into a list
    userAdj = input('Give me a ' + Fore.LIGHTCYAN_EX + 'Adjective: ' + Fore.RESET)
    if not userAdj.strip():
        userAdj = random.choice(noInput.get('adjList'))

    userAdverb = input('Give me a ' + Fore.LIGHTCYAN_EX + 'Adverb: ' + Fore.RESET)
    if not userAdverb.strip():
        userAdverb = random.choice(noInput.get('adverbList'))

    userNoun = input('Give me a' + Fore.LIGHTCYAN_EX + ' noun' + Fore.RESET + '(Prefered Animal): ')
    if not userNoun.strip():
        userNoun = random.choice(noInput.get('nounList'))
        
    userVerb = input('Give me a' + Fore.LIGHTCYAN_EX + ' verb: ' + Fore.RESET)
    if not userVerb.strip():
       userVerb = random.choice(noInput.get('verbList'))
    
    userLocation = input('Give me a' + Fore.LIGHTCYAN_EX + ' location: ' + Fore.RESET)
    if not userLocation.strip():
        userLocation = random.choice(noInput.get('locationList'))

    userName = input('Gime me someone\'s'+ Fore.LIGHTCYAN_EX +' name: ' + Fore.RESET)
    if not userName.strip():
        userName = random.choice(noInput.get('nameList'))

    # Border
    border()
    print( Fore.YELLOW + 'Your MADLIB has Been Generated' + Fore.RESET )
    border()


    print(
        f'Greg looked quite {userAdj.lower()} on a good day. He hated {userNoun.lower()}s because they {userAdverb.lower()} {userVerb.lower()}ed him for the way he looked. ' +
        f'In till he met {userName.title()}\'s {userNoun.lower()} his one true love in life in {userLocation.lower()}. {userName.title()} was honestly quite disgusted when he heard about this.')
    

   



try:
   storySelector = int(input('1: ' + Fore.CYAN + 'True Love Story?\n' + Fore.RESET+ '2: '+ Fore.RED +'-No Story-\n' + Fore.RESET+ '3: '+ Fore.RED+'-No Story-\n' + Fore.RESET + 'Choose a Story: '))
except ValueError:
   pass


# Story selection 1,2,3
if storySelector == 1:
    border()
    print(Fore.RED + Style.BRIGHT + 'Blank respouce will give you a random generated word')
    border()
    trueLoveQuestionMark()
elif storySelector == 2:
    print('wrong , choose 1')
elif storySelector == 3:
    print('No more chaotic ideas')


