# PlotterTwitter_AxiDraw
In this repository, you will find AxiDraw's program and documentation. A guide to moving it and drawing with it.

<!--pic of AxiDraw-->

<p align="center">
<b><i>Interaction between humans and robots behavior </i></b>
</p>

<p align="center">
<img src="figs/intro/Axidraw.jpg" alt="" width="51%">
</p>


<p align="center">
<b> Alexandra Bremers & Itay Grinberg </b>
<br>
<a href="mailto:itaygrinberg@campus.technion.ac.il" target="_top">itaygrinberg@campus.technion.ac.il</a>
</p>
<p align="center">
<a href="mailto:awb227@cornell.edu" target="_top">awb227@cornell.edu</a>
</p>

<a id="top"></a>
## Contents
1. [Introduction](#1.0)
2. [Environment Setup](#2.0)
3. [Theoretical Background](#3.0)
4. [Demo and Review](#4.0)

------------
<a name="1.0"></a>
## 1. Introduction

#### Objective


#### Relevance

------------
<a name="2.0"></a>
## 2. Environment Setup
### AxiDraw Installation
#### Software Installation
1\. The project uses Python 3.7.

2\. Install the environment of the AxiDarw using this [guide](https://axidraw.com/doc/py_api/#installation)  
for mor trubleshout and support click [here](https://cdn.evilmadscientist.com/dl/ad/public/AxiDraw_Guide_v571.pdf) 
3\. Next, set up Dynamixel SDK, using the command:
```sh
 pip install dynamixel-sdk
```
4\. Then, install the dependencies, using the command:
```sh
 pip install PyQt5 qdarkstyle evdev
```

#### hardware Installation

</p>
<p align="center">
<img src="figs/intro/Axidraw_kit.jpg" alt="" width="51%">
</p>

1\. Use this [guide](https://evilmadscience.s3.us-east-1.amazonaws.com/dl/ad/public/AxiDraw_MiniKit_v1.pdf) to assumble the AxiDarw  
!!! Importent: from part 4.13 in the assmbly guide use this parts. 
Now you sould be in this step:
</p>
<p align="center">
<img src="figs/intro/2.1.jpg" alt="" width="51%">
</p>

2\. Next, 3D print the 4 parts:
</p>
<p align="center">
<img src="figs/intro/parts.jpg" alt="" width="51%">
</p>

  2.1 holder first motor
  </p>
<p align="center">
<img src="figs/intro/part2.1.jpg" alt="" width="51%">
</p>
  2.2 holder first motor
  </p>
<p align="center">
<img src="figs/intro/part2.2.jpg" alt="" width="51%">
</p>
  2.3 holder plate
  </p>
<p align="center">
<img src="figs/intro/part2.3.jpg" alt="" width="51%">
</p>
  2.4 conector plate for motor
</p>
<p align="center">
<img src="figs/intro/part2.4.jpg" alt="" width="51%">
</p>
</p>

3\. Put one of the M4×12 Torx Tapping Screws on the tip of the Torx L-wrench and then insert it through part 2.1
    do the same with the other one.

</p>
<p align="center">
<img src="figs/intro/2.4.jpg" alt="" width="51%">
</p>
</p>

!!! Importent - threaded the wires before you conncet the motor somtimes its hard to connect them to the motor when it screwed. 

4\. Then, connect one of the Dynamixel 1 motor to the conector by using the screws which supply with the motor.

</p>
<p align="center">
<img src="figs/intro/2.4.jpg" alt="" width="51%">
</p>
</p>

5\. connect part 2.3 using M2×2 
</p>
<p align="center">
<img src="figs/intro/2.4.jpg" alt="" width="51%">
</p>
</p>

!!! importent - the frist motor sould be in the position of 180 degree you can use [this](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/) to communicate the motor manually

6\. New, connect part 2.2 using M1.5×3 use a M1.5 allen key.


</p>
<p align="center">
<img src="figs/intro/2.4.jpg" alt="" width="51%">
</p>
</p>

6\. Take part 2.4 and connect it to the second Dynamixel motor using the screws which supply with the motor.

</p>
<p align="center">
<img src="figs/intro/before.jpg" alt="" width="51%">
</p>
</p>

</p>
<p align="center">
<img src="figs/intro/after.jpg" alt="" width="51%">
</p>
</p>

!!! Importent - try to rutate the motor after you screw the bolts if you can't unscrew them slow until you can.

7\. Connect the Dynamixel 2 motor to the conector by using the screws which supply with the motor.

</p>
<p align="center">
<img src="figs/intro/2.4.jpg" alt="" width="51%">
</p>
</p>

8\. New, go back to step 4.13 in the [guide](https://evilmadscience.s3.us-east-1.amazonaws.com/dl/ad/public/AxiDraw_MiniKit_v1.pdf) and finish the assmbly. 

9\. Last step is to conncet the wires to the conntrolers.

 9.1 The white connector goes to the U2D2.
 </p>
<p align="center">
<img src="figs/intro/2.4.jpg" alt="" width="51%">
</p>
</p>

 9.2 The electric wires goes one to the V_pin and one to the ground as you can see at the figure below.
</p>
<p align="center">
<img src="figs/intro/2.4.jpg" alt="" width="51%">
</p>
</p>

 9.3 The other direction of the wires goes to motor 2 as the figure below.
</p>
<p align="center">
<img src="figs/intro/2.4.jpg" alt="" width="51%">
</p>
</p>

#### Testing


------------

<a name="3.0"></a>
## 3. Theoretical Background

------------
<a name="4.0"></a>

## Demo and Review

------------

## References


