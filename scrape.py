import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def is_valid_url(url, base_url):
    """Check if the URL is within the same domain as the base URL."""
    return urlparse(url).netloc == urlparse(base_url).netloc

def scrape_page(url, visited):
    """Scrape a single page and return its content and new links."""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text(separator=" ", strip=True)
        
        # Find all links on the page
        links = soup.find_all('a', href=True)
        new_links = [urljoin(url, link['href']) for link in links 
                     if is_valid_url(urljoin(url, link['href']), url)]
        
        # Only return links that haven't been visited
        new_links = [link for link in new_links if link not in visited]
        
        return content, new_links
    except requests.RequestException as e:
        print(f"Error scraping {url}: {e}")
        return "", []

def scrape_website(start_url, file_path):
    """Scrape entire website starting from start_url."""
    visited = set()
    to_visit = [start_url]
    all_content = ""

    while to_visit:
        url = to_visit.pop(0)
        if url not in visited:
            print(f"Scraping: {url}")
            content, new_links = scrape_page(url, visited)
            all_content += content + "\n\n"
            visited.add(url)
            to_visit.extend(new_links)

    # Save the content to a file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(all_content)

    return all_content

# Directory and file path where the content will be saved

file_path = os.path.join("scraped.txt")

# Scrape the website content and save it to the file
start_url = "https://preferhub.com" #change to the desired URL
website_content = scrape_website(start_url, file_path)

# Print the file path for verification
print(f"Content saved to {file_path}") 