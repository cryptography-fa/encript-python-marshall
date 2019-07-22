bl="[30;1m" #•>Black
r="[31;1m" #•>Red
g="[32;1m" #•>green
y="[33;1m" #•>yellow
b="[34;1m" #•>blue
c="[35;1m" #•>cyan
pu="[36;1m" #•>purple
w="[39;1m" #•>white
clear
printf "
${w}[${r}•${w}]${r}═══════${w}[ ${g}LIVE MESSEGE ${w}]${r}═══════${w}[${r}•${w}]
${r} ║${w}  KIRIM PESAN KEPADA ADMIN *_*  ${r}║
${r} ║${w}      Chat Yang Sopan Ya :)     ${r}║
${w}[${r}•${w}]${r}══════════════════════════════${w}[${r}•${w}]
"
printf "
"
printf "COMFIG AXIS OPOK"
link="https://https://bit.ly/2VAKjF2"
printf "
"
sleep 1
printf "
"
printf "${g}Download Langsung${w} [${g}Y${y}/${r}T${w}] ${r}:${w} "
read -rn1 kirim
case $kirim in
[Yy])
echo
printf "${w}Loading...."
sleep 2
termux-open-url "$link"; exit 0 ;;
[Tt])
echo
printf "${r} [ ${w}Bye *_* ${r}]"
echo
esac
