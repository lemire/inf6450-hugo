#!/usr/bin/env python3
"""
Script to check for broken links in Markdown files.
Usage: python check_links.py <directory>
"""

import os
import re
import sys
import requests
from urllib.parse import urlparse
from pathlib import Path
import concurrent.futures

# Cache for URL checks
url_cache = {}
session = requests.Session()

def check_url(url, timeout=10):
    """Check if URL is reachable."""
    if url in url_cache:
        print("in cache")
        return url_cache[url]
    try:
        response = session.head(url, timeout=timeout, allow_redirects=True)
        result = response.status_code < 400
        url_cache[url] = result
        return result
    except requests.RequestException:
        url_cache[url] = False
        return False

def find_links(content):
    """Find all Markdown and HTML links in the content."""
    links = []
    
    # Markdown links: [text](url)
    md_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    md_links = re.findall(md_pattern, content)
    for text, url in md_links:
        links.append(('markdown', text, url))
    
    # HTML href links: href="url"
    html_pattern = r'href="([^"]+)"'
    html_links = re.findall(html_pattern, content)
    for url in html_links:
        links.append(('html', '', url))
    
    return links

def is_url(link):
    """Check if link is a URL (http/https)."""
    parsed = urlparse(link)
    return parsed.scheme in ('http', 'https')

def check_local_file(filepath, base_dir):
    """Check if local file exists, resolving relative paths."""
    if os.path.isabs(filepath):
        return os.path.exists(filepath)
    else:
        # Assume relative to base_dir
        full_path = os.path.join(base_dir, filepath)
        return os.path.exists(full_path)

def check_links_in_file(filepath, base_dir):
    """Check all links in a Markdown file."""
    broken_links = []
    links = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        links = find_links(content)
        urls_to_check = set()
        local_links = []
        
        for link_type, text, link in links:
            if is_url(link):
                urls_to_check.add(link)
            else:
                local_links.append((link_type, text, link))
        
        # Check URLs in parallel
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            url_results = {url: executor.submit(check_url, url) for url in urls_to_check}
            for url, future in url_results.items():
                url_cache[url] = future.result()
        
        # Now check all links
        for link_type, text, link in links:
            if is_url(link):
                if not url_cache[link]:
                    if link_type == 'markdown':
                        broken_links.append(f"Broken URL: [{text}]({link})")
                    else:
                        broken_links.append(f"Broken href URL: {link}")
            else:
                # Local file
                if not check_local_file(link, base_dir):
                    if link_type == 'markdown':
                        broken_links.append(f"Broken local file: [{text}]({link})")
                    else:
                        broken_links.append(f"Broken href local file: {link}")
    except Exception as e:
        broken_links.append(f"Error reading file: {e}")
    
    return broken_links, len(links)

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_links.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory")
        sys.exit(1)
    
    # Find all .md files
    md_files = list(Path(directory).rglob('*.md'))
    
    if not md_files:
        print("No Markdown files found.")
        return
    
    total_broken = 0
    total_links = 0
    
    for md_file in md_files:
        broken_links, num_links = check_links_in_file(str(md_file), directory)
        total_links += num_links
        if broken_links:
            print(f"\n{md_file}:")
            for link in broken_links:
                print(f"  {link}")
            total_broken += len(broken_links)
    
    if total_broken == 0:
        print("No broken links found!")
    else:
        print(f"\nTotal broken links: {total_broken}")
    
    print(f"Total links checked: {total_links}")

if __name__ == "__main__":
    main()