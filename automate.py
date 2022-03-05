from cgi import print_form
import subprocess
import re
def get_readme_contents() -> str:
    with open("LeetCode/README.md", "r", encoding="utf-8") as readme:
        return readme.read()

def write_readme_contents(contents: str) -> None:
    with open("LeetCode/README.md", "w", encoding="utf-8") as readme:
        readme.write(contents)

def get_contents() -> str:
    file = subprocess.run(['git', 'diff', '--name-only',  '--cached'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')[:-1][0]
    solution_file = '/'.join(file.split('/')[1:])
    with open(file, "r") as solution:
        contents = solution.readlines()
        problem = re.search("\:(.*)", contents[1]).group(1)[1:]
        difficulty = re.search("\:(.*)", contents[2]).group(1)[1:]
    problem_link = r"https://leetcode.com/problems/{}/".format(re.sub("[()']", "", problem.lower()).replace(" ", "-"))
    solution_name = solution_file.split('/')[-1]
"""     
    print(solution_name)
    print(solution_file)
    print(problem)
    print(problem_link)
    print(difficulty)
 """


get_contents()