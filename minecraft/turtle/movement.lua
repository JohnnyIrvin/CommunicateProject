-- Copyright (c) 2021 Johnathan P. Irvin
-- 
-- Permission is hereby granted, free of charge, to any person obtaining
-- a copy of this software and associated documentation files (the
-- "Software"), to deal in the Software without restriction, including
-- without limitation the rights to use, copy, modify, merge, publish,
-- distribute, sublicense, and/or sell copies of the Software, and to
-- permit persons to whom the Software is furnished to do so, subject to
-- the following conditions:
-- 
-- The above copyright notice and this permission notice shall be
-- included in all copies or substantial portions of the Software.
-- 
-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
-- EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
-- MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
-- NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
-- LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
-- OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
-- WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
require('minecraft.event_bus')

local origTurtle = {
    forward = turtle.forward,
    back = turtle.back,
    up = turtle.up,
    down = turtle.down,
    turnLeft = turtle.turnLeft,
    turnRight = turtle.turnRight
}

local function movementFactory(func, event)
    local function generatedFunction(repetitions)
        for i = 1, repetitions or 1, 1 do
            local success, msg = func()
    
            if not success then
                return success, msg, i - 1
            end

            if event then
                eventBus.publish(event)
            end
        end
    
        return true, nil, repetitions
    end

    return generatedFunction
end

turtle.forward = movementFactory(origTurtle.forward, 'turtle_move_forward')
turtle.back = movementFactory(origTurtle.back, 'turtle_move_back')
turtle.up = movementFactory(origTurtle.up, 'turtle_move_up')
turtle.down = movementFactory(origTurtle.down, 'turtle_move_down')
turtle.turnLeft = movementFactory(origTurtle.turnLeft, 'turtle_turn_left')
turtle.turnRight = movementFactory(origTurtle.turnRight, 'turtle_turn_right')

turtle.turnAround = function()
    return turtle.turnLeft(2)
end
