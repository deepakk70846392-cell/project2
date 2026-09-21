import os
import shutil


folder_path="/Users/deepakpal/Documents/cat2 ex.py"
files=os.listdir(folder_path)
for file in files:
  file_path=os.path.join(folder_path,file)
  if os.path.isdir(file_path):
    continue
  name, extension = os.path.splitext(file)
  if extension in [".jpg", ".png", ".jpeg"]:
        target_folder = "Images"
  elif extension in [".pdf", ".docx", ".txt"]:
        target_folder = "Documents"
  elif extension in [".mp3", ".wav"]:
        target_folder = "Music"
  else:
        target_folder = "Others"
  target_path = os.path.join(folder_path, target_folder)
  if not os.path.exists(target_path):
        os.makedirs(target_path)
        shutil.move(file_path, target_path)
  print(f"{file} ko {target_folder} mein bhej diya")