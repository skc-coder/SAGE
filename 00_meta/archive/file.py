#!/usr/bin/env python3
import os, sys, hashlib, shutil

COPY_SUFFIX = " (copy 1)"

def original_path_from_copy(copy_path):
    folder, base = os.path.split(copy_path)

    # Folder: ".../archive (copy 1)" -> ".../archive"
    if base.endswith(COPY_SUFFIX):
        return os.path.join(folder, base[: -len(COPY_SUFFIX)])

    # File: "name (copy 1).ext" -> "name.ext"
    root, ext = os.path.splitext(base)
    if root.endswith(COPY_SUFFIX):
        return os.path.join(folder, root[: -len(COPY_SUFFIX)] + ext)

    return None

def delete_empty_dirs_bottom_up(root_dir):
    for root, dirs, _ in os.walk(root_dir, topdown=False):
        for d in dirs:
            full = os.path.join(root, d)
            try:
                if os.path.isdir(full) and not any(os.scandir(full)):
                    os.rmdir(full)
            except OSError:
                pass

def keep_original_delete_copy_pairs(paths, different_log):
    # For every "(copy 1)" path, if its original exists (by name mapping),
    # delete the copy path (file or directory).
    # Logs deletions and unmatchable copy paths.
    processed = set()

    open(different_log, "w", encoding="utf-8").close()

    with open(different_log, "a", encoding="utf-8") as log:
        for p in paths:
            if p in processed:
                continue
            processed.add(p)

            if COPY_SUFFIX not in p:
                continue

            copy_path = p
            original_path = original_path_from_copy(copy_path)
            if not original_path:
                continue

            if os.path.exists(original_path) and os.path.exists(copy_path):
                if os.path.isfile(copy_path):
                    try:
                        os.remove(copy_path)
                        print(f"Deleted copy (kept original): {copy_path}")
                        log.write(f"DELETED FILE COPY: {copy_path}\n  original: {original_path}\n")
                    except OSError as e:
                        log.write(f"FAILED TO DELETE FILE COPY: {copy_path}\n  error: {e}\n")
                elif os.path.isdir(copy_path):
                    try:
                        shutil.rmtree(copy_path)
                        print(f"Deleted copy dir (kept original): {copy_path}")
                        log.write(f"DELETED DIR COPY: {copy_path}\n  original: {original_path}\n")
                    except OSError as e:
                        log.write(f"FAILED TO DELETE DIR COPY: {copy_path}\n  error: {e}\n")
            else:
                if os.path.exists(copy_path):
                    log.write(f"KEPT UNMATCHED COPY (original missing): {copy_path}\n")
                # if copy_path missing, do nothing

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 delete_copy1_keep_original.py paths.txt [logfile]")
        sys.exit(1)

    list_file = sys.argv[1]
    log_file = sys.argv[2] if len(sys.argv) >= 3 else "different.log"

    with open(list_file, "r", encoding="utf-8") as f:
        paths = [ln.strip() for ln in f if ln.strip()]

    keep_original_delete_copy_pairs(paths, log_file)

if __name__ == "__main__":
    main()
