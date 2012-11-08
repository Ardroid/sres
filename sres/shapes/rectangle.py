# -*- coding: utf-8 -*-

import numpy as np

class Rectangle(object): # TODO: let's cython this.
  def __init__(self, top, left, width, height):
    self._matrix = np.matrix([
      [top, top, top+height, top+height, left+width/2.0],
      [left, left+width, left, left+width, top+height/2.0]
    ])

    self._width = width
    self._height = height

    self.__get_attr_map = {
      "width" : lambda: self._width,
      "height" : lambda: self._height,
      "topleft" : lambda: (self._matrix.item((0, 0)), self._matrix.item((1, 0))),
      "topright" : lambda: (self._matrix.item((0, 1)), self._matrix.item((1, 1))),
      "bottomleft" : lambda: (self._matrix.item((0, 2)), self._matrix.item((1, 2))),
      "bottomright" : lambda: (self._matrix.item((0, 3)), self._matrix.item((1, 3))),
      "location" : lambda: (self._matrix.item(0, 4), self._matrix.item((1, 4))),
      "x" : lambda: self._matrix.item((0, 4)),
      "y" : lambda: self._matrix.item((1, 4)),
      "topleft_m" : lambda: self._matrix[:, 0],
      "topright_m" : lambda: self._matrix[:, 1],
      "bottomleft_m" : lambda: self._matrix[:, 2],
      "bottomright_m" : lambda: self._matrix[:, 3],
      "location_m" : lambda: self._matrix[:, 4],
    }

  def __getattr__(self, name):
    return self.__get_attr_map[name]()

  def set_width(self, width):
    pass

  def set_height(self, height):
    pass

  def set_x(self, x):
    pass

  def set_y(self, y):
    pass

  def set_topleft(self, topleft):
    pass

  def set_topright(self, topright):
    pass

  def set_bottomleft(self, bottomleft):
    pass

  def set_bottomright(self, bottomright):
    pass

  def set_location(self, location):
    pass

  def set_topleft_m(self, topleft_m):
    pass

  def set_topright_m(self, topright_m):
    pass

  def set_bottomleft_m(self, bottomleft_m):
    pass

  def set_bottomright_m(self, bottomright_m):
    pass

  def set_location_m(self, location_m):
    pass

  def __setattr__(self, name, value):
    pass


  def rotate(self, theta):
    """rotate the rectangle counterclockwise. Theta given in radians.

    Rotation is done in place."""

    R = np.matrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    self._matrix = R * self._matrix

  def collidepoint(self, point):
    pass

  def colliderect(self, rect):
    pass