import time
from functions.count_letters import count_letters_in_name
import requests


def main():
    results = []
    ### First exercise ###
    results_char_counter = []
    # Start counting execution time
    start_time = time.time()
    # Count letters
    results_location = count_letters_in_name('https://rickandmortyapi.com/api/location','l', 'location')
    results_episode = count_letters_in_name('https://rickandmortyapi.com/api/episode','e', 'episode')
    results_characters = count_letters_in_name('https://rickandmortyapi.com/api/character','c', 'character')
    # Add results
    results_char_counter.append(results_location)
    results_char_counter.append( results_episode)
    results_char_counter.append(results_characters)
    # Get execution time
    execution_time = time.time() - start_time
    # Generate json and add to results
    in_time = True if execution_time<=3 else False
    char_counter_json = { "exercise_name": "Char counter","time": execution_time,
        "in_time": in_time,"results":results_char_counter}
    results.append(char_counter_json)

    ### Second exercise ###
    # Start counting execution time
    start_time = time.time()
    ##
    response = requests.get('https://rickandmortyapi.com/api/episode').json()
    total_pages = response['info']['pages']
    results_episode_locations = []
    for page in range(1,total_pages+1):
        page_url = 'https://rickandmortyapi.com/api/episode'+'/?page='+str(page)
        results_list = requests.get(page_url).json()['results']
        for item in results_list:
            locations = []
            for character_url in item['characters']:
                character_location = requests.get(character_url).json()['location']['name']
                if character_location not in locations:
                    locations.append(character_location)
            episode_result = {"name": item['name'],
                    "episode": item['episode'],
                    "locations": locations}
            results_episode_locations.append(episode_result)
    # Get execution time
    execution_time = time.time() - start_time
    # Generate json and add to results
    in_time = True if execution_time<=3 else False
    episode_locations_json = { "exercise_name": "Episode locations","time": execution_time,
        "in_time": in_time,"results":results_episode_locations}
    results.append(episode_locations_json) 
       
if __name__ == "__main__":
    main()