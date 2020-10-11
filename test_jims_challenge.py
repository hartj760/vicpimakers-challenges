import pytest
import subprocess
import re

# Given this input: 72,111,63,85,61,56,118,121,61,69,63,61
# The challenge code should produce the following answers:
ANSWERS = [
    "941",
    "78,5",
    "72,56,118",
    "56,6",
    "5,61,61,61,63,63",
    "18543",
    "56,61,61,61,63,63,69,72,85,111,118,121",
    "Ho?U=8vy=E?=",
    "HOUVYE",
    "6",
]


@pytest.fixture
def script_run():
    result = subprocess.run(
        ["python/jims_challenge.py", "72,111,63,85,61,56,118,121,61,69,63,61"],
        stdout=subprocess.PIPE,
    )
    return result


def test_challenge_output(script_run):
    print("")
    assert script_run.returncode == 0
    output = script_run.stdout.decode("utf-8")
    for answer in enumerate(ANSWERS, 1):
        output_re = rf"Output\s*#{answer[0]}:\s*(.*)"
        stdout_answer_list = [
            line for line in output.split("\n") if re.match(output_re, line)
        ]
        assert (
            not len(stdout_answer_list) < 1
        ), f"no matches found for Output #{answer[0]}"
        assert (
            not len(stdout_answer_list) > 1
        ), f"multiple matches found for Output #{answer[0]}"
        output_answer = re.match(output_re, stdout_answer_list[0])
        assert (
            output_answer.group(1) == answer[1]
        ), f"answer for Output #{answer[0]} does not match"
        print(f"Output #{answer[0]} - correct = {answer[1]}")
