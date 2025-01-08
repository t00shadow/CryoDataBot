### Testing a new implementation of the 3 dependent comboboxes

### Comment below copied from main_guiv_DEV4.py
#! Dependent Spin Boxes
#  Spin Box rules:
#  I)    box1 + box2 + box3 = 100%
#  II)   0 <= box1 <= 100
#  III)  0 <= box2 <= 100
#  IV)   0 <= box3 <= 100
#
#  Funneling rules (i.e. which boxes to change first to main rule I):
#  A) When box1 changes, first adjust box3 until limit, and then box2
#  B) When box2 changes, first adjust box3 until limit, and then box1
#  C) When box3 changes, first adjust box1 until limit, and then box2
#
#  Translating to code:
#  We only know the new/changed value of a combo box, not it's initial. Instead think of having a pot of 100 percentage points, and then taking them out in a specific order. The combo box that got changed already took from the pot first.
#  i.e. A) When box1 changes, box1 takes that amount out of the pot (its new/changed value).
#          Then box2 takes from the remainder (as much of its original value as possible). 
#          Then box3 takes whatever's left.
#  ditto for B) and C):
#       B) 2 takes first, then 1, then 3
#       C) 3 takes first, then 1, then 2
#
#  In fact, all 3 cases are the same, it's just the the order of boxes that's different. So we can generalize it to:
#       X takes from the "pot" first, then Y, then Z. Where X, Y, Z can be box1, box2, box3 in whatever order.
#
#?  TLDR: put all percentage points in a "pot" and take them out in a specific order


### Holy shit my brain actually peaked (so much simpler than my previous dogshit solution). Just think of putting everything in the pot and then taking in a specific order. 

def test_dependent_spinboxes(box1_i = 100, box2_i = 0, box3_i = 0, box1_f = 100):
    assert(box1_i + box2_i + box3_i == 100)

    X = box1_f
    Y_i = box2_i

    rem_X = 100 - X
    Y = min(rem_X, Y_i)
    rem_Y = max(rem_X - Y, 0)
    Z = rem_Y

    box2_f = Y
    box3_f = Z

    assert(X + Y + Z == 100)
    assert(box1_f + box2_f + box3_f == 100)    # same thing, just checking assigned the right vals
    print(box1_f, box2_f, box3_f)
    # return box2_f, box3_f         # box1_f is already an input

test_dependent_spinboxes(10, 0, 90, 5)

test_dependent_spinboxes(80, 12, 8, 50)

test_dependent_spinboxes(0, 21, 79, 90)

test_dependent_spinboxes(80, 20, 0, 0)



# removing the intermediate variables since dont need them (had them their originally to have less confusing names since was gonna copy paste this 3 times into the gui code, but just gonna make a general fxn instead)
# removed X_i and Z_i because theyre not needed
def test_dependent_spinboxes_cosmeticedit(X_f = 100, Y_i = 0):
    rem_X = 100 - X_f       # rem for remainder
    Y_f = min(rem_X, Y_i)
    rem_Y = max(rem_X - Y_f, 0)
    Z_f = rem_Y

    assert(X_f + Y_f + Z_f == 100)
    print(X_f, Y_f, Z_f)
    # return Y_f, Z_f         # X_f is already an input

test_dependent_spinboxes_cosmeticedit(5, 0)

test_dependent_spinboxes_cosmeticedit(50, 12)

test_dependent_spinboxes_cosmeticedit(90, 21)

test_dependent_spinboxes_cosmeticedit(0, 20)