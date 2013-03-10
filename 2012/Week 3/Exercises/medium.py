converter = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

def performCalc(line):
    calc = line.split(' ') # transforms the line into a list splitting each word into an element (with a ' ' seperator)
    val1 = converter[calc[0].lower()]
    val2 = converter[calc[2].lower()]

    if calc[1] == 'plus':
        return val1 + val2

    elif calc[1] == 'minus':
        return val1 - val2
    
    elif calc[1] == 'times':
        return val1 * val2

    elif calc[1] == 'divided_by':
        return val1 / val2

while True:
    print performCalc(raw_input("Enter a Calculation: "))
