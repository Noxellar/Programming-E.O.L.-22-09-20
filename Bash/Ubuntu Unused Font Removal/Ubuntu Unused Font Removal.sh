for i in fonts-kacst fonts-kacst-one fonts-khmeros-core fonts-lklug-sinhala fonts-guru fonts-nanum fonts-noto-cjk fonts-takao-pgothic fonts-tibetan-machine fonts-guru-extra fonts-lao fonts-sil-padauk fonts-sil-abyssinica fonts-tlwg-* fonts-lohit-* fonts-beng fonts-beng-extra fonts-gargi fonts-gubbi fonts-gujr fonts-gujr-extra fonts-kalapi fonts-lohit-gujr fonts-samyak-* fonts-noto-unhinted fonts-noto-hinted fonts-navilu fonts-nakula fonts-orya-extra fonts-pagul fonts-sahadeva fonts-sarai fonts-smc fonts-telu-extra fonts-wqy-microhei fonts-smc-anjalioldlipi fonts-smc-chilanka fonts-smc-dyuthi fonts-smc-karumbi fonts-smc-keraleeyam fonts-smc-manjari fonts-smc-meera fonts-smc-rachana fonts-smc-raghumalayalamsans fonts-smc-suruma fonts-smc-uroob fonts-mathjax; do
  sudo apt purge -y $i
  echo
done
 
echo "==== Fixing font cache"
sudo fc-cache -f -v && sudo dpkg-reconfigure fontconfig
 
echo "==== Packages remained (each containing multiple fonts)"
dpkg -l fonts\*|grep ^ii|awk '{print $2}'
 
 
echo
read -p "Press any key to close."
