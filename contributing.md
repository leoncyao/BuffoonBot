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

Test run:
```bash
docker run --cpus 1 -it --rm $(docker build -q .)
```