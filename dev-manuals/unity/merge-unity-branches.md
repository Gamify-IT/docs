# How to merge Unity branches

1) Install [Sourcetree](https://www.sourcetreeapp.com/)  
1) Click on `Data > Clone / New`  
1) Clone your project  
1) Add your Github account  
1) Click on `Tools > Options > Diff`  
1) Change `Merge-Tool`to `Custom`  
1) Add `C:\unity\2021.3.1f1\Editor\Data\Tools\UnityYAMLMerge.exe` (you may search this .exe on your PC) to `Merge-Command`  
1) Add `merge -p $BASE $REMOTE $LOCAL $MERGED` to `Arguments`  
1) Download [TortoiseGit](https://tortoisegit.org/download/)  
1) Add path of TortoiseGit to `C:\unity\2021.3.1f1\Editor\Data\Tools\mergespecfile.txt` like this `* use "%programs%\TortoiseGit\bin\TortoiseGitMerge.exe" -base:"%b" -mine:"%l" -theirs:"%r" -merged:"%d"` (at line 21)  

## Merge branch X to Y
1) Check out `Y`  
1) Right click `X` in `History`-view  
1) Select `Merge...`  
1) Switch to `Data Status`-view  
1) Right click the merge conflicts  
1) Select `Resolve conflicts > Start external merge-tool...`  
1) Wait (something will happen... eventually... someday...)  
1) When a TortoiseGit-windows pops up fix the conflict manually and press `Resolveconflict`  
1) Ignore the error and close it and TortoiseGit  
1) Wait  
1) Press `Commit` in the bottom left corner  
1) Press `Push`  
