local function word_count(s)
  local counter = {}
  for line in s do
    for word in string.gmatch(line, "%w+") do
      counter[word] = (counter[word] or 0) + 1
    end
  end
end

word_count("Ola, tudo bem? pq você fez isso pq?")
