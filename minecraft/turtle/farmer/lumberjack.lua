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
require('minecraft.turtle.placement')

lumberjack = {}

local function waitForLog()
    local hasBlock, block = true, {}
    while hasBlock == true and block.name ~= 'minecraft:log' do
        hasBlock, block = turtle.inspect()
        os.sleep(1)
    end

    return hasBlock and block.name == 'minecraft:log'
end

lumberjack.plant = function()
    return turtle.place(nil, 'minecraft:sapling')
end

lumberjack.harvest = function()
    local success = waitForLog()
    if not success then
        return false, "Unable to detect solid block."
    end

    local up = 0
    local hasBlock, block = turtle.inspect()
    while hasBlock == true and block.name == 'minecraft:log' do
        turtle.dig()
        turtle.digUp()
        turtle.up()
        hasBlock, block = turtle.inspect()
        up = up + 1
    end

    turtle.down(up)
end