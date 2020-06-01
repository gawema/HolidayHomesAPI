import requests
import json

def scrape(profile):
	instagram_url = 'https://www.instagram.com'
	profile_url = profile
	last_3_posts = []

	response = requests.get(f"{instagram_url}/{profile_url}/?__a=1")
	if response.ok:
		try:
			json_data = json.loads(response.text)
			post_list = json_data['graphql']['user']['edge_owner_to_timeline_media']['edges']
			for i in range(3):
				last_3_posts.append(post_list[i]['node']['shortcode'])
		except (requests.exceptions.ConnectionError, ValueError):
			last_3_posts = [
				"CAzR-nvppNV",
				"CAu1hZ-JFfY",
				"CAqDicnBmwV"
				]
		return(json.dumps(last_3_posts))
	return []
	