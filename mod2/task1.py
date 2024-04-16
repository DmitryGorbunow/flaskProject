from flask import Flask
import requests
from concurrent.futures import ThreadPoolExecutor
path = "../files/output_file.txt"


def get_summary_rss(file_path):
    total_memory = 0

    with open(file_path, 'r') as file:
        next(file)

        for line in file:
            parts = line.split()

            rss = int(parts[5])
            total_memory += rss

    return convert_kb_to_mb_gb(total_memory)


def convert_kb_to_mb_gb(kb):
    mb = kb / 1024
    gb = mb / 1024

    if gb >= 1:
        return f"{gb:.2f} GB"
    elif mb >= 1:
        return f"{mb:.2f} MB"
    else:
        return f"{kb} KB"

def fetch_cat_fact(url):
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        cat_fact = data["fact"]
        print(cat_fact)
    else:
        print("Failed to fetch cat fact")

def get_cat_facts():
    url = "https://catfact.ninja/fact"
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(fetch_cat_fact, url) for _ in range(20)]
        for future in futures:
            future.result()


if __name__ == '__main__':
    get_cat_facts()
    # print(get_summary_rss(path))
