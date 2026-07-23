#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from imoto_equipment.press_machine_operator_mock import HeatpressOperatorMock
from imoto_equipment.press_machine_operator_mock import ColdpressOperatorMock


def main():
    rospy.init_node('press_machine_operator_mock_node', anonymous=True)

    # Generate instance
    hp_operator_mock = HeatpressOperatorMock()
    cp_operator_mock = ColdpressOperatorMock()

    # Run
    rospy.spin()


if __name__ == '__main__':
    main()
