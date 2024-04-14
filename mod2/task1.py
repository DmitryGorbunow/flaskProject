from flask import Flask

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


if __name__ == '__main__':
    print(get_summary_rss(path))
