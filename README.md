# ChainHelper
A tool that checks the status of your TORN.com chain targets and skips the ones that are not "Okay".  
**I wrote it during the chain and haven't cleaned up code since then. Don't judge me please OwO**

## Purpose
Allows you to skip the boring username copypasting part of the chain.  
It also ignores the targets that are not ready to be attacked (they're in the hospital or traveling), so you don't waste your time on looking at their profiles.  

## Usage
1. Download the script or clone the repository
2. Uncomment line 63 if you want the script to automatically open Firefox (change it to whatever command runs your browser) whenever it finds an attackable target.
3. Create `targets.txt` or edit the sample one I included (got targets from Baldr's Guide).

When you run it (with Python 3), it starts going through `targets.txt` querying API for your target's information.  
If it founds the target you can attack, it spits out the attack link (or opens your browser on victim's profile) and waits for you to hit Enter.  
When you do that, it checks the next target.