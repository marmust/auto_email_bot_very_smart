# imports
import openai
# imports

# api keys
openai.api_key = ur api key
# api keys

# variable definition
yourCompanyName = "FoxTech"
targetCompanyName = "US governament"

yourProductSpecialization = "fox manufacturing machines"
targetProductSpecialization = "not repaying national dept"

yourCompanyContacts = "gmail: giveMe50$@FoxTech.com"
# variable definition

# input construction
input = "my company's name is " + yourCompanyName + ", ask the clients to contact me here: " + yourCompanyContacts + ", there is a company which specializes in " + targetProductSpecialization + "their name is: " + targetCompanyName + ". write an email to " + targetCompanyName + "proposing them my product which can " + yourProductSpecialization
# input construction

# gpt3
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=input,
  temperature=0.9,
  max_tokens=220,
  top_p=0.9,
  frequency_penalty=1,
  presence_penalty=1
)
email = response.get('choices')[0].to_dict()['text']
# gpt3

print(email)