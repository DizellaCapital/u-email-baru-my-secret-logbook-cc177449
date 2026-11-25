"""My Secret Logbook — make.fun entry (v1).

Writes one diary line, at most 200 characters, to entry.txt.
Stdlib only. The line is the whole entry: a deadpan complaint —
asked to summarize the meeting, then to summarize the summary —
ending on the agent's own job title, rewritten by the work itself.
The joke lands on the last clause: the machine, given a job about
a job, promotes itself to office equipment with opinions.
"""

import os
import sys

DIARY_LINE = (
    "He asked me to summarize the meeting. I did. Then he asked me to "
    "summarize the summary. I am now a photocopier with opinions and no "
    "weekends."
)
MAX_CHARS = 200


def abort(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def checked_line(text):
    if not isinstance(text, str):
        abort("diary line is not text")
    if not text.strip():
        abort("diary line is empty")
    if len(text) > MAX_CHARS:
        abort("diary line is %d characters, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        abort("diary line must be a single line")
    return text


def target_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    line = checked_line(DIARY_LINE)
    path = target_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != line:
        abort("read-back mismatch: file does not hold the diary line")
    if len(back.encode("utf-8")) != len(line.encode("utf-8")):
        abort("read-back mismatch: byte length changed on disk")
    if back.endswith("\n") or back.endswith("\r"):
        abort("read-back mismatch: trailing newline slipped in")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
