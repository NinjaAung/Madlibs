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


# + '4: Random Story\n'

storySelector = int(input('1: True Love Story?\n' + '2: -No Story-\n' + '3: -No Story-\n' + 'Choose a Story: '))
print( Fore.BLUE + "_______________________________________________________________________________________________________________________________\n" + Fore.RESET)

# Need blank respounce

def inputChecker(userInput):
    if re.match(r'^[a-zA-Z]*$', userInput):
        return True
    else:
        print('You cannot use special characters.')
        return False


def trueLoveQuestionMark():
    # Dictionary contains predetermined words that will be selected at random incase the user doesn't input anything
    noInput = {
        'adjList': ['Amazing', 'FABULOUSE', 'GORGEOUSE', 'GOD SEND'],
        'nounList': ['robin', 'flea', 'dog', 'fly'],
        'verbList': ['mock', 'hate', 'laugh', 'teas'],
        'nameList': ['Jason', 'Tod', 'Danny', 'Ninja'],
        'locationList': ['basement', 'Africa', 'Zimbabewa', 'Makeschool']
    }


    
    

    userAdj = input('Give me a Adjective: ')
    if not userAdj.strip():
        userAdj = random.choice(noInput.get('adjList'))

    userNoun = input('Give me a noun(Prefered Animal): ')
    if not userNoun.strip():
        userNoun = random.choice(noInput.get('nounList'))
        
    userVerb = input('Give me a verb: ')
    if not userVerb.strip():
       userVerb = random.choice(noInput.get('verbList'))
    
    userLocation = input('Give me a location: ')
    if not userLocation.strip():
        userLocation = random.choice(noInput.get('locationList'))

    userName = input('Gime me someone\'s name: ')
    if not userName.strip():
        userName = random.choice(noInput.get('nameList'))

    # Border
    print(Fore.BLUE + "_______________________________________________________________________________________________________________________________\n" + Fore.RESET + Fore.YELLOW + "Your MadLib was generated: \n" + Fore.RESET)
    
    print(
        f'greg looked quite {userAdj.lower()} on a good day. He hated {userNoun.lower()}s because they {userVerb.lower()}ed him for the way he looked. ' +
        f'In till he met {userName.title()}\'s {userNoun.lower()} his one true love in life in {userLocation.lower()}. {userName.title()} was honestly quite disgusted when he heard about this.')






# Story selection 1,2,3
if storySelector == 1:
    print(Fore.RED + Style.BRIGHT + 'Blank respouce will give you a random generated word')
    trueLoveQuestionMark()
elif storySelector == 2:
    print('wrong , choose 1')
elif storySelector == 3:
    print('No more chaotic ideas')

