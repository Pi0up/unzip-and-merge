import os
import zipfile
import shutil
import argparse
import time
from datetime import datetime

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def is_newer(file1, file2):
    return os.path.getmtime(file1) > os.path.getmtime(file2)

def merge_directories(src, dest):
    folders_created = 0
    folders_merged = 0
    files_copied = 0

    for root, dirs, files in os.walk(src):
        rel_path = os.path.relpath(root, src)
        dest_path = os.path.join(dest, rel_path)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
            folders_created += 1
        else:
            folders_merged += 1

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_path, file)

            if os.path.exists(dest_file):
                if is_newer(src_file, dest_file):
                    shutil.copy2(src_file, dest_file)
                    files_copied += 1
            else:
                shutil.copy2(src_file, dest_file)
                files_copied += 1

    return folders_created, folders_merged, files_copied

def process_zip(zip_file, target_dir, tmp_dir):
    print(f"\n⏳ Traitement de : {zip_file}")
    extract_path = os.path.join(tmp_dir, os.path.splitext(os.path.basename(zip_file))[0])
    os.makedirs(extract_path, exist_ok=True)

    extract_zip(zip_file, extract_path)
    created, merged, copied = merge_directories(extract_path, target_dir)

    shutil.rmtree(extract_path)
    os.remove(zip_file)

    print(f"✅ Terminé : {zip_file}")
    print(f"   📁 Dossiers créés     : {created}")
    print(f"   🔁 Dossiers fusionnés : {merged}")
    print(f"   📄 Fichiers copiés     : {copied}")

def main():
    parser = argparse.ArgumentParser(description="Dézippe, fusionne et copie vers un dossier cible.")
    parser.add_argument("target", help="Dossier de destination")
    args = parser.parse_args()

    current_dir = os.getcwd()
    target_dir = os.path.abspath(args.target)
    tmp_dir = os.path.join(current_dir, "__temp_extract__")

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    os.makedirs(tmp_dir, exist_ok=True)

    print("👀 Surveillance du dossier en cours... Ctrl+C pour arrêter.\n")

    try:
        while True:
            zip_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.zip') and os.path.isfile(f)]
            if zip_files:
                for zip_file in zip_files:
                    process_zip(zip_file, target_dir, tmp_dir)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Arrêt du script demandé. Nettoyage...")
        shutil.rmtree(tmp_dir, ignore_errors=True)
        print("✅ Terminé.")

if __name__ == "__main__":
    main()
