from pathlib import Path

def main():

    try:
        path = Path("/Users/anthonylumantao/Desktop")

        for item in path.iterdir():
            if item.is_file():
                if item.name.startswith("Screenshot"):
                    item.unlink()


    except Exception as e:
        print(path.exists())
        print(path.is_dir())
        print(e)


if __name__ == "__main__":
    main()