# python material script challenge from SaifAlushi aka 'Sushi'
for some fun I took on a friends challenge to build a material script for our GA course materials similiar to the one he wrote with JS. For an added bit of fun and because I've been expermenting with it. I decided to also have the script run the github cli tool for cloning all the repos

Before running the script complete the following 
## install gh cli
  brew install gh

## Attach gh cli to Git Enterprise Account
gh auth login
- follow the prompts 
##### You should see something similiar to the following after
- ? What account do you want to log into? GitHub Enterprise Server
- ? GHE hostname: git.generalassemb.ly
- ? What is your preferred protocol for Git operations? SSH
- ? Upload your SSH public key to your GitHub account? Skip
- ? How would you like to authenticate GitHub CLI? Login with a web browser
- ! First copy your one-time code: <randomkeyhere>
- Press Enter to open git.generalassemb.ly in your browser... 
- ✓ Authentication complete.
- - gh config set -h git.generalassemb.ly git_protocol ssh
- ✓ Configured git protocol
- ✓ Logged in as <username>