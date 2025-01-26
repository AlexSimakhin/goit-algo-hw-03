"""task1.py"""
import argparse
import shutil
from pathlib import Path

def parse_argv():
    # Створюємо парсер для аргументів командного рядка
    parser = argparse.ArgumentParser(description="Сортування файлів")
    parser.add_argument(
        "-S", "--source", type=Path, required=True, help="Джерело (каталог)"
    )
    parser.add_argument(
        "-O",
        "--output",
        type=Path,
        default=Path("dist"),
        help="Каталог призначення (за замовчуванням: dist)",
    )
    return parser.parse_args()

def create_test_files(base_dir: Path, num_files_per_dir: int = 5):
    base_dir.mkdir(parents=True, exist_ok=True)

    sub_dirs = ['docs', 'images', 'videos']
    file_extensions = {
        'docs': 'txt',
        'images': 'jpg',
        'videos': 'mp4'
    }

    for sub_dir in sub_dirs:
        current_dir = base_dir / sub_dir
        current_dir.mkdir(parents=True, exist_ok=True)

        for i in range(num_files_per_dir):
            file_name = f"test_file_{i + 1}.{file_extensions[sub_dir]}"
            file_path = current_dir / file_name

            with file_path.open('w', encoding='utf-8') as f:
                f.write(f"Це тестовий файл {file_name} у каталозі {sub_dir}.")

    print(f"Тестові файли створені в {base_dir}")

def recursive_copy(src: Path, dst: Path):
    try:
        # Рекурсивно копіюємо файли з джерела в призначення
        for item in src.iterdir():
            if item.is_dir():
                # Якщо елемент - каталог, викликаємо функцію рекурсивно
                recursive_copy(item, dst)
            else:
                # Копіюємо файл в каталог, що відповідає його розширенню
                file_extension = item.suffix.lower()[1:]
                folder = dst / file_extension
                folder.mkdir(parents=True, exist_ok=True)
                dest_file = folder / item.name
                print(f"Копіювання {item} до {dest_file}")
                shutil.copy2(item, dest_file)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Сталася помилка: {e}")

def main():
    # Головна функція програми
    args = parse_argv()
    print(f"Джерело: {args.source}, Вихід: {args.output}")

    if not args.source.exists() or not args.source.is_dir():
        # Якщо каталог джерела не існує, створюємо його та генеруємо тестові файли
        print(
            f"Каталог джерела '{args.source}' не існує або не є каталогом.\nСтворення каталогу джерела та генерація тестових файлів..."
        )
        args.source.mkdir(parents=True, exist_ok=True)
        create_test_files(args.source)
    else:
        # Якщо каталог джерела існує, генеруємо тестові файли
        create_test_files(args.source)

    try:
        # Створюємо каталог призначення, якщо його ще немає
        args.output.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Не вдалося створити каталог виходу: {e}")
        return

    # Копіюємо файли
    recursive_copy(args.source, args.output)
    print(f"Файли успішно скопійовано в {args.output}")


if __name__ == "__main__":
    main()

# python task1.py -S test -O new
