
import requests
import json

class GetJokes:
  def get_jokes(self):
    URL = "https://official-joke-api.appspot.com/jokes/programming/ten"

    response = requests.get(URL)
    return response.content
  
  def jokes(self):
    jokes_list = []
    jokes = json.loads(self.get_jokes())

    for joke in jokes:
      jokes_list.append(f'{joke["setup"]} {joke["punchline"]}')
    
    return jokes_list 

jokes = GetJokes()
jokes_list_lines = jokes.jokes()

for joke in jokes_list_lines:
  print(joke)

# So far we've used the requests to send a request for data to an API endpoint, a URL. 
# We've operated on the data that was returned to us, making sure it was formatted properly as JSON and iterating over that JSON to 
# retrieve the name of the school hosting each after-school program. 
# That was a lot of work! I wonder if there is an easier way to work with popular APIs...
# Let's check it out on the next session...