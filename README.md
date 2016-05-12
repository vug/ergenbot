# ergenbot
A Twitter bot that imitates Turkish adolescents' way of speaking by replacing all vowels in a text with "o".

# Setup

Clone the repository

`$ git clone https://github.com/vug/ergenbot`

Create a virtual environment

```$ mkvirtualenv --python=`which python3` ergenbot```

Copy the text file you are going to "ergenize" and the `secrets.py` file that holds your app's authorization tokens to the ergenbot folder

`$ scp -i PEM_FILE TEXT_FILE secrets.py SERVER_URL:~/ergenbot`

Install the dependencies

`pip install -r requirements.txt`

# Usage

In project folder

`$ python ergenbot.py TEXT_FILE FIRST_WORD_NO PAUSE_DURATION SEND_TWEETS`

- `TEXT_FILE` (string) is the text file to ergenize
- `FIRST_WORD_NO` (int) is he number of the word from which the first tweet will start
- `PAUSE_DURATION` (int) is the tamount of time to wait between tweets
- `SEND_TWEETS` (0 or 1) is the switch to actually send tweets

Example: `$ python ergenbot.py aski_memnu.txt 0 1800 1` sends ergenized tweets from "Ask-i Memnu" every 30 minutes.
