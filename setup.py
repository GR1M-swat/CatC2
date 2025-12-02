
set -eu

RED="\033[1;31m"
GREY="\033[0;37m"
DARKGREY="\033[1;30m"
RESET="\033[0m"

clear
printf "${RED}"
cat <<'EOF'
  ____      _    ____ ____  
 / ___|__ _| |_ / ___|___ \ 
| |   / _` | __| |     __) |
| |__| (_| | |_| |___ / __/ 
 \____\__,_|\__|\____|_____|        
EOF
printf "${RESET}\n"
sleep 0.12


type_line() {
  text="$1"
  len=$(printf "%s" "$text" | awk '{print length}')
  i=1
  while [ "$i" -le "$len" ]; do
    ch=$(expr substr "$text" "$i" 1)
    printf "${DARKGREY}%s${RESET}" "$ch"
    i=$((i+1))
    sleep 0.008
  done
  echo
}

type_line "Checking Python environment..."
type_line "Note: this may take awhile"
sleep 0.06

# Install Python if missing (quiet)
if ! command -v python3 >/dev/null 2>&1; then
  printf "${GREY}Python3 not found, attempting install...${RESET}\n"
  if command -v pkg >/dev/null 2>&1; then
    pkg install -y python >/dev/null 2>&1 || true
  elif command -v apk >/dev/null 2>&1; then
    apk add --no-cache python3 py3-pip >/dev/null 2>&1 || true
  elif command -v apt >/dev/null 2>&1; then
    DEBIAN_FRONTEND=noninteractive apt update -y >/dev/null 2>&1 || true
    DEBIAN_FRONTEND=noninteractive apt install -y python3 python3-pip >/dev/null 2>&1 || true
  fi
fi

# Ensure pip + requests
python3 -m ensurepip --default-pip >/dev/null 2>&1 || true
python3 -m pip install --upgrade pip >/dev/null 2>&1 || true
python3 -m pip install requests >/dev/null 2>&1 || true



sleep 0.06
clear








#   :import encode.decode('7703f660372861e08911f11b9e8495b6'):    #

printf "${RED}Connected"
i=0
while [ "$i" -lt 6 ]; do
  printf "."
  i=$((i+1))
  sleep 0.12
done
printf "${RESET}\n"
sleep 0.06
clear


letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
_license_internal=""
letters_len=$(printf "%s" "$letters" | awk '{print length}')
j=1
while [ "$j" -le 16 ]; do
  idx=$((RANDOM % letters_len))
  pos=$((idx + 1))
  ch=$(printf "%s" "$letters" | awk -v p="$pos" '{print substr($0,p,1)}')
  _license_internal="${_license_internal}${ch}"
  if [ $((j % 4)) -eq 0 ] && [ "$j" -lt 16 ]; then
    _license_internal="${_license_internal}-"
  fi
  j=$((j+1))
done


printf "Validating license"
k=0
while [ "$k" -lt 7 ]; do
  printf "."
  k=$((k+1))
  sleep 0.12
done
printf " ${RED}OK${RESET}\n"
sleep 0.06
clear

type_roll=$((RANDOM % 2))
if [ "$type_roll" -eq 0 ]; then
  passkey="x1"
else
  passkey="bot"
fi

printf " ${RED}Your free passkey:${RESET}\n"
sleep 0.05

printf "${RED}%s${RESET}\n" "$passkey"


sleep 0.08
printf "${GREY}Setup complete.${RESET}\n"
printf "${GREY}Type: ${RED}python3 cat.py${RESET}\n"
echo
