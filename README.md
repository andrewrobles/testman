### How to set up Instabot for local development
- Download Firefox webdriver https://github.com/mozilla/geckodriver/releases 
- Unzip `geckodriver` to root directory
- Add driver to path `export PATH=$PATH:$(pwd)`
- Enable setup script `chmod +x setup.sh`
- Run setup script `./setup.sh`
- Replace `username`, `password`, and `message` and in `settings.json`
- Put usernames on different lines in `usernames.txt`
- Verify tests run without failure `python3 test.py`

### Questions, comments, or concerns?
I'm best reachable by email `andrewrobles@berkeley.edu`