# Tasks of the Project Manager

## First Day of the Sprint

- [ ] Copy most important statistics from sheet `Issues` to the last row of `Sprints`
- [ ] Add last row to sheet `Sprints!A` with the new Sprint name
- [ ] Create an issue with 0 storypoints that is closed immediately
- [ ] Copy the sheet `Sprint $PREVIOUS_SPRINT_NAME` to `Sprint $CURRENT_SPRINT_NAME`
- [ ] Click on Column `A` or Cell `A1` in the new sheet and increase the number in `Sprints!A\d` by one
- [ ] Archive and protect the sheet `Sprint $PREVIOUS_SPRINT_NAME`
- [ ] Copy the sheet `Zeiten` to the archived and protected sheet `Zeiten - $CURRENT_SPRINT_NAME`
- [ ] Clear the sheet `Zeiten` except for the first two rows (columns and pseudo-work)
- [ ] Adapt the only date present to today
- [x] Enjoy everything working correctly

## Last Day of the Sprint

- [ ] Create an issue with 0 storypoints that is closed immediately
- [ ] One-time-setup for the automation script: Execute `git clone https://Gamify-IT/issues.git; cd issues; python -m venv venv; . venv/bin/activate && pip install -r requirements.txt && cp $GOOGLE_OAUTH_SECRETS_FILE secrets.json && cp $GOOGLE_SHEET_ID_FILE sheet-id.txt`. Optional: `cp $GITHUB_PAT_FILE github-pat.txt`
- [ ] Setup automation script: Execute `. venv/bin/activate`
- [ ] Execute automation script: Execute `python spreadsheet-issue-updater.py`
- [ ] Manually enter the current sprint in the sheet `Issues!D` for all issues that were worked on in this sprint
- [ ] Close all remaining open issues that were worked on in this sprint in GitHub
- [x] **IMPORTANT**: Do not execute script above anymore after the previous step, or the diagrams will be wrong!
- [ ] Prepare the rest of the review presentation
- [ ] Name both the latest versions of the presentation and of the sheets to be able to find them later again
