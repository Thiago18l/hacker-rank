--[@array is a list of integers
-- @num is the number that we want to find]
local function find(array, num)
  local found = 0
  for i = 1, #array do
    if array[i] == num then
      found = i
      break
    end
  end
  print("found in index: ", found)
end

find({ 2, 2, 3, 4 }, 4)
