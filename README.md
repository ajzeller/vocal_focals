# *Vocal* **Focals**

#### A wearable text recognition device for the visually impaired.

##### *Made using the Raspberry Pi and Google Cloud Vision API.*

[vocalfocals.com](https://vocalfocals.com)

---
This tutorial will walk through setting up a Raspberry Pi Zero W with the Google Cloud Vision API to detect text in an environment and then play that text

Ingredients you will need:
* 1 x Raspberry Pi Zero W
* 1 x microSD card
* 1 x microUSB cable
* 1 x [Raspberry Pi Camera Module v2](http://a.co/gOyJ8m6)
* 1 x [microUSB to USB adapter](http://a.co/eIHAlxn)
* 1 x [USB to audio adapter](http://a.co/1Pvllqo)


This tutorial will assume that you are working on a mac or linux computer.

If you have already setup your Raspberry Pi and installed git, jump to part 3 to set up VocalFocals.

#### 1) Raspberry Pi initial setup
With a factory Pi Zero W, you can follow [this tutorial](https://www.losant.com/blog/getting-started-with-the-raspberry-pi-zero-w-without-a-monitor) to first setup the Raspberry Pi.

If you are unable to connect to wifi following this tutorial, you can follow [this quick tutorial](https://blog.gbaman.info/?p=791) to ssh into your Raspberry Pi using USB-OTG.

Note that the factory credentials for the Raspberry Pi are:

```
Username: pi
Password: raspberry
```

#### 2) Raspberry Pi housekeeping

You will need to do some housekeeping on the Raspberry Pi.

```
Sudo raspi-config
```

In *Interfacing Options*, enable the camera, enable SSH, and enable VNC server if they are not already enabled.

[Install VNC viewer](https://www.realvnc.com/en/connect/download/viewer/) on your computer to remotely view the Raspberry Pi's screen.

#### 3) Install git on your Raspberry Pi
Create a [GitHub](https://github.com/) account.

```
$ sudo apt-get install git
```

Configure your name:

```
git config --global user.name "Your Name"
```

Configure your email:

```
git config --global user.email email@example.com
```



In the /home/pi/ directory, run:

```
git clone https://github.com/ajzeller/vocal_focals.git
```
