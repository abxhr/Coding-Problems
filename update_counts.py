import os
import re
import subprocess

curr_dir = os.getcwd()

exclude = [
    ".gitignore", 
    "README.md", 
    ".git", 
    "assets", 
    ".deepsource.toml", 
    "update_counts.py"
]

counted = []
counts = {
    "leetcode": 0,
    "codeforces": 0,
    "hackerrank": 0,
    "codechef": 0,
    "atcoder": 0,
    "gfg": 0,
    "hackerearth": 0
}

def get_readme_contents() -> str:
    with open("README.md", "r", encoding="utf-8") as readme:
        return readme.read()

def counter(dir):
    count = 0
    print("First", os.listdir(dir), dir)
    for path in os.listdir(dir):
        curr = os.path.join(dir, path)
        print("curr:", curr)
        print("file:",path)
        if os.path.isfile(curr) and path not in exclude:
            count += 1
            counted.append(path)
        elif os.path.isdir(curr) and path not in exclude:
            os.listdir(curr)
            curr_count = counter(curr)
            if "LeetCode" in curr:
                counts["leetcode"] = curr_count
            elif path == "CodeForces":
                counts["codeforces"] = curr_count
            elif path == "HackerRank":
                counts["hackerrank"] = curr_count
            elif path == "CodeChef":
                counts["codechef"] = curr_count
            elif path == "AtCoder":
                counts["atcoder"] = curr_count
            elif path == "GeeksforGeeks":
                counts["gfg"] = curr_count
            elif path == "HackerEarth":
                counts["hackerearth"] = curr_count
            count += curr_count
    return count

def get_solved_counts() -> int:
    count = counter(curr_dir)
    return count

def write_readme_contents(contents: str) -> None:
    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write(contents)


if __name__ == "__main__":
    readme_contents = get_readme_contents()
    total = get_solved_counts()

    pattern = r"- _Total Solved:_ \d+\n- _LeetCode:_ \d+\n- _CodeForces:_ \d+\n- _HackerRank:_ \d+\n- _CodeChef:_ \d+\n- _AtCoder:_ \d+\n- _GeeksforGeeks:_ \d+\n- _HackerEarth:_ \d+\n"
    replace_w = f"- _Total Solved:_ {total}\n- _LeetCode:_ {counts['leetcode']}\n- _CodeForces:_ {counts['codeforces']}\n- _HackerRank:_ {counts['hackerrank']}\n- _CodeChef:_ {counts['codechef']}\n- _AtCoder:_ {counts['atcoder']}\n- _GeeksforGeeks:_ {counts['gfg']}\n- _HackerEarth:_ {counts['hackerearth']}\n"

    readme_contents = re.sub(
        pattern,
        replace_w,
        readme_contents,
    )

    write_readme_contents(readme_contents)
    print(get_readme_contents())

    print(f"Updated the solved count in the README.md to {total}")

    subprocess.run(["git", "add", "README.md"])

    print("README.md added to the staging area.")
