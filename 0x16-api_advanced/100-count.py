#!/usr/bin/python3
"""Reddit API word counter"""

import requests


def count_words(subreddit, words_list, next_page="", counts=[]):
    """Counts occurrences of words in the titles of hot posts in a subreddit."""
    
    # Initialize the counts list on the first call
    if next_page == "":
        counts = [0] * len(words_list)

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
                        counts[i] += 1

        # Update the next_page variable with the 'after' value for pagination
        next_page = data['data']['after']
        if next_page is None:
            skip_indices = []
            # Combine counts for duplicate words and sort results
            for i in range(len(words_list)):
                for j in range(i + 1, len(words_list)):
                    if words_list[i].lower() == words_list[j].lower():
                        skip_indices.append(j)
                        counts[i] += counts[j]

            # Sort words by count and alphabetically if counts are equal
            for i in range(len(words_list)):
                for j in range(i, len(words_list)):
                    if (counts[j] > counts[i] or
                            (words_list[i] > words_list[j] and
                             counts[j] == counts[i])):
                        counts[i], counts[j] = counts[j], counts[i]
                        words_list[i], words_list[j] = words_list[j], words_list[i]

            # Print the results, excluding duplicates
            for i in range(len(words_list)):
                if counts[i] > 0 and i not in skip_indices:
                    print("{}: {}".format(words_list[i].lower(), counts[i]))
        else:
            # Recursive call to process the next page of data
            count_words(subreddit, words_list, next_page, counts)

# Example usage
# count_words("programming", ["python", "java", "javascript"])
