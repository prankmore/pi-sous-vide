Information on the USB Relay

# Introduction #

Information on the USB Relay
Bought from
[here](http://www.ecrater.co.uk/p/11853067/usb-relay-controller-one-channel?keywords=usb+relay)

Manual
[here](http://www.sigma-shop.com/manuals/USB1RELAY_manual.pdf)
# Details #

The relay arrived yesterday, so I have had a quick play with it in my lunch break today.

I fired up my linux virtual machine, plugged in the USB device and attached it to the virtual machine.
My first attempt at driving the relay didn't work. I was following the simple commandline echo to /dev/ttyUSB0 described in the manual. So I disconnected it from the VM and tried the downloadable test application running in windows. This worked fine so I guessed the issue lay in my comms port handling on linux.
First instinct suggested the baud rate, a quick look on their forum confirmed this as a possibility so I added a line to set the comms port baud rate.
```
stty -F /dev/ttyUSB0 9600
```
Then the commands work as described.
The line below works for turning the relay off and on for 10 seconds
```
for ((i=0;i<10;i++)) do echo -e '\xFF\x01\x01' > /dev/ttyUSB0;sleep 0.5;echo -e '\xFF\x01\x00' > /dev/ttyUSB0;sleep 0.5;done
```