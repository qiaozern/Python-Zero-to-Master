"""
Issue
We've got some buggy code, try running the code. The code will crash and give you a KeyError. 
This is because some of the posts in the facebook_posts don't have any "Likes".

Bad Output
NameError: name 'facebook_posts' is not defined.

Instructions
Use what you've learnt about exception handling to prevent the program from crashing.
"""

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_like = 0

for post in facebook_posts:
    try:
        total_like = total_like + post['Likes']
    except KeyError:
        pass
        # total_like +=  0



print(total_like)