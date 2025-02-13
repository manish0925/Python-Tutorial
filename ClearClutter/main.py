import os
files=os.listdir("ClearClutter")
i=1
for file in files:
    print(file)
    if file.endswith(".jpg"):
        os.rename(f"ClearClutter/{file}",f"ClearClutter/{i}.jpg")
        i+=1