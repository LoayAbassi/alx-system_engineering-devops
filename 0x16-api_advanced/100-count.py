#!/usr/bin/python3
"""word counter container"""

import requests


def count_words(subreddit, w_list, next_page="", count=[]):
    """count occurrences of words in the
    titles of hot posts in a subreddit."""

    # Initialize the count list on the first call
    if next_page == "":
        count = [0] * len(w_list)

    # Construct the API URL
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url,
                            params={'after': next_page},
                            allow_redirects=False,
                            headers={'User-Agent': 'loayIsMe'})

    if response.status_code == 200:
        data = response.json()

        # Iterate through each post and count
        # occurrences of each word in the list
        for post in data['data']['children']:
            for word in post['data']['title'].split():
                for i in range(len(w_list)):
                    if w_list[i].lower() == word.lower():
                        count[i] += 1

        # Update the next_page variable with
        # the 'after' value for pagination
        next_page = data['data']['after']
        if next_page is None:
            skip_indices = []
            # Combine count for duplicate words and sort results
            for i in range(len(w_list)):
                for j in range(i + 1, len(w_list)):
                    if w_list[i].lower() == w_list[j].lower():
                        skip_indices.append(j)
                        count[i] += count[j]

            # Sort words by count and alphabetically if count are equal
            for i in range(len(w_list)):
                for j in range(i, len(w_list)):
                    if (count[j] > count[i] or
                            (w_list[i] > w_list[j] and
                             count[j] == count[i])):
                        count[i], count[j] = count[j], count[i]
                        w_list[i], w_list[j] = w_list[j], w_list[i]

            # Print the results, excluding duplicates
            for i in range(len(w_list)):
                if count[i] > 0 and i not in skip_indices:
                    print("{}: {}".format(w_list[i].lower(), count[i]))
        else:
            # Recursive call to process the next page of data
            count_words(subreddit, w_list, next_page, count)

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
