from pose_class import BodyPose
import string_instrument as si
import cv2
import sys

if __name__ == '__main__':
    draw_skel = True

    if len(sys.argv) > 1:
        if sys.argv[1] == 'false':
            draw_skel = False

    inst = si.StringInstrument('ukulele')
    bp = BodyPose()
    can_strum = True
    
    print("Drawing Skeleton:", draw_skel)
    print()
    for i in range(len(si.InstrumentData.List)):
        print("Press", i+1, "for", si.InstrumentData.List[i])
    print()

    while bp.isOpened():
        results = bp.get(draw=draw_skel)

        arm_angles = bp.find_arm_angle(results)
        if arm_angles is not None:
            # print(arm_angles) # used for testing

            if (arm_angles[1] > 45 and arm_angles[1] < 135) and can_strum:
                inst.strum_tuned()
                can_strum = False
            elif (arm_angles[1] < 45):
                can_strum = True
            # elif (arm_angles[1] > 135):
            #     can_strum = True

            # If/else statements for closing
            # application (esc) or change instrument

            key_press = cv2.waitKey(1)
            new_inst = None

            if key_press & 0xFF == 27:
                bp.release()
            elif key_press == ord('1'):
                new_inst = si.InstrumentData.List[0]
            elif key_press == ord('2'):
                new_inst = si.InstrumentData.List[1]
            elif key_press == ord('3'):
                new_inst = si.InstrumentData.List[2]
            elif key_press == ord('4'):
                new_inst = si.InstrumentData.List[3]
            if new_inst is not None:
                print("New Instrument:", new_inst)
                inst.choose_instrument(new_inst)

    bp.release()