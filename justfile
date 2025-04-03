set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

# list tasks
default:
    @just --list

# run bot
run *args:
    uv run pixl {{args}}

# lint code
lint:
    uv run pyright
    uv run ruff check --fix

# format code
format:
    uv run ruff format

# lint & format
verify: lint format
