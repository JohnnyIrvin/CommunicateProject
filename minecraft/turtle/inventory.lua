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

local origTurtle = {
    select = turtle.select,
    getItemDetail = turtle.getItemDetail
}

turtle.select = function(slot) 
    slot = slot or 1

    if slot < 1 or slot > 16 then
        return false
    end

    return origTurtle.select(slot)
end

turtle.getItemDetail = function(slot, detailed)
    local detail = origTurtle.getItemDetail(slot, detailed)

    if detail == nil then
        return {}
    end

    return detail
end

turtle.inventory = function()
    local currentSlot = 0
    return function()
        currentSlot = currentSlot + 1

        if currentSlot > 16 then
            return
        end

        if turtle.getItemCount(currentSlot) ~= 0 then
            return currentSlot, turtle.getItemDetail(currentSlot, true)
        end
    end
end

turtle.selectItem = function(name)
    for slot, item in turtle.inventory() do
        if item.name == name then
            turtle.select(slot)
            return slot, item
        end
    end

    return
end

turtle.hasItem = function(name)
    local slot = turtle.selectItem(name)

    if slot ~= nil then
        return true
    end

    return false
end
