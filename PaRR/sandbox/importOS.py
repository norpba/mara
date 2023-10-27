import os
import shutil
from pathlib import Path
dst_directory = r"C:\Users\norppa\myCode\mara\PaRR\sandbox\output"

os.makedirs(dst_directory, exist_ok=True)
dst = os.path.join(dst_directory, "test.txt")

src = Path(r"C:\Users\norppa\myCode\mara\PaRR\sandbox\file_src\test.txt")

shutil.copyfile(src, dst)