#!/usr/bin/env python3

import os
import time
import random
import string
import argparse
import logging
import sys
from datetime import datetime


class GhostLockSimulator:
    def __init__(self, target_dir="test", extensions=None, log_file=None):
        self.target_dir = os.path.abspath(target_dir)

        self.extensions = extensions or [
            ".txt", ".docx", ".xlsx",
            ".pdf", ".jpg", ".png"
        ]

        self.affected_files = []
        self.simulated_key = self.generate_key()
        self.simulation_id = self.generate_simulation_id()

        self.logger = self.setup_logging(log_file)

    def generate_key(self):
        return "".join(
            random.choice(string.ascii_letters + string.digits)
            for _ in range(32)
        )

    def generate_simulation_id(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_part = "".join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(8)
        )
        return f"GHOST-{timestamp}-{random_part}"

    def setup_logging(self, log_file):
        logger = logging.getLogger("ghostlock")
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            console = logging.StreamHandler()
            console.setFormatter(
                logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"
                )
            )
            logger.addHandler(console)

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(
                logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"
                )
            )
            logger.addHandler(file_handler)

        return logger

    def scan_for_files(self):
        self.logger.info(
            f"Scanning directory: {self.target_dir}"
        )

        if not os.path.isdir(self.target_dir):
            self.logger.warning(
                f"Directory does not exist: {self.target_dir}"
            )
            return 0

        print("\nGhostLock scanning...\n")

        count = 0

        for root, _, files in os.walk(self.target_dir):
            for filename in files:
                _, ext = os.path.splitext(filename)

                if ext.lower() in self.extensions:
                    path = os.path.join(root, filename)
                    self.affected_files.append(path)

                    count += 1

                    sys.stdout.write(
                        f"\rScanning... {count} files found"
                    )
                    sys.stdout.flush()

        print()

        self.logger.info(
            f"Scan complete. Found {len(self.affected_files)} files."
        )

        return len(self.affected_files)

    def simulate_encryption(self):
        if not self.affected_files:
            print("\nNo matching files found.")
            return 0

        print("\nSimulating encryption...\n")

        total = len(self.affected_files)

        for i, path in enumerate(self.affected_files, 1):
            # SAFE: original files are NEVER modified
            print(f"[SIMULATED] {i}/{total}: {path}")

            self.logger.info(
                f"Would encrypt: {path}"
            )

            time.sleep(0.05)

        print("\nSimulation finished.")

        return total

    def display_ransom_note(self):
        print()
        print("=" * 70)
        print("             GHOSTLOCK RANSOMWARE SIMULATION")
        print("=" * 70)
        print()
        print("THIS IS ONLY A SIMULATION")
        print("NO REAL FILES WERE ENCRYPTED OR MODIFIED.")
        print()
        print(f"Files detected: {len(self.affected_files)}")
        print(f"Simulation ID: {self.simulation_id}")
        print(f"Simulation key: {self.simulated_key[:8]}...")
        print(f"Timestamp: {datetime.now().isoformat()}")
        print()
        print("Educational / security testing only.")
        print("=" * 70)


def display_banner():
    print()
    print("=" * 60)
    print("              GHOSTLOCK SIMULATOR")
    print("=" * 60)
    print("        Safe ransomware behavior demo")
    print("        NO REAL FILE ENCRYPTION")
    print("=" * 60)
    print()


def main():
    parser = argparse.ArgumentParser(
        description="GhostLock safe ransomware simulator"
    )

    # FIX: --target-dir is no longer required
    parser.add_argument(
        "--target-dir",
        default="test",
        help="Directory to scan (default: test)"
    )

    parser.add_argument(
        "--extensions",
        nargs="+",
        default=[
            ".txt", ".docx", ".xlsx",
            ".pdf", ".jpg", ".png"
        ],
        help="File extensions to scan"
    )

    parser.add_argument(
        "--log-file",
        default=None,
        help="Optional log file"
    )

    args = parser.parse_args()

    display_banner()

    print(f"Target directory: {os.path.abspath(args.target_dir)}")
    print("Mode: SAFE SIMULATION")
    print()
    print("No original files will be changed.")
    print()

    try:
        simulator = GhostLockSimulator(
            target_dir=args.target_dir,
            extensions=args.extensions,
            log_file=args.log_file
        )

        simulator.scan_for_files()
        simulator.simulate_encryption()
        simulator.display_ransom_note()

        print("\nSimulation completed successfully.")

    except Exception as error:
        print()
        print("ERROR:")
        print(error)


if __name__ == "__main__":
    main()
