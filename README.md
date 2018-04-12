RasPiWiiMote
============

A simple Python script for controlling motors connected to a Raspberry Pi with a Wii Remote. If I recall correctly, I was using the L293D H-bridge IC (or similar) to drive the two motors, you definitely shouldn't try to connect motors directly to the logic pins on the Raspberry Pi.

This script relies on the cwiid Python module (run 'apt-get install libcwiid1' to install it) and a compatible USB bluetooth module. In my case, I was using a generic £1 nano bluetooth receiver from eBay which worked perfectly. Your mileage may vary.

I made this 4 years ago when I had little to none programming experience, don't judge. If I eventually get round to it, I might clean up the code a bit.
