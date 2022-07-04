import time
from functions.count_letters import count_letters_in_name

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
        
if __name__ == "__main__":
    main()