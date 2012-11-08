# -*- coding: utf-8 -*-
import uuid

class ZeroRobot(object):
  """ZeroRobot is a Robot that is a point (0 dimensional). It is also a base
  class for all other robots.

  Some object variables:
    .id: The id of the robot.
    .hitbox: The hitbox of the robot. Must define the function
             .collidepoint(x, y), colliderect(Rect). Same as the pygame.Rect
             method. Right now only supports pygame.Rect and the ZeroRobot
             Point, as if we want to collide different shapes, we need
             a more sane interface. Must have .centerx and .centery
  """ # TODO: advanced hitbox

  class ZeroHitbox(object):

    def __init__(self, x, y):
      self.centerx = int(x)
      self.centery = int(y)

    def collidepoint(self, x, y):
      if x == self.centerx or y == self.centery:
        return True
      return False

    def colliderect(self, rect):
      if isinstance(rect, self.__class__):
        return self.collidepoint(rect.centerx, rect.centery)
      return rect.collidepoint(self.centerx, self.centery)

  def __init__(self, x, y, sensors, id=None):
    """Initializes a new instance of the ZeroRobot

    Args:
      x: the starting x location. Center of the robot.
      y: the starting y location. Center of the robot.
      sensors: a list of sensors
      id: Am identifier. Otherwise it is randomly generated as an uuid4 hex
    """
    self.hitbox = self.ZeroHitbox(x, y)
    self.sensors = sensors
    self.id = id if id else uuid.uuid4().hex

  def get_all_sensor_data(self):
    """Gets all the sensor data and """