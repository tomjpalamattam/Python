###ZSH CONFIGURATION
#paru -S zsh-syntax-highlighting zsh-autosuggestions fzf-tab-git zsh-completions starship

eval "$(starship init zsh)"
autoload -Uz compinit promptinit
compinit
promptinit
zstyle ':completion:*' menu select
zstyle ':completion::complete:*' gain-privileges 1

[[ -n "${key[Up]}"   ]] && bindkey -- "${key[Up]}"   up-line-or-beginning-search
[[ -n "${key[Down]}" ]] && bindkey -- "${key[Down]}" down-line-or-beginning-search

HISTSIZE=200000
export HISTFILE=/home/tom/.zsh_history
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory
setopt sharehistory
setopt hist_ignore_space
setopt hist_ignore_all_dups
setopt hist_save_no_dups
setopt hist_ignore_dups
setopt hist_find_no_dups



source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search
bindkey "^[[A" up-line-or-beginning-search
bindkey "^[[B" down-line-or-beginning-search

autoload -U compinit; compinit
source /usr/share/zsh/plugins/fzf-tab-git/fzf-tab.zsh 

zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'

###CUSTOM CONFIGURATION

PATH="/home/tom/.local/bin:$PATH"
export PATH
PATH="/home/tom/.dotnet/tools:$PATH"
export PATH
PATH="/home/tom/Desktop/launchers/binaries:$PATH"
export PATH
PATH="/var/lib/flatpak/exports/share:$PATH"
export PATH
PATH="/home/tom/.local/share/flatpak/exports/share:$PATH"
export PATH
PATH="/home/tom/apps/npm/bin:$PATH"
export PATH

alias vpn='sudo surfshark-vpn attack'
alias vpnd='sudo surfshark-vpn down'
alias vpns='sudo surfshark-vpn'
alias phone-ssh='sshfs phone:storage /home/tom/cloud-drives/Phone -o follow_symlinks -p 8022'
#alias ff='find "$(pwd)" -iname'
export LC_CTYPE=en_US.UTF-8
#export G_SLICE=always-malloc

### ARCHIVE EXTRACTION
# usage: ex <file>
ex ()
{
  if [ -f "$1" ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   unzstd $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

ff ()
{
  #find "$(pwd)" -type d \( -path /home/tom/cloud-drives -o -path /home/tom/.local/share/waydroid -o -path /home/tom/.WineApps \) -prune -o -iname "*$1*" -print
  fd --strip-cwd-prefix -i --exclude '/home/tom/cloud-drives' --exclude '/home/tom/.local/share/waydroid' --exclude '/home/tom/.WineApps' "$1"
}

ft ()
{
  fd --strip-cwd-prefix -i --exclude '/home/tom/cloud-drives' --exclude '/home/tom/.local/share/waydroid' --exclude '/home/tom/.WineApps' --changed-within "$1"
  #fd --strip-cwd-prefix -i --exclude '/home/tom/cloud-drives' --exclude '/home/tom/.local/share/waydroid' --exclude '/home/tom/.WineApps' --changed-before "$1"
}

tts ()
{
gtts-cli --file $1 --output $1.mp3 &  PIDTTF=$!
sleep 2 && vlc $1.mp3 & PIDVLC=$!
wait $PIDTTF
wait $PIDVLC
}

alias sttm='cd /home/tom/apps/vosk-api/python/example && python3 test_microphone.py -d 20'

cpph ()
{
scp -P 8022 $1 u0_a323@192.168.178.176:/data/data/com.termux/files/home/storage/shared/PC
}

cppc ()
{
scp -P 8022 u0_a323@192.168.178.176:/data/data/com.termux/files/home/storage/shared/$1 $2
}

alias convid='ffmpeg_convert'
function ffmpeg_convert() {
    ffmpeg -i "$1" -c:v h264_nvenc -rc constqp -qp 28 "${1%.*}.mkv"
}

#alias xlock='systemctl hibernate && xsecurelock'
alias hlock='systemctl hibernate && hyprlock'


xlock ()
{
export XSECURELOCK_SAVER=saver_mpv
export XSECURELOCK_LIST_VIDEOS_COMMAND="find ~/wallpapers/new -type f"
export XSECURELOCK_IMAGE_DURATION_SECONDS=15
systemctl hibernate && xsecurelock
}

alias subdl='source /home/tom/apps/cache/python-envs/subtitle/bin/activate && /home/tom/apps/cache/python-envs/subtitle/bin/python /home/tom/apps/opensubtitles_subtitle_downloader/download_subs.py $1 '
alias ls='eza --long --color=always --icons=always --no-user'
alias cat=bat
alias nano=nvim
export EDITOR=nvim


eval "$(zoxide init zsh)"

function v() {
	source ~/apps/cache/python-envs/ML/bin/activate
	nvim .
}

function y() {
	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
	yazi "$@" --cwd-file="$tmp"
	if cwd="$(command cat -- "$tmp")" && [ -n "$cwd" ] && [ "$cwd" != "$PWD" ]; then
		builtin cd -- "$cwd"
	fi
	rm -f -- "$tmp"
}
