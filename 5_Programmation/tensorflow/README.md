<div align="center">
    <h1> Reconnaissance visuel </h1>
</div>


>  Release : [release](http://172.16.32.230/Forestier/reconnaissance-visuel/-/releases)

Vous trouverez ici tous les programmes que j'ai réalisé avec tensorflow.

<h2></h2>

Tensorflow est une plate-forme Open Source de bout en bout dédiée au machine learning dévelopée par Google. <br>
[Tenserflow](https://www.tensorflow.org) <br>
[GitHub](https://github.com/tensorflow)

<h2></h2>

Pour représenter la puissance de cette outils avec opencv,
voici le temps de traitement par image pour chacun des raspberry Pi.

|Board			|Raspberry 3 B+	|Raspberry 4 B	|
|:----:			|---:		|---:		|
|Tenserflow		|500 ms		|300 ms		|
|Tenserflow (lite)	|300 ms		|100 ms		|
|Coral USB Accelerator	|50 ms		|15 ms		|

> Coral USB Accelerator: <br>
Ce petit boitier branchable en USB au Raspberry, permet de réaliser l'entièreté des calcule 
en rapport avec l'inteligence artificiel permettant (en théorie) de diviser par 10 le temps de traitement.
Ce qui offre d'énorme avantage pour de la détéction poussée en temp réel, on passerait de ~2fps à ~20fps.
[Coral](https://coral.ia/products/accelerator/)


<h2></h2>
    
<div align="center">
    <i>Robin Forestier</i>
</div>