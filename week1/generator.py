import random

class TextGenerator:
    def __init__(self):
        self.dict = {}
    
    # Function to create dictionary of tuple to list of words with tuple as key
    def assimilateText(self, name):             
        with open(name, 'r') as file:
            letter = file.read()
            text = letter.split()

            for i in range(len(text) - 2):
                pre = (text[i], text[i+1])

                # Checks whether current tuple is in the dictionary, if present then append the next word
                if pre not in self.dict:                          
                    self.dict[pre] = [text[i+2]]

                else:
                    self.dict[pre].append(text[i+2])
    
    def generateText(self, num, start = None):
        tuple = ""
        
        # Checking if the 1st word 
        if start is not None and start not in [i[0] for i in self.dict.keys()]:
            raise Exception("<class 'Exception'>\nUnable to produce letter with the specified start word.")

        if self.dict is {}:
            print("Waiting to assimilate tuple")

        # list to pick all tuple in key of dictionary with 1st element is sample word
        if start is not None:
            temp = []

            for i in self.dict.keys():
                if i[0] == start:
                    temp.append(i)

            # Picking 1 random tuple from list temp
            current = random.choice(temp)
            tuple += start + " " + current[1]
        
        # If no word to start is given, choosing any random word from sample text 
        else:
            current = random.choice(list(self.dict))
            tuple += current[0] + " " + current[1]

        # Choosing 1 random word from the list assigned to current tuple
        for i in range(num - 2):
            next = random.choice(self.dict[current])
            tuple += ' ' + str(next)
            current = (current[1] ,next)
        print(tuple)


# Test case
t = TextGenerator()
t.assimilateText('sherlock.txt')
t.generateText(100  , "London")