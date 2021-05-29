# newm v0.1
[![IMAGE](https://github.com/jbuchermn/newm/blob/v0.1/newm/resources/screenshot.png)](https://youtu.be/otMEC03ie0g)
(Wayland compositor)

## Idea

TODO

## Installing

### Prerequisites and pywm

[pywm](https://github.com/jbuchermn/pywm) is the abstraction layer for and main dependency of newm. If all prerequisites are installed, the command:

``` sh
pip3 install git+https://github.com/jbuchermn/pywm
```

should suffice.

Additionally, unless configured otherwise, newm depends on alacritty.


### Single-user installation (without newm-login)

To install newm:

``` sh
pip3 install git+https://github.com/jbuchermn/newm
```

Start it using

``` sh
start-newm
```

### Configuring

#### Setting up the config file

Configuring is handled via Python and read from either `$HOME/.config/newm/config.py` or (lower precedence) `/etc/config.py`. Take `default_config.py` as a basis and check the source code for usages of `configured_value` to get more details about the different keys.

For example, copy:

``` sh
cd
mkdir -p .config/newm
cp .local/lib/pythonX.Y/site-packages/newm/default_config.py .config/newm/config.py
vim .config/newm/config.py
```

and adjust:

``` py
import os
from pywm import (
    PYWM_MOD_LOGO,
    PYWM_MOD_ALT
)

mod = PYWM_MOD_ALT
wallpaper = os.environ['HOME'] + '/wallpaper.jpg'
```


#### Lock on hibernate

Place in `/lib/systemd/system-sleep/00-lock.sh`

``` sh
#!/bin/sh
newm-cmd lock-$1 
```

### Multi-user installation with greetd (to use newm for login)

Make sure to also install pywm using sudo:

``` sh
sudo pip3 install git+https://github.com/jbuchermn/pywm
sudo pip3 install git+https://github.com/jbuchermn/newm
```

Place configuration in `/etc/newm/config.py` and check, after logging in as `greeter`, that `start-newm` works and shows the login panel (login itself should not work). If it works, set

``` toml
command = "start-newm"
```

in `/etc/greetd/config.toml`.

## Panel

See [newm-panel-nwjs](https://github.com/jbuchermn/newm-panel-nwjs) for a different panel implementation (launcher, locker, notifiers) based on NW.js.
