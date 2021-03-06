# python3 solution -- sort by count descending, quote_count descending, alphabetically
# Approach 1: Hashmap, sort by multiple keys
# Time complexity: O(W)+O(TlogT)

# W - total number of words(quotes* words in each quote)
# T - number of toys

# Space complexity: O(T) -->(dictionary)

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

toys_freq = {toy: [0,0] for toy in toys}
print(toys_freq)

for quote in quotes:
    # for each quote, initiate toy occurence to False
    quote_toy = {toy: False for toy in toys}

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

print(toys_freq.items())


# sort by count descending, quprint(toys_freq.items())ote_count descending, alphabetically
result = [w[0] for w in sorted(toys_freq.items(), key=lambda x: (-x[1][0],-x[1][1],x[0]))[:N]]
print(result)


#dict_items([('elmo', [4, 3]), ('elsa', [4, 2]), ('legos', [0, 0]), ('drone', [1, 1]), ('tablet', [0, 0]), ('warcraft', [1, 1])])
#['elmo', 'elsa', 'drone']
