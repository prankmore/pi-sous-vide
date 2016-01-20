Latest news

# Introduction #
Here you will find updates on how the project is going.

# Details #

After finally getting my Raspberry Pi at the end of last week, and playing around with kernel images etc. I am now ready to continue development.

First up is the USB Thermometer.

I have done a little bit of playing around using the code from http://www.isp-sl.com/pcsensor-1.0.0.tgz

Which in turn is based on http://relavak.wordpress.com/2009/10/17/temper-temperature-sensor-linux-driver/

In addition using the changes from
http://relavak.wordpress.com/2009/10/17/temper-temperature-sensor-linux-driver/#comment-283

This seems to basically work giving me both temperatures from my usb thermometer (tested on a Linux Virtual machine).

However rather than converting this to python, I think I am going to wrap this into a FUSE filesystem.
The file system will have a single folder containing 4 files.
InnerC, InnerF, OuterC, OuterF
Reading from one of these files will return the current temperature.
This will allow things like
cat temper/InnerC which would display a rolling log of the current temperature.
Or cp temper/InnerC which will create a file containing the values.
This will make the python code to read the temperature very simple as it simply reads it from a file.

Stay tuned for further updates!