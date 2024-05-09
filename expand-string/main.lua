local function expand(s)
  return (string.gsub(s, "$(%w+)", _G))
end

Code = "Code";
Status = "great"

print(expand("$Code is $Status, isn't it?"))
