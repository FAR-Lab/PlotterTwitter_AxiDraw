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
3. [Demo and Review](#3.0)

------------
<a name="1.0"></a>
## 1. Introduction
Interpersonal relationships are based on communication and collaboration. Is it possible for nonanthropomorphic robots to communicate using nonverbal signals? The paper investigates whether people's perceptions of mobile robot status or behavior could be influenced by their motion style. Using concepts from body language and pen movement, we developed motion styles across some scenarios, to observe how a robot’s dominance status affects human behaviors through nonverbal expression. At the demo, we used the AxiDraw pen plotter robot.   

#### Objective
The paper wants to test the hypothesis that robots that use nonverbal expressions can influence the behavior of a human.

#### Relevance

The number of robots involved in communication is growing exponentially [1], and that number will continue to increase as new applications of their communication abilities are developed. Social robots [2, 3] interact effectively with people in a public setting for example, hotels [4, 5], malls [6, 7], airports [8, 9], hospitals [10], urban [11] or schools [13,14,15]. Co-bots [16, 17] in a production plant, as well as smart toys [18] and autonomous cars [19].


------------
<a name="2.0"></a>
## 2. Environment Setup
### AxiDraw Installation
#### Software Installation
1\. The project uses Python 3.7.

2\. Install the environment of the AxiDarw using this [guide](https://axidraw.com/doc/py_api/#installation)  
For more troubleshoot and support click [here](https://cdn.evilmadscientist.com/dl/ad/public/AxiDraw_Guide_v571.pdf) 
2.1\. **change** the axidarw.py, which you install with the one that in the scripts folder

3\. Next, set up Dynamixel SDK, using the command:
```sh
 pip install dynamixel-sdk
```
4\. Then, install the dependencies, using the command:
```sh
 pip install PyQt5 qdarkstyle evdev
```

#### Hardware Installation

</p>
<p align="center">
<img src="figs/intro/Axidraw_kit.jpg" alt="" width="51%">
</p>

1\. Use this [guide](https://evilmadscience.s3.us-east-1.amazonaws.com/dl/ad/public/AxiDraw_MiniKit_v1.pdf) to assemble the AxiDarw  
!!! Important: from part 4.13 in the assembly guide use these parts. 
Now you should be in this step:
</p>
<p align="center">
<img src="figs/intro/2.1.jpg" alt="" width="20%">
</p>

2\. Next, 3D print the 4 parts:
</p>
<p align="center">
<img src="figs/intro/parts.jpg" alt="" width="20%">
</p>

  2.1 Holder first motor
  </p>
<p align="center">
<img src="figs/intro/part2.1.jpg" alt="" width="20%">
</p>
  2.2 Holder first motor
  </p>
<p align="center">
<img src="figs/intro/part2.2.jpg" alt="" width="20%">
</p>
  2.3 holder plate
  </p>
<p align="center">
<img src="figs/intro/part2.3.jpg" alt="" width="20%">
</p>
  2.4 Connector plate for motor
</p>
<p align="center">
<img src="figs/intro/part2.4.jpg" alt="" width="20%">
</p>
</p>

3\. Put one of the M4×12 Torx Tapping Screws on the tip of the Torx L-wrench and then insert it through part 2.1. 
 
 Do the same with the other one.

</p>
<p align="center">
<img src="figs/intro/3.jpg" alt="" width="20%">
</p>
</p>

!!! Important - threaded the wires before you connect the motor sometimes it's hard to connect them to the motor when it is screwed. 
</p>
<p align="center">
<img src="figs/intro/3.1_importent.jpg" alt="" width="20%">
</p>
</p>

</p>
<p align="center">
<img src="figs/intro/3.2_importent.jpg" alt="" width="20%">
</p>
</p>
4. Then, connect one of the Dynamixel motor 1 to the connector by using the screws supplied with the motor.


</p>
<p align="center">
<img src="figs/intro/4.jpg" alt="" width="20%">
</p>
</p>

5\. Connect part 2.3 using M2×2 
</p>
<p align="center">
<img src="figs/intro/5.jpg" alt="" width="20%">
</p>
</p>

!!! important - the first motor should be in the position of 180 degrees you can use [this](https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/) to communicate the motor manually

6\. New, connect part 2.2 using M1.5×3 using M1.5 Allen key.


</p>
<p align="center">
<img src="figs/intro/6.jpg" alt="" width="20%">
</p>
</p>

7\. Take part 2.4 and connect it to the second Dynamixel motor using the screws which supplied with the motor.

</p>
<p align="center">
<img src="figs/intro/7_before.jpg" alt="" width="20%">
</p>
</p>

</p>
<p align="center">
<img src="figs/intro/7_after.jpg" alt="" width="20%">
</p>
</p>

!!! Important - try to rotate the motor after you screw the bolts if you can't unscrew them slowly until you can.

8\. Connect the Dynamixel 2 motor to the connector by using the screws which supplied with the motor.

</p>
<p align="center">
<img src="figs/intro/2.4.jpg" alt="" width="20%">
</p>
</p>

9\. Now, go back to step 4.13 in the [guide](https://evilmadscience.s3.us-east-1.amazonaws.com/dl/ad/public/AxiDraw_MiniKit_v1.pdf) and finish the assembly. 
 </p>
<p align="center">
<img src="figs/intro/9.jpg" alt="" width="20%">
</p>
</p>

 </p>
<p align="center">
<img src="figs/intro/9.1.jpg" alt="" width="20%">
</p>
</p>

Now the robot needs to look like that.

 </p>
<p align="center">
<img src="figs/intro/9.2.jpg" alt="" width="20%">
</p>
</p>

10\. The last step is to connect the wires to the controllers.

 10.1 The white connector goes to the U2D2.
 </p>
<p align="center">
<img src="figs/intro/10.jpg" alt="" width="20%">
</p>
</p>

 10.2 The electric wires go one to the V_pin and one to the ground as you can see in the figure below.
</p>
<p align="center">
<img src="figs/intro/10.1.jpg" alt="" width="20%">
</p>
</p>

 </p>
<p align="center">
<img src="figs/intro/10.2.jpg" alt="" width="20%">
</p>
</p>

 10.3 The other direction of the wires go to motor 2 as the figure below.
</p>
<p align="center">
<img src="figs/intro/10.3.jpg" alt="" width="20%">
</p>
</p>

#### Testing
To test the installation run the test.py 

------------
<a name="3.0"></a>

## Demo and Review

------------

## References
1. World Service Robots. International Federation of Robotics, 2019.
2. Leite I, Martinho C, Paiva A. Social robots for long-term interaction: a survey. Int J Soc Robot. 2013;5(2):291–308.
3. • Breazeal C, Dautenhahn K, Kanda T. Social robotics. In: Springer handbook of robotics: Springer; 2016. p. 1935–72.
4. Pinillos R, Marcos S, Feliz R, Zalama E, Gómez-García-Bermejo J. Long-term assessment of a service robot in a hotel environment. Robot Auton Syst. 2016;79:40–57.
5. Yu C-E. Humanlike robots as employees in the hotel industry: thematic content analysis of online reviews. J Hosp Mark Manag. 2020;29(1):22–38.
6. Sabelli AM, Kanda T. Robovie as a mascot: a qualitative study for long-term presence of robots in a shopping mall. Int J Soc Robot. 2016;8(2):211–21.
7. Niemelä M, Heikkilä P, Lammi H, Oksman V. Shopping mall robots–opportunities and constraints from the retailer and manager perspective. In: International Conference on Social Robotics: Springer; 2017. p. 485–94.
8. Nielsen S, Bonnerup E, Hansen AK, Nilsson J, Nellemann LJ, Hansen KD, Hammcrshoi D. Subjective experience of interacting with a social robot at a Danish airport1. In 2018 27th IEEE International Symposium on Robot and Human Interactive Communication (RO-MAN); 2018. p. 1163–1170.
9. Tonkin M, Vitale J, Herse S, Williams M-A, Judge W, Wang X. Design methodology for the UX of HRI: a field study of a commercial social robot at an airport. In Proceedings of the 2018 ACM/ IEEE International Conference on Human-Robot Interaction; 2018. p. 407–415.
10. 
11. F Bu, I Mandel, WY Lee, W Ju, "Trash Barrel Robots in the City", 2023 ACM/IEEE International Conference on Human-Robot, p. 875-877
12. 
13. Alonso SG, Hamrioui S, de la Torre Díez I, Cruz EM, López- Coronado M, Franco M. Social robots for people with aging and dementia: a systematic review of literature. Telemed J E Health. 2019;25(7):533–40.
14. Kachouie R, Sedighadeli S, Khosla R, Chu M-T. Socially assistive robots in elderly care: a mixed-method systematic literature review. Int J Hum Comput Interact. 2014;30(5):369–93.
15. Broadbent E, Stafford R, MacDonald B. Acceptance of healthcare robots for the older population: review and future directions. Int J Soc Robot. 2009;1(4):319.
16. Sherwani F, Asad MM, Ibrahim BSKK. Collaborative robots and industrial revolution 4.0 (ir 4.0). In 2020 International Conference on Emerging Trends in Smart Technologies (ICETST). IEEE; 2020. p. 1–5.
17. Terzioğlu Y, Mutlu B, Sahin E. Designing social cues for collaborative robots: the role of gaze and breathing in human-robot collaboration.
In: Proceedings of the 2020 ACM/IEEE International Conference on Human-Robot Interaction, HRI 20. New York: Association for Computing Machinery; 2020. p. 343357.
18. Hobby Products Report 2018 - Toys and games. Statista. 2019.
19. Basu C, Singhal M. Trust dynamics in human autonomous vehicle interaction: a review of trust models. In 2016 AAAI Spring Symposium Series; 2016.

