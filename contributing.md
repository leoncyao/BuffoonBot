## Setup:
1. Install `uv` with 
```bash
pip install uv
```
2. Sync all project dependencies and create a venv with
```bash
uv sync
```
3. Activate the venv

Windows:
```bash
.venv\scripts\activate
```

Mac:
```bash
source .venv/bin/activate
```

## Add dependencies
Run `uv add <dependency>`
## Test against stockfish
Download the appropriate stockfish from https://github.com/official-stockfish/Stockfish/wiki/Download-and-usage#official-downloads
```bash
export STOCKFISH_PATH="<path>"
```
```bash
uv run fight_fish.py
```


Test run with limited resources (5MB memory, 1 CPU):
```bash
docker run --cpus 1 -it --rm $(docker build -q .)
```