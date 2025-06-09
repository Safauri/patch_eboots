import sys

def main(filename, old, new):
    try:
        with open(filename, "rb+") as f:
            data = f.read()
            if (index := data.find(old.encode())) == -1:
                return
            f.seek(index)
            f.write(new.encode().ljust(len(old), b"\x00"))
            print(f"Renamed '{old}' to '{new}' at 0x{index:X}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide an ELF file.")
    else:
        for old, new in [("ros.rockstargames.com", "ros.gtao.me"), ("https://", "http://"), ("cyprusv.se", "ros.gtao.me")]:
            main(sys.argv[1], old, new)

    input("\nPress Enter to exit...")