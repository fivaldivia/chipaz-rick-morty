import requests

def count_letters_in_name(url, letter_to_find, resource):
    response = requests.get(url).json()
    total_pages = response['info']['pages']
    total_letters_in_names = 0
    for page in range(1,total_pages+1):
        page_url = url+'/?page='+str(page)
        results_list = requests.get(page_url).json()['results']
        for item in results_list:
            total_letters_in_names += item['name'].lower().count(letter_to_find)
    return {
                "char": letter_to_find,
                "count": total_letters_in_names,
                "resource": resource
            }