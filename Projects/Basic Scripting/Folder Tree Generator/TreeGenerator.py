from pathlib import Path


def generate(location, prefix=""):
    path = Path(location)

    try:
        items = sorted(
            [i for i in path.iterdir() if not i.name.startswith(".")],
            key=lambda x: (not x.is_dir(), x.name.lower()),
        )
        count = len(items)

        for index, item in enumerate(items):

            is_last = index == count - 1
            connector = "└── " if is_last else "├── "

            if item.is_file():
                print(f"{prefix}{connector}{item.name}")

            elif item.is_dir():
                print(f"{prefix}{connector}{item.name}/")
                generate(item, prefix + ("    " if is_last else "│   "))

    except PermissionError:
        print(f"{prefix}└── [Access Denied]")

    except Exception:
        pass


if __name__ == "__main__":
    root = Path("/Users/anthonylumantao/Downloads/file")
    print(root.name + "/")
    generate(root)
