# OSINT Social Media Checker

This script checks the availability of social media profiles based on a provided username. It uses multiple platforms such as Instagram, Twitter, Facebook, Reddit, GitHub, YouTube, and many more to determine if the username is taken, available, or if any issues arise (such as SSL certificate errors or redirects).

## Features

- Checks for multiple social media platforms (Instagram, Twitter, Facebook, Reddit, GitHub, etc.).
- Uses multi-threading for fast parallel checks.
- Prints the status of each platform (Found, Not Found, Error, or Unknown).
- Customizable for additional social media platforms or different usernames.

## Platforms Checked

- Instagram
- Twitter
- Facebook
- TikTok
- Reddit
- GitHub
- LinkedIn
- YouTube
- Snapchat
- Pinterest
- Tumblr
- Medium
- DeviantArt
- Twitch
- Steam
- Dribbble
- Vimeo
- Flickr
- SoundCloud
- Spotify
- Goodreads
- Quora
- WordPress
- Behance
- Bandcamp
- Patreon
- Kickstarter
- Slack
- Stack Overflow

## Requirements

- Python 3.x
- Requests library (`pip install requests`)
- `concurrent.futures` (comes with Python standard library)

## How to Use

1. Clone the repository:
    ```bash
    git clone (https://github.com/Retr0-0Sec/Social-Media-OSINT.git)
    cd OSINT.py
    ```

2. Install the required dependencies (if not already installed):
    ```bash
    pip install requests
    ```

3. Run the script:
    ```bash
    python OSINT.py
    ```

4. Enter the username you wish to check when prompted.

    Example output:
    ```bash
    Checking social media profiles for username: username123

    [FOUND] Instagram: https://www.instagram.com/username123
    [UNKNOWN] Facebook: Status Code 400
    [FOUND] Reddit: https://www.reddit.com/user/username123
    [ERROR] Tumblr: SSL certificate error
    [NOT FOUND] YouTube: https://www.youtube.com/username123
    ```

## Example Usage

```bash
Enter the username to check: username123
