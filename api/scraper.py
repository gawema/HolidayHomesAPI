import requests
import json

def scrape(profile):
	instagram_url = 'https://www.instagram.com'
	profile_url = profile
	last_3_posts = []

	response = requests.get(f"{instagram_url}/{profile_url}/?__a=1")
	if response.ok:
		html = response.text
		json_data = json.loads(html)
		post_list = json_data['graphql']['user']['edge_owner_to_timeline_media']['edges']
		for x in range(3):
			last_3_posts.append(post_list[x]['node']['shortcode'])
		return(json.dumps(last_3_posts))
	return []