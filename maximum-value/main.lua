local function maximum(array)
  local mi = 1
  local mx = array[mi]
  for i = 1, #array do
    if array[i] > mx then
      mi = i; mx = array[i]
    end
  end
  return mx, mi
end

local mx, mi = maximum({ 8, 10, 23, 12, 5 })
print(mx, mi)
