local function sum(a)
  local total = 0
  for i = 1, #a do
    total = total + a[i]
  end
  return total
end

local function minimum(min_value, next)
  if next ~= nil and next < min_value then
    return next
  end
  return min_value
end

local function min_max(array)
  local total_sum = sum(array)
  local min = array[1]
  local max = array[1]

  for i = 1, #array do
    max = math.max(max, array[i])
    min = minimum(min, array[i] ~= max and array[i] or min)
  end

  local min_sum = total_sum - max
  local max_sum = total_sum - min

  return min_sum, max_sum
end

local min, max = min_max({ 1, 3, 5, 7, 9 })
print(min, max)
