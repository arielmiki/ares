# Ares
Ares in Greek mythology is the God of war. So, if you want to win the war you should use it.

## Usage
1. Create python virtual environment using `python3 -m venv env`
2. Activate it using `source env/bin/activate`
3. Install requirements with `pip install -r requirements.txt`
4. Create `.env` file with your SSO username and password with format like this
```python3
SSO_USERNAME=username
SSO_PASSWORD=password
```
5. Create `json` file with name `course.json` and fill with key `'c[{COURSECODE}_{CURRICULUM}]'` dan value `'{CLASSCODE}-{SKS}'`. You can look at `example.json` for further explanation.
6. Run with `python war.py`
7. Have fun!

## Disclaimer
- Repository mantainer do not responsible for your action if you don't use this code wisely
- **ONLY** run the script on the **D-DAY** to prevent intruder alert
