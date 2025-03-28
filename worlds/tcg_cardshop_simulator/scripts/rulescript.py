def convert_file(input_file, output_file, start_number=60):
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for index, line in enumerate(lines):
            # Extracting the hex ID and item name using string manipulation
            parts = line.strip().split(", ")
            if len(parts) < 2:
                continue  # Skip malformed lines

            hex_id = parts[0].split("(")[1]  # Extracts 0x1F280021
            item_name = parts[1].strip('"')  # Extracts "Premium Collection Book"

            # Formatting the new output line
            formatted_line = f"{{{start_number + index}, ({hex_id}, \"{item_name}\", 1, 0x) }},\n"

            # Writing to output file
            outfile.write(formatted_line)


# Usage example
input_file = "inconvert.txt"  # Change this to your actual input file
output_file = "outconvert.txt"  # Change this to your desired output file
convert_file(input_file, output_file)