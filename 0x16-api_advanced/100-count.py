#!/usr/bin/python3
"""word counter container"""

import requests


def count_words(subreddit, words_list, next_page="", count=[]):
    """count occurrences of words in the
    titles of hot posts in a subreddit."""

    # Initialize the count list on the first call
    if next_page == "":
        count = [0] * len(words_list)

    # Construct the API URL
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            params={'after': next_page},
                            allow_redirects=False,
                            headers={'User-Agent': 'loayIsMe'})

    if response.status_code == 200:
        data = response.json()

        # Iterate through each post and count occurrences of each word in the list
        for post in data['data']['children']:
            for word in post['data']['title'].split():
                for i in range(len(words_list)):
                    if words_list[i].lower() == word.lower():
                        count[i] += 1

        # Update the next_page variable with the 'after' value for pagination
        next_page = data['data']['after']
        if next_page is None:
            skip_indices = []
            # Combine count for duplicate words and sort results
            for i in range(len(words_list)):
                for j in range(i + 1, len(words_list)):
                    if words_list[i].lower() == words_list[j].lower():
                        skip_indices.append(j)
                        count[i] += count[j]

            # Sort words by count and alphabetically if count are equal
            for i in range(len(words_list)):
                for j in range(i, len(words_list)):
                    if (count[j] > count[i] or
                            (words_list[i] > words_list[j] and
                             count[j] == count[i])):
                        count[i], count[j] = count[j], count[i]
                        words_list[i], words_list[j] = words_list[j], words_list[i]

            # Print the results, excluding duplicates
            for i in range(len(words_list)):
                if count[i] > 0 and i not in skip_indices:
                    print("{}: {}".format(words_list[i].lower(), count[i]))
        else:
            # Recursive call to process the next page of data
            count_words(subreddit, words_list, next_page, count)

# Example usage
# count_words("programming", ["python", "java", "javascript"])


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(
            sys.argv[0]))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
