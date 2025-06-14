import sys

def main(filename, replacements):
    try:
        with open(filename, "rb+") as f:
            data = f.read()

            for old, new in replacements:
                old_bytes, new_bytes = old.encode() + b"\x00", new.encode().ljust(len(old) + 1, b"\x00")
                offset = 0

                while (index := data.find(old_bytes, offset)) != -1:
                    print(f"[+] Patched: {old} → {new} @ 0x{index:X}")
                    f.seek(index)
                    f.write(new_bytes)
                    offset = index + len(old_bytes)  # Move past current occurrence

        print("\n[✓] Patch complete.")

    except Exception as e:
        print(f"[!] Error: {e}")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] Drag and drop an ELF file onto this script.")
    else:
        main(sys.argv[1], [
            ("ros.rockstargames.com", "ros.gtao.me"),
            ("https://", "http://") # 2 checks
        ])
