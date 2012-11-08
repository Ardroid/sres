# -*- coding: utf-8 -*-

"""Sensor modules. The sensors are perfect here, but uncertain once passed
through the robot class."""

class BaseSensor(object):

  def __init__(self, world, x, y):
    self.x = x
    self.y = y
    self.world = world

  def get_data(self):
    raise NotImplementedError

class LaserRangeFinder(BaseSensor):

  def __init__(self, world, x, y, theta):
    BaseSensor.__init__(self, world, x, y)
    self.theta = theta

  def get_data(self):
    """This should get the current reading of the laser range finder given the
    current x, y, theta, and world.

    Returns:
      A perfect reading of the nearest obstacles. Floating point"""
    pass
