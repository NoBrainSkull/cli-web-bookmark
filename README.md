# cli-web-bookmark
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