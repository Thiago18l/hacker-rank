local function match_date(date)
  local date_pattern = "%d%d/%d%d/%d%d%d%d"

  local match = string.match(date, date_pattern)

  if match then
    print("Valid date: " .. match)
  else
    print("Invalid date format")
  end
end

print(match_date("18/12/1997"))
