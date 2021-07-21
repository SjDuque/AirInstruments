from pose_class import BodyPose
from string_instrument import StringInstrument
import fluidsynth


inst = StringInstrument('ukulele')

bp = BodyPose()

can_strum = True

while bp.isOpened():
    results = bp.get()

    arm_angles = bp.find_arm_angle(results)
    if arm_angles is not None:
        # print(arm_angles)
        
        if (arm_angles[1] > 90) and can_strum:
            inst.strum_tuned()
            can_strum = False
        elif (arm_angles[1] < 60):
            can_strum = True
        # elif (abs(arm_angles[1] - 120) < 10):
        #     can_strum = True
        

        


bp.release()