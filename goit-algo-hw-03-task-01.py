from pathlib import Path
import shutil
import argparse

def copy_files_recursive(src_dir, dest_dir):
    try:
        src_path = Path(src_dir)
        dest_path = Path(dest_dir)
    
        if not src_path.exists():
            print(f"Директорії {src_path} не існує.")
            return
    
        for item in src_path.iterdir():
            if item.is_dir():
                copy_files_recursive(item, dest_path)
            else:
                file_extension = item.suffix[1:].lower() or "no_extension"
                dest_subdir = dest_path / file_extension
                dest_subdir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, dest_subdir)
                print(f"Скопійовано {item} до {dest_subdir}")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Помилка при обробці {src_dir}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Рекурсивно копіювати файли та сортувати за розширенням.')
    parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення (за замовчуванням dist)')
    args = parser.parse_args()

    copy_files_recursive(args.src_dir, args.dest_dir)

if __name__ == "__main__":
    main()
