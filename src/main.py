from pose_class import BodyPose
from string_instrument import StringInstrument


inst = StringInstrument('ukulele')

bp = BodyPose()

can_strum = True

while bp.isOpened():
    results = bp.get(draw = False)

    arm_angles = bp.find_arm_angle(results)
    if arm_angles is not None:
        print(arm_angles)

        if (arm_angles[1] > 45 and arm_angles[1] < 135) and can_strum:
            inst.strum_tuned()
            can_strum = False
        elif (arm_angles[1] < 45):
            can_strum = True
        # elif (arm_angles[1] > 135):
        #     can_strum = True
        

        


bp.release()