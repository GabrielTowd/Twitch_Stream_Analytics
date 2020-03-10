import json
import requests
import datetime

api_token = 'ek4ezzhg4t9m6t4wx3weml4s86cyz7'
api_url_base = 'https://api.twitch.tv/helix'
api_header = {'Content-Type': 'application/json',
           'Client-ID': api_token}

def get_game_id(game):
    response = requests.get(api_url_base + '/games?name=' + game, headers=api_header)
    if response.status_code == 200: 
        return json.loads(response.content.decode('utf-8'))['data'][0]['id']
    else :
        return None

def get_streams_datas(game_id):
    response = requests.get(api_url_base + '/streams?game_id=' + game_id, headers=api_header)
    if response.status_code == 200: 
        streams = json.loads(response.content.decode('utf-8'))['data']
    else :
        return None

    views_count = 0
    top_twenty = []
    streamer_count = len(streams)

    for stream in streams:
        count = 0
        views_count += stream['viewer_count']

        if count < 20: 
            count += 1
            top_streamer = {
                "user_id": stream['user_id'],
                "user_name": stream['user_name'],
                "viewer_count": stream['viewer_count'],
                "started_at": stream['started_at']
            }
            top_twenty.append(top_streamer)
    
    data = {
        "view_count": view_count,
        "top_twenty": top_twenty,
        "streamer_count": streamer_count
    }

    date = datetime.datetime.now()

    with open(date + ////game////, 'w') as write_file:
        json.dump(data, write_file)


game_id = get_game_id("Dofus")
get_streams_datas(game_id)