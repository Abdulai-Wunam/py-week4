# Program to read a file, process its content, and write results to a new file

# Creating input.txt with at least five lines of text
with open("input.txt", "w") as file:
    file.write("Python is powerful.\n")
    file.write("It is widely used in data science.\n")
    file.write("HTML and CSS are important for web development.\n")
    file.write("Statistics helps in data analysis.\n")
    file.write("Machine learning is the future of AI.\n")

# Reading the contents of input.txt
with open("input.txt", "r") as file:
    content = file.read()

# Counting the number of words
words = content.split()
word_count = len(words)

# Converting text to uppercase
uppercase_content = content.upper()

# Writing processed text and word count to output.txt
with open("output.txt", "w") as file:
    file.write(uppercase_content + "\n")
    file.write(f"Word Count: {word_count}\n")

# Step 6: Print success message
print(" Processing complete! The file 'output.txt' has been created.")
