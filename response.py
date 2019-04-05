import requests
import json

app_id = '982812a1'
app_key = '75cbf611efa97cd128b405705647add4'

language = 'en'
word_id = 'Variance'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower() + '/synonyms;antonyms'

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

synonyms = r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
related_word_list = []

for i in synonyms:
    related_word_list.append(i['text'])

print(related_word_list)

# print("code {}\n".format(r.status_code))
# print()
# print("json \n" + json.dumps(r.json()))