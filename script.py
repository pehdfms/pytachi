import math
import os

def pad_by_count(length, n):
    size = int(math.log10(length) + 1)
    return str(n).zfill(size)

def sort_images(title, path):
    images = os.listdir(path)
    length = len(images)
    for idx, image in enumerate(images):
        old_path = os.path.join(path, image)
        _, extension = os.path.splitext(old_path)

        new_path = os.path.join(path, f"{title} - {pad_by_count(length, idx+1)}{extension}")
        os.rename(old_path, new_path)

def separate_chapters(title, chapters, offset):
    base_path = "images"
    images = os.listdir(base_path)

    chapters.append(len(images)+1)

    last = 0
    for idx, chapter in enumerate(chapters):
        new_dir = f"{title} - 【第{idx+offset+1}話】"

        try:
            os.mkdir(new_dir)
        except OSError as error:
            pass

        chapter_images = images[last:chapter-1]

        for idx, image in enumerate(chapter_images):
            old_path = os.path.join(base_path, image)
            new_path = os.path.join(new_dir, image)

            os.rename(old_path, new_path)

        sort_images(title, new_dir)
        last = chapter-1


def main(title, chapters, offset):
    sort_images(title, "images")
    separate_chapters(title, chapters, offset)
    pass

if __name__ == '__main__':
    title = "上野さんは不器用"
    chapters = [17, 31, 45, 59, 73, 87, 101, 115, 129]
    offset = 0
    main(title, chapters, offset)
