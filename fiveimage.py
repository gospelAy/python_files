from pathlib import Path
import shutil
new_dir = Path.home() / "my_folder"
# print(new_dir)
new_dir.mkdir(exist_ok=True)

file_1 = new_dir / "file1.txt"
file_2 = new_dir / "file2.txt"
image_1 = new_dir / "image1.png"

if not file_1.exists():
    file_1.touch()

if not file_2.exists():
    file_2.touch()

if not image_1.exists():
    image_1.touch()

images = new_dir / "images"
images.mkdir(exist_ok=True)

source = new_dir/"image1.png"
# print(source)
destination = new_dir/"images"/ "image1.png"
# print(destination)
if not destination.exists():
    source.replace(destination)

file_1.unlink()

shutil.rmtree(new_dir)