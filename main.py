import json
from watson_developer_cloud import PersonalityInsightsV3
import pprint



personality_insights = PersonalityInsightsV3(
    version = '2017-10-13',
    username = '0ab3e944-620a-4f2f-a2ee-6257e27f44a7',
    password = 'MoFUXg2mfhcb'
)




def main():

    with open('infile.txt', 'r') as infile:
        text = infile.read()

    profile = personality_insights.profile(text, content_type='text/plain')


    with open('outfile.json', 'w+') as outfile:
        outfile.write(json.dumps(profile, indent = 4, sort_keys = True))





if __name__ == '__main__':
    main()
