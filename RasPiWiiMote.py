import cwiid, time

button_delay = 0.1

print 'Please press buttons 1 + 2 on the Wiimote...'
time.sleep(1)

try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Connection failed!"
  quit()

print 'Connection established!\n'
print 'Go ahead and press some buttons\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

while True:

  buttons = wii.state['buttons']

  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)

  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)
