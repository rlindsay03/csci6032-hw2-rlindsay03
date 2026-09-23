---
name: blackboard-submission
description: "Use this skill when submitting the csci6032 HW2 assignment to Blackboard from the expected homework repository. It validates the repo identity and Git state, packages the committed HEAD into csci6032-hw2-rlindsay03.tar.gz without including .git, credentials, caches, or unrelated files, supports a dry run, pauses before the irreversible submission step until the student explicitly confirms, and prevents credential exposure or public storage of Blackboard receipts or browser data."
---

# Blackboard homework submission workflow

Use this skill only for the current coursework repository and only when the user explicitly wants the homework submitted to Blackboard.

## Required operating rules

- Confirm that the agent is operating in the expected homework repository: a repository matching the course homework pattern for the current GitHub username, such as `csci6032-hw2-<rlindsay03>`.
- Confirm the repository URL and the working directory before proceeding. Stop if the repo is the wrong project, the remote is not the expected course/homework repository, or required files are missing.
- Run a preflight before any Blackboard interaction:
  1. Check the current branch.
  2. Check `git status` for cleanliness.
  3. Check recent commits.
  4. Confirm the expected remote URL.
  5. Verify required files exist in the repository.
- Stop immediately if the tree is not clean, required artifacts are absent, or unresolved secrets, credentials, private data, or credential-like content are apparent.
- Do not store, print, type, read, or expose credentials. Never request credentials, private tokens, or Blackboard passwords from the user, even indirectly.
- Do not include `allowed-tools: "*"` in this skill, and do not preapprove shell or browser tools; permission prompts must remain visible and explicit.
- Ask before opening or controlling the Blackboard tab. Never do so automatically.
- Require the student to authenticate personally to Blackboard; do not assume or reuse another user’s session.
- Never commit Blackboard screenshots, receipts, browser data, or personal information to the public repository.

## Submission procedure

1. Confirm it is operating in the expected homework repository.
2. Run a preflight that checks the current branch, `git status`, recent commits, expected remote URL, and required files.
3. Stop if the tree is not clean, required artifacts are absent, or unresolved secrets/private data are apparent.
4. Confirm that the reviewed branch has been pushed to the expected remote and is ready for submission.
5. Prepare `csci6032-hw2-rlindsay03.tar.gz` from the committed `HEAD` without including `.git`, credentials, caches, or unrelated files.
6. List the archive contents and show the exact notebook, archive, repository URL, and submission text it proposes to use.
7. Support a dry run that performs every possible check without opening Blackboard or submitting anything.
8. Ask before opening or controlling the Blackboard tab.
9. Require the student to authenticate personally; never request, read, store, type, or expose credentials.
10. Navigate only to this homework’s Blackboard submission page and stage the required files and repository URL.
11. Stop immediately before the final, irreversible submission action and show the student exactly what will be submitted.
12. Require explicit confirmation at that point. A prior general approval is not sufficient.
13. After confirmation, complete the submission, verify the confirmation page or receipt, and report the result.
14. Do not commit Blackboard screenshots, receipts, browser data, or personal information to the public repository.

## Safety and output requirements

- Before any destructive or irreversible step, present the exact final submission payload for review, including:
  - the notebook file that will be submitted,
  - the archive file that will be uploaded,
  - the repository URL,
  - the exact submission text.
- The archive should be created from the committed `HEAD` and must exclude any `.git` directory, secrets, local caches, editor metadata, or unrelated files.
- If any dry run is requested, perform all checks and previews without opening Blackboard or submitting any data.
- If the repository is not ready or a required preflight check fails, stop and report the blocker before proceeding.
- If the user has not explicitly confirmed the final submission, do not submit.

## Required confirmation language

At the final review step, the agent must say clearly that it is about to submit the exact items listed below and wait for explicit confirmation before executing the irreversible action. This confirmation must be new and specific to the final submission, not a prior blanket approval.

## Expected artifact summary

The final submission workflow should produce and display, at minimum:

- `csci6032-hw2-rlindsay03.tar.gz`
- the exact notebook file selected for submission (for example `CSCI6032_hw2.ipynb`)
- the repository URL used for the submission
- the exact text to be posted in the Blackboard submission field

The skill must not override the user’s right to inspect and approve the final submission before the irreversible action is performed.
