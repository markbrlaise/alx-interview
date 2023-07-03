#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    function to check if all boxes are unlockable
    """
    unlocked_boxes = []
    keys_list = []

    def get_keys(box):
        # function to get keys
        for key in box:
            if key not in keys_list:
                keys_list.append(key)
        unlocked_boxes.append(box)

    get_keys(boxes[0])

    def check_box(box):
        # function to check if a box is unlockable
        if (boxes.index(box) in keys_list) and box not in unlocked_boxes:
            get_keys(box)

    for key in keys_list:
        try:
            box = boxes[key]
            check_box(box)
        except Exception as e:
            continue

    if len(unlocked_boxes) == len(boxes):
        return True
    else:
        return False
