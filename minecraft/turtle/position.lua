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

local direction = {
    NORTH = 0,
    EAST = 1,
    SOUTH = 2,
    WEST = 3
}

if turtle.position == nil then
    turtle.position = vector.new(0, 0, 0)
end
if turtle.facing == nil then
    -- Assumption, correct later
    turtle.facing = direction.NORTH
end

turtle.getFacing = function()
    return turtle.facing
end

turtle.getPosition = function()
    return turtle.position
end

turtle.setPosition = function(position)
    turtle.position = position
end

local function onUp()
    turtle.setPosition(
        turtle.getPosition():add(
            vector.new(0, 1, 0)
        )
    )
end

local function onDown()
    turtle.setPosition(
        turtle.getPosition():sub(
            vector.new(0, 1, 0)
        )
    )
end

eventBus.subscribe('turtle_move_up', onUp)
eventBus.subscribe('turtle_move_down', onDown)
