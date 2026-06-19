from pathlib import Path

file = []


def sizeAnalyzer(location):

    path = Path(location)

    items = sorted(
        [
            i
            for i in path.iterdir()
            if not i.name.startswith((".", "Sparkle"))
        ],
        key=lambda x: (not x.is_dir(), x.name.lower()),
    )

    for item in items:
        if item.is_file():
            if not item.name.endswith((".string", ".strings", ".plist")):
                file.append((item.name, item.stat().st_size))

        elif item.is_dir():
            sizeAnalyzer(item)

def humanSize(size_bytes):
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"


if __name__ == "__main__":
    sizeAnalyzer("/Users/anthonylumantao/Downloads/")
    for index, (name, size) in enumerate(sorted(file, key=lambda x: x[1]), start=1):
        print(f"{index}. {name}: {humanSize(size)}")
