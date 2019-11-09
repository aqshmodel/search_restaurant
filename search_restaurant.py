import requests

def search_restaurant(access_key, free_word, result_number):
    response = requests.get(
        f'https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid={access_key}&freeword={free_word}&hit_per_page={result_number}')
    results = response.json()
    for i in range(0, len(results['rest'])):
        print('■ ' + results['rest'][i]['name'])
        print(results['rest'][i]['url'])
        line_name = results['rest'][i]['access']['line']
        station_name = results['rest'][i]['access']['station']
        time_on_foot = results['rest'][i]['access']['walk']
        print(f'{line_name} {station_name} {time_on_foot}分\n')
