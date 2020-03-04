# Approach 2 -- min heap of size N(max toys) at any time, toy class with modified comparator
# Time complexity: O(W)+O(TlogN) ---> maintain heap of size N(max toys) at any time

# W - total number of words(quotes* words in each quote)
# T - number of toys
#N - max number of toys to return

# Space complexity: O(T) + O(N) -->(dictionary + heap)

import heapq
import re

quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
N=3

# create a dictionary --> toy:[count, quote_count]
toys_freq = {toy:[0,0] for toy in toys}
for quote in quotes:
    # for each quote, initiate toy occurence to False
    quote_toy = {toy:False for toy in toys}
    # convert quote to lower case,split 
    for word in quote.lower().split():
        # remove anything other than lower cased letters in each word
        word = re.sub('[^a-z]','',word)
        # increment count of toy if it exists in toys dictionary
        if word in toys_freq:
            toys_freq[word][0] += 1
            # if toy found in a quote, set to True and increment quote_count--> we do it only once for a toy in a quote
            if not quote_toy[word]:
                quote_toy[word] = True
                toys_freq[word][1] += 1                
# print toy, count, quote_count
print(toys_freq.items()) 
                
# modify comparator in Toy class(__lt__) to move min priority toys to root of min heap
class Toy:
    def __init__(self, count, quote,toy):
        self.count = count
        self.quote = quote
        self.toy = toy
    
    def __lt__(self,other):
        if not self.count==other.count:
            return self.count < other.count
        if not self.quote == other.quote:
            return self.quote < other.quote
        return self.toy > other.toy

toys_res = []
for toy in toys_freq:
    t = Toy(toys_freq[toy][0],toys_freq[toy][1],toy)
    heapq.heappush(toys_res,t)
    if len(toys_res)>N:
        heapq.heappop(toys_res)
output = []
while toys_res:
    output.append(heapq.heappop(toys_res).toy)
# reverse order--> min heap pops min priority toy
print(output[::-1])
#dict_items([('elmo', [4, 3]), ('elsa', [4, 2]), ('legos', [0, 0]), ('drone', [1, 1]), ('tablet', [0, 0]), ('warcraft', [1, 1])])
#['elmo', 'elsa', 'drone']
