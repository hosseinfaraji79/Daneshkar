with open('Zen.txt','r') as input_file:
    zen = input_file.read()
    """
    The Zen of Python, by Tim Peters
    """

replacements = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'ten': '10',
    'eleven': '11',
    'twelve': '12',
    'thirteen': '13',
    'fourteen': '14',
    'fifteen': '15',
    'sixteen': '16',
    'seventeen': '17',
    'eighteen': '18',
    'nineteen': '19',
}

for key,value in replacements.items():
    zen = zen.replace(key, value)

with open('Zen_New.txt' , 'w') as output_file:
    output_file.write(zen) 