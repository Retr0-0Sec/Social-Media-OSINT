import requests
from concurrent.futures import ThreadPoolExecutor
import pyfiglet

# User-Agent to prevent blocks from some platforms
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Function to check social media profiles
def check_platform(platform, url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            return f"[FOUND] {platform}: {url}"
        elif response.status_code == 404:
            return f"[NOT FOUND] {platform}: {url}"
        else:
            return f"[UNKNOWN] {platform}: Status Code {response.status_code}"
    except requests.RequestException as e:
        return f"[ERROR] {platform}: {e}"

# Main function to check all platforms
def check_social_media(username):
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "GitHub": f"https://github.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "YouTube": f"https://www.youtube.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Medium": f"https://medium.com/@{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Goodreads": f"https://www.goodreads.com/user/show/{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Behance": f"https://www.behance.net/{username}",
        "Bandcamp": f"https://{username}.bandcamp.com",
        "Patreon": f"https://www.patreon.com/{username}",
        "Kickstarter": f"https://www.kickstarter.com/profile/{username}",
        "Slack": f"https://{username}.slack.com",
        "Stack Overflow": f"https://stackoverflow.com/users/{username}",
    }

    # Print ASCII Art
    ascii_art = pyfiglet.figlet_format("Social Media Checker", font="slant")
    print(f"\033[1;32m{ascii_art}\033[0m")

    print(f"Social Media Checker\n")
    print(f"Enter the username to check: {username}\n")
    print(f"Checking social media profiles for username: {username}\n")

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda p: check_platform(p[0], p[1]), platforms.items())
    
    for result in results:
        if "FOUND" in result:
            print(f"\033[1;32m{result}\033[0m")
        elif "NOT FOUND" in result:
            print(f"\033[1;31m{result}\033[0m")
        elif "ERROR" in result:
            print(f"\033[1;33m{result}\033[0m")
        else:
            print(f"\033[1;34m{result}\033[0m")

# Replace 'your_username' with the username to check
username_to_check = input("Enter the username to check: ")
check_social_media(username_to_check)
