from pathlib import Path


def main():
    path = Path("/Users/anthonylumantao/Downloads")
    existing = {item.name for item in path.iterdir() if item.is_dir()}

    directories = ["Documents", "Images", "Videos", "Activities", "Programs", "audio", "Activities"]

    for d in directories:
        if d not in existing:
            (path / d).mkdir()

    for item in path.iterdir():
        if item.is_file():
            if item.name.endswith(
                (".docx" , ".pdf", ".xlsx", ".pptx", ".csv", ".gz")):
                    item.move(Path("/Users/anthonylumantao/Downloads/Documents") / item.name)
            elif item.name.endswith((".py", ".java", ".ino")):
                item.move(Path("/Users/anthonylumantao/Downloads/Programs") / item.name)
            elif item.name.endswith((".wav", ".mp3", ".m4a")):
                item.move(Path("/Users/anthonylumantao/Downloads/audio") / item.name)
            elif item.name.startswith(("Screenshots")) or item.name.endswith((".gif", ".png", ".jpg", ".jpeg")):
                item.move(Path("/Users/anthonylumantao/Downloads/Images") / item.name)
            elif item.name.endswith((".drawio", ".aep", ".pkt", ".zip", "md", ".piskel")):
                item.move(Path("/Users/anthonylumantao/Downloads/Activities") / item.name)
            else:
                item.unlink()



if __name__ == '__main__':
    main()