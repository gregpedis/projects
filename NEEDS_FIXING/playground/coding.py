alphabet = {
    "A" : "00",
    "B" : "01",
    "C" : "10",
    "D" : "11",
}


def convert(input_stuff):
    output_stuff = [alphabet[x] for x in input_stuff]
    return '-'.join(output_stuff)


input_data = "AAAABDCACD"
output_data = convert(input_data)
print('-'.join(input_data))
print(output_data)
