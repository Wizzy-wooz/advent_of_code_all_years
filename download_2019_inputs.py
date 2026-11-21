"""Download missing Advent of Code 2019 inputs using a local session token."""

import os
from pathlib import Path
import subprocess
import time


YEAR = 2019
ROOT = Path(__file__).resolve().parent
REQUEST_DELAY_SECONDS = 1.0


def download_input(day: int, session: str) -> bytes:
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    try:
        result = subprocess.run(
            [
                "curl",
                "--silent",
                "--show-error",
                "--location",
                "--max-time",
                "30",
                "--config",
                "-",
                "--user-agent",
                "Advent of Code input downloader (local use)",
                "--write-out",
                "\n__HTTP_STATUS__%{http_code}",
                url,
            ],
            capture_output=True,
            check=False,
            input=f'header = "Cookie: session={session}"\n'.encode(),
            timeout=35,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise RuntimeError(f"Could not download day {day}: {error}") from error

    if result.returncode:
        message = result.stderr.decode(errors="replace").strip()
        raise RuntimeError(f"Could not download day {day}: {message}")

    body, marker, status = result.stdout.rpartition(b"\n__HTTP_STATUS__")
    if not marker:
        raise RuntimeError(f"Could not read the HTTP status for day {day}")
    if status != b"200":
        detail = body[:300].decode(errors="replace").strip()
        raise RuntimeError(f"Day {day} returned HTTP {status.decode()}: {detail}")

    content = body

    if not content or content.lstrip().startswith(b"<!DOCTYPE html"):
        raise RuntimeError(
            f"Day {day} did not return puzzle input. Check that AOC_SESSION is valid."
        )
    return content


def main() -> None:
    session = os.environ.get("AOC_SESSION", "").strip()
    if not session:
        raise SystemExit("Set AOC_SESSION in your environment before running this script.")

    for day in range(1, 26):
        input_path = ROOT / str(YEAR) / f"day_{day}" / "input.txt"
        if input_path.exists() and input_path.stat().st_size > 0:
            print(f"Day {day}: already has input; skipped")
            continue

        content = download_input(day, session)
        input_path.parent.mkdir(parents=True, exist_ok=True)
        input_path.write_bytes(content)
        print(f"Day {day}: downloaded {len(content)} bytes")
        time.sleep(REQUEST_DELAY_SECONDS)


if __name__ == "__main__":
    main()
