# 🎵 Spotify Playlist Creator with Python

## Project Overview
This project automates the creation of a Spotify playlist based on the Billboard Hot 100 chart for a specified date. It combines web scraping and Spotify API integration to fetch song data and create a personalized playlist.

## Features
- **Web Scraping**: Utilizes BeautifulSoup to extract song names from the Billboard Hot 100 chart.
- **Spotify API Integration**: Uses Spotipy to authenticate with Spotify, search for songs, and create a playlist.
- **Error Handling**: Implements robust error handling to manage songs not found on Spotify.

## Prerequisites
- Python 3.x
- Spotify Developer Account
- Billboard Hot 100 URL

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spotify-playlist-creator.git
   cd spotify-playlist-creator
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   ```bash
   export USER_CLIENT_ID='your_spotify_client_id'
   export USER_CLIENT_SECRET='your_spotify_client_secret'
   export USER_URI='your_spotify_redirect_uri'
   ```

## Usage
Run the script:
```bash
python playlist_creator.py
```

Enter the desired date in the format YYYY-MM-DD when prompted.


## Code Explanation
### Web Scraping Billboard Hot 100
Prompts the user to input a date.
Sends a request to the Billboard Hot 100 chart page for that date.
Parses the HTML response using BeautifulSoup.
Extracts song names from the parsed HTML.

### Spotify API Integration
Authenticates with the Spotify API using OAuth credentials.
Retrieves the current user’s Spotify ID.
Searches Spotify for each song extracted from the Billboard chart.
Adds the found song URIs to a list.

### Creating and Populating the Playlist
Creates a new private playlist on Spotify named after the specified date.
Adds the collected song URIs to the newly created playlist.

## Key Learnings
➡️ Data Extraction: Enhanced skills in web scraping and data parsing.
➡️ Secure Authentication: Gained experience with OAuth for secure API access.
➡️ API Integration: Improved ability to work with third-party APIs, specifically for music streaming services.
