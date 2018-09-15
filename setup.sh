 !/bin/bash

bldblu=${txtbld}$(tput setaf 4)

mkdir -p koruri mplus opensans
cd opensans
wget -o opensans.zip https://fonts.google.com/download?family=Open+Sans
unzip opensans.zip
cd ../

echo "${bldblu}                        **                        "
echo "${bldblu}                      **# **                      "
echo "${bldblu}                    **##### **                    "
echo "${bldblu}                  **######### **                  "
echo "${bldblu}                **############# **                "
echo "${bldblu}              **################# **              "
echo "${bldblu}            **##################### **            "
echo "${bldblu}          **###***      *****######## **          "
echo "${bldblu}        **##**        ***    ***####### **        "
echo "${bldblu}      **##**         *###*      ***###### **      "
echo "${bldblu}    **###*            ****         *****### **    "
echo "${bldblu}  **####*                     ***############ **  "
echo "${bldblu} **###**                    **#################** "
echo "${bldblu}  ****                     *##################**  "
echo "${bldblu}                          *#################**    "
echo "${bldblu}                         *|###############**      "
echo "${bldblu}                         *##############**        "
echo "${bldblu}                         *############**          "
echo "${bldblu}                         *##########**            "
echo "${bldblu}                         |########**              "
echo "${bldblu}                        *#######**                "
echo "${bldblu}                       * #####**                  "
echo "${bldblu}                      *#####**                    "
echo "${bldblu}                      ** #**                      "
echo "${bldblu}                        **                        "

echo "Koruri を生成するには FontForge をインストールし、"
echo "最新の M+ 1p を mplus/ に展開した後、以下を実行してください"
echo "fontforge -lang=py -script koruri.py"
tput sgr0
