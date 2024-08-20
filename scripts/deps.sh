#!/usr/bin/env bash

set -e

local_bin="$HOME/.local/bin"
mkdir -p "$local_bin"

if [[ ":$PATH:" != *":$local_bin:"* ]]; then
    update_path="export PATH=\"$local_bin:\$PATH\""
    eval "$update_path"
    case "$SHELL" in
        *zsh)
            echo "$update_path" >> "$HOME/.zshrc"
            ;;
        *bash)
            echo "$update_path" >> "$HOME/.bash_profile"
            ;;
        *)
            echo "WARNING: Could not determine shell startup file. Please prepend $local_bin to your PATH manually."
            ;;
    esac
fi

if [[ ! -f "$local_bin/envsub" ]]; then
    # Install enhanced `envsubst` command for templating
    # configs. Rename as `envsub` so as not to conflict with GNU
    # `envsubst`.
    curl -L https://github.com/a8m/envsubst/releases/download/v1.2.0/envsubst-"$(uname -s)"-"$(uname -m)" -o envsub
    chmod +x envsub
    mv envsub "$local_bin"
fi

if ! brew ls --versions mysql-client@5.7 > /dev/null; then
    # Install mysql-client via brew
    brew install mysql-client@5.7
fi
