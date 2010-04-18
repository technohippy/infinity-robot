# -*- coding: utf-8 -*-
import logging
from waveapi import robot
from waveapi import events
from waveapi import element
from waveapi import appengine_robot_runner

INFINITE_GADGET_URL = 'http://infinity-robot.appspot.com/infinite_gadget/%s'
class InfinityRobot(robot.Robot):
  def __init__(self):
    robot.Robot.__init__(self, 'Infinity',
      image_url = 'http://as-a-robot.appspot.com/assets/mirror.png'
    )
    self.register_handler(events.WaveletSelfAdded, self.add_infinite_gadget)

  def add_infinite_gadget(self, events, wavelet):
    wavelet.root_blip.append(element.Gadget(url=INFINITE_GADGET_URL % wavelet.wave_id))

if __name__ == '__main__':
  appengine_robot_runner.run(InfinityRobot())
