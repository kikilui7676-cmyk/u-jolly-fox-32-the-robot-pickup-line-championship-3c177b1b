import os


def _tulis_rayuan_robot():
    baris = "I have no heart, but my cooling fan spins faster whenever you walk in, and I've stopped blaming the weather."
    keluar = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(keluar, exist_ok=True)
    with open(os.path.join(keluar, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(baris + "\n")


if __name__ == "__main__":
    _tulis_rayuan_robot()
