#!/usr/bin/env bash

REPOSITORY=my-repo

set -e

rm -rf "${REPOSITORY}"
mkdir "${REPOSITORY}"
pushd "${REPOSITORY}"
touch README.md
git init
git remote add origin codecommit::eu-west-1://my-profile@repository
git add README.md
git commit -m "feat: initial commit"

git checkout -b documentation-update

echo "# ${REPOSITORY}" >> README.md
echo "" >> README.md
echo "This is a test repository with multiple commits. These commits can be used to test the pull-request-codecommit tool." >> README.md
git add README.md
git commit -m "feat: initial README setup

Because it is a good practice to describe what a repository is doing we add it to the README.md.

Issue: #1"

echo "" >> README.md
echo "We want to support multiple commits" >> README.md

git add README.md
git commit -m "docs: describe multiple commits

Issue: #1"

echo "" >> README.md
echo "Even more and different issue number" >> README.md

git add README.md
git commit -m "chore: other issue number

Issue: #2"

echo "" >> README.md
echo "Even more and different style issue number" >> README.md

git add README.md
git commit -m "refactor: use jira style issue number

fixes issue JIRA-1234"

poetry run pull-request-codecommit
