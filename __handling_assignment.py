with open("my_file.txt", "a") as file:
    file.write("hello this is my number:08108591615\n")
    file.write("i know you have 300 bucks\n")
    file.write("but i will make do with what i have")
    
    
with open("my_file.txt",  "r" ) as file_1:
    print(file_1.read())
    

with open("my_file.txt", "a") as file_2:
    file_2.write("\n This is my final lapse")        