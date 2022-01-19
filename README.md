# Automatic notes creator

I usually take the time to separate my notes in a specific format, goal of this project was to provision these notes automatically. Ideally ignoring weekend days.  

## How to use 

```bash
git clone git@github.com:duchaineo1/automatic-notes-creator.git
cd automatic-notes-creator
python -m venv .venv
pip install -r requirements.txt
```

Add this line to your crontab : `30 8 1 * * /path/to/.venv/bin/python /path/to/app.py`

* Change the paths for the full path to the virtual env python and the script. 
* Use the user you usually use to create the crontab instead of root. This way you'll get a good permission set.
* Adjust crontab as needed, the current format runs every first of the month at 8:30 am. [https://crontab.guru/](https://crontab.guru/)
