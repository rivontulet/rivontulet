import requests

API_KEY = 'f6f8bdceb51c4d90d4ae2424448d2a99'
USERNAME = 'digimon9999'

url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={USERNAME}&api_key={API_KEY}&format=json"

try:
    response = requests.get(url)
    data = response.json()

    track = data['recenttracks']['track'][0]
    track_name = track['name']
    artist_name = track['artist']['#text']
    album_name = track['album']['#text']

    content = (
        "[![Rivon profile views](https://u8views.com/api/v1/github/profiles/102215669/views/day-week-month-total-count.svg)]"
        "(https://u8views.com/github/rivontulet)\n\n"
        "# 🎧 Last Played Track\n\n"
        f"**Artist:** {artist_name}  \n"
        f"**Track:** {track_name}  \n"
        f"**Album:** {album_name}\n"
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ README.md updated successfully!")

except Exception as e:
    print("❌ Error fetching or writing track:", e)
