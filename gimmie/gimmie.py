#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

def fetch_text_from_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    text = soup.get_text(separator='\n')
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    marker = "(Transcription below image)"
    index = next((i for i, line in enumerate(lines) if marker in line), None)
    if index is not None:
        lines = lines[index + 1:]
    else:
        print(f"Marker '{marker}' not found in the text.")

    stop_indices = [i for i, line in enumerate(lines) if line in {'1', '2', '3'}]
    if stop_indices:
        first_stop = min(stop_indices)
        lines = lines[:first_stop]

    prev_index = next((i for i, line in enumerate(lines) if line == "Previous"), None)
    if prev_index is not None:
        for j in range(1, 11):
            if prev_index + j < len(lines) and "London 1915-16" in lines[prev_index + j]:
                lines = lines[:prev_index]
                break

    one_line_text = ' '.join(lines).rstrip(" Previous")
    return f'"{one_line_text}"'

def fetch_and_save_multiple_pages(root_url, num_pages, filename, header):
    all_texts = []

    for i in range(1, num_pages + 1):
        if i == 1:
            url = root_url
        else:
            url = f"{root_url.rstrip('/')}/page/{i}/"

        print(f"Fetching: {url}")
        text = fetch_text_from_page(url)
        if text:
            all_texts.append(f'"{header}{i:03}": {text}')

    final_text = ', '.join(all_texts)

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(final_text)
        print(f"Text saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    root_url = input("Enter the root URL of the webpage: ")
    num_pages = int(input("Enter the number of pages to fetch: "))
    filename = input("Enter the output filename (e.g., output.txt): ")
    header = input("Enter the header (as an index for JSON): ")
    fetch_and_save_multiple_pages(root_url, num_pages, filename, header)
