file_name = "data.txt"
file = io.open(file_name, "rb")

if file then 
    file:close()
else
    print("File not found") 
    return 
end

elves = {}
elves_counter = 0
cal = 0
for line in io.lines(file_name) do 
    if line == "" then 
        elves[elves_counter] = cal
        elves_counter = elves_counter+1
        cal = 0 
    else
        cal = cal + tonumber(line)
    end
end

print(math.max(table.unpack(elves)))
