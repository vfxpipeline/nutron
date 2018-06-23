"""
Name: Nuke Operations
Author :  Rajiv Sharma
Developer Website : www.technicaldirector.in
Developer Email   : rajiv@technicaldirector.in
Date Started : 23 JUNE 2018
Date Modified :
Description :

Source Code Website : https://github.com/vfxpipeline/nutron
Free Video Tutorials : www.youtube.com/vfxpipeline

Copyright (c) 2018, RAJIV SHARMA(www.TechnicalDirector.in) . All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

    * Neither the name of RAJIV SHARMA(www.TechnicalDirector.in) nor the names of any
      other contributors to this software may be used to endorse or
      promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
__author__ = 'Rajiv Sharma'

from nuke.rotopaint import *


def create_rotopaint_node():
    """
    This function will set control point data for nuke bezier curve
    :return:
    """
    rotopaint_node = nuke.nodes.RotoPaint()

    # get the RotoPaint Curve list knob
    curve = rotopaint_node['curves']

    # get the Root layer of the curve list
    root_layer = curve.rootLayer

    # create a layer
    layer = Layer(curve)

    # append the layer to the root
    root_layer.append(layer)

    # create a bezier shape
    p1 = ShapeControlPoint()
    p2 = ShapeControlPoint()
    p3 = ShapeControlPoint()
    p4 = ShapeControlPoint()
    p1.center.setPosition(CVec2(100, 100))
    p2.center.setPosition(CVec2(100, 400))
    p3.center.setPosition(CVec2(400, 400))
    p4.center.setPosition(CVec2(400, 100))

    # create new shape
    curve_shape = Shape(curve)

    all_control_points = [p1, p2, p3, p4]
    for point in all_control_points:
        curve_shape.append(point)

    # append the bezier shape to the layer
    layer.append(curve_shape)


create_rotopaint_node()
