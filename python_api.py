# Python requests package
# Let's connect to live web using python requests api
# We will connect to www.bbc.com and check if the web is live

import requests

    response = requests.get("http://www.bbc.co.uk/")
    def __init__(self,):

    def check_status():
        if response: # the condition was True
            return ("success and the status code " + str(response.status_code))
        elif response:
             print("failure ")
        elif response:
            print("OOPs something went wrong")
    print(check_status())
# requests goes one step further in simplifying this process for us
# if you use response instance in a condition expression
# It will evaluation to True if the status code was between 200 and 400, False otherwise
# Therefore, you can simplify the last example by rewriting the if statement as above














# def status_code_chect():
# responses = requests.get("http://www.bbc.co.uk")
#
# if responses.status_code == 200:
#     print("The website is up and running status code is " + str(responses.status_code))
# else:
#     print("OOPs something went wrong " + str(responses.status_code))
#
# # status 200 which a success means the website is live running
# # status 400 or 404 means not working
#
# # create a function called status code check
# # function should return status code with appropriate message
# # DRY
