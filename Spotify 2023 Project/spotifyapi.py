import requests
import pandas as pd
import time
import os

# -------------------------------
# Spotify API credentials
# -------------------------------
client_id = 'c14e32fefa4e4fd28287a319c67a6dcc'
client_secret = 'c9091925810e42ddb1ee94a5993a035e'

# -------------------------------
# Functions
# -------------------------------
def get_spotify_token(client_id, client_secret):
    """Get Spotify access token using client credentials."""
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_data = auth_response.json()
    return auth_data.get('access_token')


def search_track(track_name, artist_name, token):
    """Search Spotify for a track and return its ID."""
    query = f"{track_name} artist:{artist_name}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    if response.status_code != 200:
        print(f"  → Error {response.status_code} for track '{track_name}'")
        return None
    json_data = response.json()
    try:
        first_result = json_data['tracks']['items'][0]
        return first_result['id']
    except (KeyError, IndexError):
        return None


def get_track_details(track_id, token):
    """Get album cover URL for a given track ID."""
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    if response.status_code != 200:
        return None
    json_data = response.json()
    try:
        return json_data['album']['images'][0]['url']
    except (KeyError, IndexError):
        return None


# -------------------------------
# Load CSV
# -------------------------------
csv_path = r"C:\Users\Z One\Desktop\PowerBI-Projects\Spotify 2023 Project\spotify-2023.csv"

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV file not found: {csv_path}")

df_spotify = pd.read_csv(csv_path, encoding='ISO-8859-1')

# -------------------------------
# Normalize column names
# -------------------------------
df_spotify.columns = df_spotify.columns.str.strip().str.lower()  # strip spaces, lowercase
if 'track' in " ".join(df_spotify.columns):
    track_col = [c for c in df_spotify.columns if 'track' in c][0]
else:
    raise KeyError("No track column found")
if 'artist' in " ".join(df_spotify.columns):
    artist_col = [c for c in df_spotify.columns if 'artist' in c][0]
else:
    raise KeyError("No artist column found")

df_spotify.rename(columns={track_col: 'track_name', artist_col: 'artist_name'}, inplace=True)

# -------------------------------
# Clean track and artist names
# -------------------------------
df_spotify['track_name'] = df_spotify['track_name'].astype(str).str.strip().str.replace("'", "", regex=False)
df_spotify['artist_name'] = df_spotify['artist_name'].astype(str).str.strip().str.replace("'", "", regex=False)
df_spotify['artist_name'] = df_spotify['artist_name'].str.replace(',', ' ')  # Replace commas for multiple artists

# Add image_url column if not exists
if 'image_url' not in df_spotify.columns:
    df_spotify['image_url'] = ''

# -------------------------------
# Get Spotify access token
# -------------------------------
access_token = get_spotify_token(client_id, client_secret)
if not access_token:
    raise RuntimeError("Failed to get Spotify access token.")

# -------------------------------
# Loop through rows and fetch album covers
# -------------------------------
for i, row in df_spotify.iterrows():
    track = row['track_name']
    artist = row['artist_name']
    print(f"Processing {i+1}/{len(df_spotify)}: '{track}' by {artist}")

    track_id = search_track(track, artist, access_token)
    if track_id:
        image_url = get_track_details(track_id, access_token)
        df_spotify.at[i, 'image_url'] = image_url
        print(f"  → Found cover URL")
    else:
        print(f"  → Track not found on Spotify.")

    time.sleep(0.1)  # Small delay to avoid API rate limits

# -------------------------------
# Save updated CSV
# -------------------------------
output_path = r"C:\Users\Z One\Desktop\PowerBI-Projects\Spotify 2023 Project\spotify-2023-updated.csv"
df_spotify.to_csv(output_path, index=False, encoding='utf-8')
print(f"\n✅ Updated CSV saved to: {output_path}")
