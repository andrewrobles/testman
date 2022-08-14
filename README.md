# Testman
How to set up Testman for local development
- Download Firefox webdriver https://github.com/mozilla/geckodriver/releases 
- Unzip `geckodriver` to root directory
- Add driver to path `export PATH=$PATH:$(pwd)`
- Enable setup script `chmod +x setup.sh`
- Run setup script `./setup.sh`
- Create a file in root directory called `settings.json` with the following contents:
```json
{
    "username": "",
    "password": ""
}
```
- Add LeetCode `username` and `password` in `settings.json`
- Put usernames on different lines in `usernames.txt`
- Enable run script `chmod +x run.sh`
- Run the program `./run.sh`

## Use case
```python
python3 -i testman.py
>>> from solution import Solution
>>> t = Testman()
>>> t.submit('two-sum', 'solution.py')
```