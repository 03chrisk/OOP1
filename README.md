# OOP - 2023/24 - Assignment 1

This is the base repository for assignment 1.
Please follow the instructions given in the [PDF](https://brightspace.rug.nl/content/enforced/243046-WBAI045-05.2023-2024.1/2023_24_OOP.pdf) for the content of the exercise.

## How to carry out your assignment

1. Clone this template into a private repository.
2. Please add your partner and `oop-otoz` to the collaborators.
3. Create a new branch called `submission`.
4. Create your code in the `main` branch.
5. Once you are done with the assignment (or earlier), create a pull request from the `main` branch to your `submission` branch and add `oop-otoz` to the reviewers.

The assignment is divided into 4 blocks.
Block 1, 2, and 3 all define different classes.

Put the three classes in three separate files in the `src` folder, with the names specified in the PDF.
**Leave the __init__.py file untouched**.

Put the **main.py** script **outside** of the `src` folder, in the root of this repo.

Below this line, you can write your report to motivate your design choices.

## Submission

The code should be submitted on GitHub by opening a Pull Request from the branch you were working on to the `submission` branch.

There are automated checks that verify that your submission is correct:

1. Deadline - checks that the last commit in a PR was made before the deadline
2. Reproducibility - downloads libraries included in `requirements.txt` and runs `python3 main.py`. If your code does not throw any errors, it will be marked as reproducible.
3. Style - runs `flake8` on your code to ensure adherence to style guides.

---

## Your report

