#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from imoto_equipment.cutter_operator import CutterOperator


def main():
    rospy.init_node('cutter_operator_node', anonymous=True)

    # Generate instance
    cutter_operator = CutterOperator()

    # Run
    rospy.spin()


if __name__ == '__main__':
    main()
