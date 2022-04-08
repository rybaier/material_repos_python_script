# python material script challenge from SaifAlushi1
for some fun I took on a friends [challenge](https://github.com/saifalushi1/material-script) to build a material script for our GA course materials similiar to the one he wrote with JS. For an added bit of fun and because I've been expermenting with it. I decided to also have the script run the github cli tool for cloning all the repos

## Before running the script complete the following 
### clone the repo
### install gh cli
  `brew install gh`

### Attach gh cli to Git Enterprise Account
`gh auth login`
- follow the prompts 
##### You should see something similiar to the following after
- ` ? What account do you want to log into? GitHub Enterprise Server`
- ` ? GHE hostname: git.generalassemb.ly`
- ` ? What is your preferred protocol for Git operations? SSH`
- ` ? Upload your SSH public key to your GitHub account? Skip`
- ` ? How would you like to authenticate GitHub CLI? Login with a web browser`
- ` ! First copy your one-time code: [randomkeyhere]`
- ` Press Enter to open git.generalassemb.ly in your browser... `
- ` ✓ Authentication complete.`
- ` gh config set -h git.generalassemb.ly git_protocol ssh`
- ` ✓ Configured git protocol`
- ` ✓ Logged in as [username]`

## Once the above is completed 
cd into repo directory then run the following command in terminal to start the script
`python3 ghcli_script.py`