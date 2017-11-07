# *Vocal* **Focals**

#### A wearable text recognition device for the visually impaired.

##### *Made using the Raspberry Pi and Google Cloud Vision API.*

[vocalfocals.com](https://vocalfocals.com)

---
This tutorial will walk through setting up a Raspberry Pi Zero W with the Google Cloud Vision API to detect text in an environment and then relay that text to the wearer over audio.

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
sudo raspi-config
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

#### 4) Google Cloud Platform setup

To detect text in the image captured by the Raspberry Pi, we will use the Google Cloud Vision (GCV) API on the Google Cloud Platform. While this is a paid product, Google offers 1000 API calls for free each month, enough to experience the concept in action.

[Create a Google Cloud Platform account.](https://console.cloud.google.com/freetrial)

...

#### 5) Prepare the Raspberry Pi for GCV
In the /home/pi/ directory, run:

```
git clone https://github.com/ajzeller/vocal_focals.git
```

You will need to upgrade Pip, the package manager for python installations:

```
sudo pip install --upgrade pip
```

```
sudo apt-get install libjpeg8-dev
```
Next, you will install the Google API Python Client:

```
sudo pip install --upgrade google-api-python-client
```

Next, install Python Imaging Library:

```
sudo pip install --upgrade Pillow
```
Install Python PiCamera:

```
sudo apt-get install python-picamera
```

Install mpg321, a command line .mp3 player:
```
sudo apt-get -y install mpg321
```

*[API key JSON stuff here]*
