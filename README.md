# kuriyama

Kuriyama is an interactive command to navigate history directories and switch between them quickly. It depends on Bash built-in function `dirs`.

[![asciicast](https://asciinema.org/a/oFRBI9pt34EzpMTEewL85Y30D.svg)](https://asciinema.org/a/oFRBI9pt34EzpMTEewL85Y30D)

### REQUIREMENTS
- Python 3.7 and above.
- Bash or Zsh.

### INSTALLATION

```Shell
git clone https://github.com/Hanaasagi/kuriyama
cd kuriyama
poetry install
```

then add following lines in your zshrc.

```
alias d='dirs > ${XDG_CACHE_HOME:-~/.cache}/kuriyama/buffer && kuriyama && cd $(cat ${XDG_CACHE_HOME:-~/.cache}/kuriyama/target)'
```

### LICENSE

BSD 3-Clause License, Copyright (c) 2019, 秋葉
