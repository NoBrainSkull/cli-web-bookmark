# Dash your web bookmarks from Command line
Dash to your web fav with a single command line.


## Config

* Change database path in bookmark.py
* __Use your own webrowser command in main.py__

## Usage
Save a link

```bash
python main.py <bookmark-name> <url>
```

Access it
```bash
python main.py <bookmark-name>
```

Delete it
```bash
python main.py -r <bookmark-name>
```

## Boost it
symlink or alias a custom command with `python /path/to/main.py` like

```bash
alias bkm='python ~/sources/scripts/bookmarks/main.py'
```

so as to type :

```bash
bkm <bookmark-name>
```