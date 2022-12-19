# Tasks of the Project Manager

`$X` is the number of the previous sprint.  
`$Y` is the number of the current sprint.  
`$NAME(Z)` is the name of sprint `Z`.  
`$DIAGRAMS(Z)` is the sheet storing the diagrams for sprint `Z`.  
  - At the moment, these sheets are called `Diagramme $Z - $NAME(Z)`
`$TIMES(Z)` is the sheet storing the times worked in sprint `Z`.
  - At the moment, these sheets are called `Zeiten $Z - $NAME(Z)`

## First Day of the Sprint

- [ ] Copy the most important statistics from `$DIAGRAMS(X)` to the last row of `Sprints`
- [ ] Create an issue with 0 storypoints that is closed immediately
- [ ] Copy `$DIAGRAMS(X)` to `$DIAGRAMS(Y)`
- [ ] Protect `$DIAGRAMS(Y)`
- [ ] In `$DIAGRAMS(Y)!K2`, select the new sprint this sheet should track
- [ ] Add last row to sheet `Sprints` with the new Sprint name, the sprint starting date (inclusive), the sprint ending date (inclusive, so use a day prior).  
All rows that are not automatically filled can be copied from the row above except every occurence of `$DIAGRAMS(X)` should be replaced with `$DIAGRAMS(Y)`
- [ ] Archive and protect the sheet `$DIAGRAMS(X)`
- [ ] Copy the sheet `Zeiten` to the archived and protected sheet `$TIMES(X)`
- [ ] Clear the sheet `Zeiten` except for the first row (columns) and potential times that were entered for the next sprint already
- [ ] Make sure there is a entry which gives the invisible worker 0 minutes today
- [ ] Add the entry `;'TIMES(Y)'!A$2:F` to the end of the array in sheet `Gesamtzeiten!A1`
- [x] Enjoy everything working correctly

## Last Day of the Sprint

- [ ] Create an issue with 0 storypoints that is closed immediately
- [ ] One-time-setup for the automation script: Execute `git clone https://Gamify-IT/issues.git; cd issues; python -m venv venv; . venv/bin/activate && pip install -r requirements.txt && cp $GOOGLE_OAUTH_SECRETS_FILE secrets.json && cp $GOOGLE_SHEET_ID_FILE sheet-id.txt`. Optional: `cp $GITHUB_PAT_FILE github-pat.txt`
- [ ] Setup automation script: Execute `. venv/bin/activate`
- [ ] Execute automation script: Execute `python spreadsheet-issue-updater.py`
- [ ] Manually enter the current sprint in the sheet `Issues!G` for all issues that were worked on in this sprint
- [ ] Close all remaining open issues that were worked on in this sprint in GitHub
- [x] **IMPORTANT**: Do not execute script above anymore after the previous step, or the diagrams will be wrong!
- [ ] Prepare the rest of the review presentation
- [ ] Name both the latest versions of the presentation and of the sheets to be able to find them later again
