<div align="center">
    <h1>Reconnaissance visuel <img src="/logo.PNG"  width="196" height="103"> </h1>
</div>


>  Release : [release](https://github.com/Forestierr/Opencv-reconnaissance/releases)

Voici mon Gitlab regroupant mon travaille tout aux long de ma 3ème et ma 4ème années d'apprentssage,
sur le traitement d'image et la reconnaissance d'image.

Si vous êtes intéressé liser : [Practical Python and OpenCV 3rd Edition](https://github.com/Forestierr/Opencv-reconnaissance/blob/main/1_Documentation/Practical_Python_and_OpenCV__3rd_Edition.pdf)

<h2>Documention PDF</h2>

Documentation complète : [Document PDF](https://github.com/Forestierr/Opencv-reconnaissance/blob/main/1_Documentation/xwiki_OpenCV_23.08.2021.pdf)

<h2>Matériel</h2>

Voici le matérielle que j'ai pu essayer durant ma spécialisation :

|Nom |Utile |Liens |Prix |
|:---- |:---:   |:----|:--- |
|Raspberry Pi 3B+|✔️|[Raspberry](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) |40 .- |
|Raspberry Pi cam V1.3|✔|[Raspberry cam (v2)](https://www.raspberrypi.org/products/camera-module-v2/)|30 .-|
|Nvidia jetson TX2|✖️|[jetson TX2](https://www.nvidia.com/fr-fr/autonomous-machines/embedded-systems/jetson-tx2/)|600 .-|
|Coral USB accelerator|✖️|[USB accelerator](https://coral.ai/products/accelerator)|60 .-|
|OAK-D|✔|[OAK-D](https://store.opencv.ai/products/oak-d) |300 .-|

<h2>Raspberry Pi 3B+</h2>

J'ai donc commencer à travailler avec un Raspberry Pi 3B+ et une Raspberry Pi cam V1.3.
Pour commence il faut installer Python et Open CV sur le Raspberry.

<h3>Instalation d'Opencv et Python</h3>

Voici les commandes à entrer dans le teminal:

>>>
`sudo apt update` <br>
`sudo apt install python3` <br>
`sudo apt install python3-opencv` <br>
`python3` <br>
`import cv2` <br>
`cv2.__version__` <br>
>>>

Relancer un nouveau terminal.

>>>
`sudo apt update` <br>
`sudo apt install python3-pip` <br>
`pip3 install opencv-python` <br>
`python3` <br>
`import cv2` <br>
`cv2.__version__` <br>
>>>

Vous avez maintenant la dernière version d'Open CV installée.

<h3>Instalation de la caméra</h3>

Pour brancher la caméra veiller à :
- Ne pas être charger en électriciter static.
- Débrancher l'alimentation de votre Raspberry Pi.

<p> <img src="https://raw.githubusercontent.com/Forestierr/Opencv-reconnaissance/main/1_Documentation/img/install_cam.gif"  width="400" height="200"> </p>

- Dans les réglages d'interface de Raspberry Pi, activer la caméra.

<h3>Tester la caméra </h3>

Pour tester la caméra taper la commande suivante dans votre terminal.

>>>
Prendre une photo :
`raspistill -o photo_01.jpg -t 5000` <br>
Prendre une vidéo :
`raspivid -o video_01.h264 -t 5000` <br>
>>>

<h2>Open CV </h2>

<h3>Présentation </h3>

OpenCv est un bibliothèque graphique développée par Intel depuis 2000 elle est disponible sur la majorité des plateformes comme Windows, Mac, Linux, IOS… Elle fonction avec plusieurs langages comme python, java et C++. <br> 
OpenCv est sous licence BSD (Berkeley Software Distribution Licence) ce qui permet à n’importe qui de l’utiliser même pour un projet commercialisé. <br>
OpenCv propose plus de 2500 algorithmes pour effectuer différent traitement sur une image comme de la détection de couleur, de l’extraction d’information etc. <br>

<h3>Programme </h3>

Vous trouverez l'entièreté de mes programmes de test [ici](https://github.com/Forestierr/reconnaissance-visuel/tree/master/5_Programmation/test). <br>
Pour les tester, utilisé Thonny disponible de base sur Raspberry Pi. <br>
Vous Trouverez ci dessous la documentation officiel d'Open CV ansi qu'un site explicant l'entièreté
des principales fonctions.

- [Open CV](https://opencv.org)
- [Tutoriel (non officiel)](https://opencv-python-tutroals.readthedocs.io/en/latest/index.html)

<h2>Nvidia Jetson TX2 </h2>

La carte Nvidia jetson TX2 est une carte de développement pour l’ai et le machin learning. <br>
Elle est d’après ses statistiques la meilleure carte de développement disponible actuellement sur le marché (2020). 

J’ai souhaité l’utiliser dans le cadre de ma spécialisation, Traitement d’image et reconnaissance d’image. <br>
Après plusieurs semaine d’essaye, j’ai décidé d’abandonner cette carte et de revenir sur mon Raspberry Pi 3B+, pourquoi ? <br>

|➕|➖|
|:---|:---|
|Grande puissance de calcul.|Difficile est mettre en place et à installer.|
||La carte ne fonctionne que sur son OS créer par Nvidia basé sur linux.|
||Impossible d’accéder à la caméra on-board avec open CV.|
||Prix très élevé.|
||Manque de documentation.|

<h2>Coral USB accelerator </h2>

<h3>Présentation </h3>

Voici l'USB accelerator de Coral.

<p> <img src="https://raw.githubusercontent.com/Forestierr/Opencv-reconnaissance/main/1_Documentation/img/coral_USB_accelerator.jpg"  width="350" height="250"> </p>

Coral USB Accelerator est un module externe vous ajoutant un coprocesseur Edge TPU vous réalisant l’entièreté de vos calculs en rapport à l’intelligence artificiel à grande vitesse est avec un très petit délai. <br>
Ce boitier développer par Coral (Google), fonctionne avec Linux, Mac et Windows. Il est aussi compatible avec Tensorflow lite et disponible aux prix de ~60 CHF sur Farnell. <br>

<h2>OAK-D </h2>

<h3>Présentation </h3>

La caméra OAK-D embarque 3 caméras. Une central de 12MP et deux autre caméra de 1MP répartie de part est d'autre de la première. La caméra central est RGB, permettant une detection de couleur, les deux autre sont elle uniquement en noir et blanc.

Ces trois caméras se trouvent dans un boitier métallique servant aussi de radiateur. Elles peuvent être alimentée soit uniquement par USB (attention moins de puissance) ou avec l'adaptateur secteur 5V 3A (avec un câble adapté).

<p> <img src="https://raw.githubusercontent.com/Forestierr/Opencv-reconnaissance/main/1_Documentation/img/OAK-D.jpg"  width="350" height="381"> </p>

| |Color Camera|	Stereo Camera Pair|
:---- |:--- |:----|
|Shutter Type|Rolling Shutter|Sync Global Shutter|
|Image Sensor|IMX378|OV9282|
|Max Framerate|60fps|120fps|
|H.265 Framerate|30fps|120fps|
|Resolution|12MP (4056x3040 px/1.55um)|1MP (1280x800 px/3um)|
|Field of View|81° DFoV - 68.8° HFoV|81° DFoV - 71.8° HFoV|
|Lens Size|1/2.3 Inch|1/2.3 Inch|
|Focus|8cm - ∞(AutoFocus)|19.6cm - ∞(FixedFocus)|
|F-number|2.0|2.2|

<h2> </h2>
    
<div align="center">
    <i>Robin Forestier</i>
</div>
