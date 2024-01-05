from PIL import Image
import csv
import json

f=open("input.json")

data=json.load(f)

print(data)

x_start=data["care_areas"][0]["top_left"]["x"]
x_end=data["care_areas"][0]["bottom_right"]["x"]

y_start=data["care_areas"][0]["bottom_right"]["y"]
y_end=data["care_areas"][0]["top_left"]["y"]

for i in range(1,6):
    img=Image.open("wafer_image_{0}.png".format(i))
    
    img=img.convert('RGB')
    print(img)
    pixels=img.load()
    print(pixels)

    color_count={}

    for y in range(y_start,y_end):
        for x in range(x_start,x_end):
            color=pixels[x,y]

            if(color in color_count):
                color_count[color]+=1
            else:
                color_count[color]=1

    print(color_count)


    major={} 
    #for finding bg grey
    maxcol_count1=max(color_count.values())
    for key in color_count:
        if color_count[key]==maxcol_count1:
            major_col1=key #this is the color with occurs max times


    major[major_col1]=color_count.pop(major_col1)


    maxcol_count2=max(color_count.values())
    for key in color_count:
        if color_count[key]==maxcol_count2:
            major_col2=key #this is the color which occurs second-max times


    major[major_col2]=color_count.pop(major_col2)

    print("\n\n")
    print(major)

    #finding defect points

    defect_points=[]

    for y in range(y_start,y_end):
        for x in range(x_start,x_end):
            color=pixels[x,y]
            if(color not in major.keys()):
                defect_points.append((i,x,y_end-y-1))


    #writing into file
    with open("output.csv","a+") as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerows(defect_points)







