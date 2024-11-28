import pytest
import main

main.debug = False

def test_gen():
    tfe = main.TwentyFortyEight()
    for x in range(4):
        for y in range(4):
            tfe.set_block(x,y,2)
            print("setting block x,y,value:",x,y,2)
    tfe.set_block(1,2,0)
    tfe.set_block(2,3,0)
    blank_blocks = main.find_empty_blocks(tfe.GAME_BOARD)
    assert blank_blocks == [[1,2],[2,3]]

def test_move_up():
    tfe = main.TwentyFortyEight()
    for x in range(4):
        for y in range(4):
            tfe.set_block(x,y,0)
    tfe.set_block(0,0,0)
    tfe.set_block(1,0,2)
    tfe.set_block(2,0,4)
    tfe.set_block(0,1,2)
    tfe.set_block(1,1,4)
    tfe.set_block(2,1,2)
    tfe.set_block(0,2,2)
    tfe.set_block(2,2,2)
    tfe.set_block(3,2,2)
    tfe.set_block(0,3,4)
    tfe.set_block(1,3,4)
    tfe.set_block(2,3,4)
    tfe.move("up")
    assert tfe.get_block(0,0) == 4
    assert tfe.get_block(1,0) == 2
    assert tfe.get_block(2,0) == 4
    assert tfe.get_block(3,0) == 2
    assert tfe.get_block(0,1) == 4
    assert tfe.get_block(1,1) == 8
    assert tfe.get_block(2,1) == 4
    assert tfe.get_block(2,2) == 4

def test_move_down():
    tfe = main.TwentyFortyEight()
    for x in range(4):
        for y in range(4):
            tfe.set_block(x,y,0)
    tfe.set_block(0,0,0)
    tfe.set_block(1,0,2)
    tfe.set_block(2,0,4)
    tfe.set_block(0,1,2)
    tfe.set_block(1,1,4)
    tfe.set_block(2,1,2)
    tfe.set_block(0,2,2)
    tfe.set_block(2,2,2)
    tfe.set_block(3,2,2)
    tfe.set_block(0,3,4)
    tfe.set_block(1,3,4)
    tfe.set_block(2,3,4)
    tfe.move("down")
    assert tfe.get_block(0,2) == 4
    assert tfe.get_block(0,3) == 4
    assert tfe.get_block(1,2) == 2
    assert tfe.get_block(1,3) == 8
    assert tfe.get_block(2,1) == 4
    assert tfe.get_block(2,2) == 4
    assert tfe.get_block(2,3) == 4
    assert tfe.get_block(3,3) == 2
    