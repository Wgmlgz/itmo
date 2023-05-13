# itmo

My itmo struff 🐸

## My isu number

371364

## latex

```
sudo apt install texlive-full
```

## LaTeX monospace font

```
mkdir font
cd font
wget https://download.jetbrains.com/fonts/JetBrainsMono-1.0.0.zip
unzip JetBrainsMono-1.0.0.zip
sudo mv *.ttf /usr/share/fonts/
```

## helios

```
ssh s371364@helios.cs.ifmo.ru -p 2222
```
```
ssh -p 2222 s371364@se.ifmo.ru -L 5432:pg:5432
```


## random setup scripts
```
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk install gradle
sdk install kotlin
```