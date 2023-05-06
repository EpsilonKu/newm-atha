# Installation on Arch Linux

## With the aur

The easiest and safest way to install newm-atha on Arch is by using its AUR package.

example:
```sh
yay -S newm-atha-git
```
(subsitute `yay` with your aur helper,eg: `paru`)

## From source (archlinux specific)

Maybe you want to test features in development or help with debugging, whatever the case, the following tutorial aims to show how to:
- install a different branch from the main newm branch.
- install from a local copy of the repo
- install a old release

1. Clone PKBUILD

```sh
yay -G newm-atha-git
```

2. Navigate to the downloaded folder

```sh
cd newm-atha-git
```

3. Clone pywm and newm

```sh
git clone https://git.sr.ht/~atha/pywm-atha.git --branch=<any branch or tag>
git clone https://git.sr.ht/~atha/newm-atha.git --branch=<any branch or tag>
```

4. Build and install

```sh
makepkg -sic
```
> Note for iterative building: remove the last build package with `rm *zst` before building,or else it will reinstall the same package that was previously built


## Tips and tricks / Install help

### `start-newm -d` core dumps as soon as it is started!
  - **Q:** I started newm with  `start-newm -d` and it core dumped!
  - **A:** try installing polkit(`pacman -S polkit`). We can't explain it, but it has fixed issues in the past.
  - **Q:** What if it still doesn't work?
  - **A:** Open a [ticket](https://todo.sr.ht/~atha/newm-atha) and post your log.


