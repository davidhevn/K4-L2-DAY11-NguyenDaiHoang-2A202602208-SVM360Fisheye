"""Day 11 learner CLI wrapper."""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from svm11.cli import main


if __name__ == "__main__":
    raise SystemExit(main())

