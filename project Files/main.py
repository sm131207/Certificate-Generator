from PIL import Image , ImageDraw , ImageFont
import datetime
import os
import sys

# Students List :

students = [
    "Aarav Sharma   ",
    "   riya Patil",
    " Aditya Kulkarni",
    "Ananya Deshmukh",
    " Vedant Joshi",
    "ishaan Mehta",
    "Sneha Pawar",
    "ARjun Desai",
    "Aditi More",
    "Rahul Jadhav",
    "Neha Shinde",
    "ROhan Chavan",
    "Kavya Nair",
    "Sneha Pawar",
    "Sakshi Bhosale",
    "Yash Thakur",
    "Priya Gaikwad",
    "Atharva Mane",
    "Tanvi Sawant",
    "Kunal Mahajan"
]


# Format Explanation :
print("This is to certify that Name {'__1> achevement__'} {'___2> Name of the compitation/Program/course___'} : ")

# Reciptant Name settings :

dummy_reciptant_name = "Student Name"
# name_coordinates = (At Main Code)
name_text_color = "#0B1F4B"

base_dir = os.path.dirname(os.path.abspath(__file__))
main_dir = os.path.dirname(base_dir)

name_font_style_path = os.path.join(base_dir, "fonts", "GreatVibes-Regular.ttf")
name_font = ImageFont.truetype(name_font_style_path,75)

# Certificate Issue Date Settings:

date = datetime.date.today()
formatted_date = date.strftime("%d/%m/%Y")

date_coordinates = (305, 800)
date_text_color = (11, 31, 75)
date_font_style_path = os.path.join(base_dir, "fonts", "Cinzel-VariableFont_wght.ttf")
date_font_style = ImageFont.truetype(date_font_style_path , 28)

# Signature Details Settings:

signature = Image.open(os.path.join(base_dir, "signature.png"))

resized_signature_pixels = (280, 90)  # (width , height)
resized_signature_image = signature.resize(resized_signature_pixels)
signature_coordinates = (985, 755)
transparant_signature = resized_signature_image.convert("RGBA")

# Adding Certification Template Settings:

certification_template = Image.open(os.path.join(base_dir, "certification_template.png"))

# certification_template_coordinates = (at main code)
resized_certification_template_pixels = (425 , 32)
resized_certification_template = certification_template.resize(resized_certification_template_pixels)

# Achievement Details :

achievement_text = input("1> : ")
achievement_font_style_path = os.path.join(base_dir, "fonts", "Cinzel-VariableFont_wght.ttf")
achievement_font_style = ImageFont.truetype(achievement_font_style_path , 26)
# achievement_text_coordinates = (at main code)
achievement_text_color = (184, 134, 11)

# Program Name settings :

program_font_style_path = os.path.join(base_dir, "fonts", "CormorantGaramond-VariableFont_wght.ttf")
program_font_style = ImageFont.truetype(program_font_style_path , 50)
program_text_color = (11, 31, 75)
# program_text_coordinates = (at the main code)
program_text = input("2> : ")

# Removing Invalid Characters From Program Name :
safe_program_text = "".join(c for c in program_text if c not in '<>:"/\\|?*').strip()

if not safe_program_text:
    safe_program_text = "Certificate"

# Main Code for making certificate :

with Image.open(os.path.join(base_dir, "certificate_template.png")) as i:
    
    cetificate_pixels = (1536 , 1024)
    i = i.resize(cetificate_pixels)
    draw = ImageDraw.Draw(i)
    
    
    # Adding Date Into Certificate :
    draw.text(date_coordinates , formatted_date , fill=date_text_color , font=date_font_style)
    
    # Adding Signature into the Certificate :
    i.paste(resized_signature_image , signature_coordinates , transparant_signature)
    
    # Adding Certification Template Into Certificate :
    i.paste(resized_certification_template , (i.width//2 - resized_certification_template.width//2 , i.height//2 - 150))
    
    # Adding About Achievement :
    draw.text((i.width/2 , i.height/2 + 80) , achievement_text , fill=achievement_text_color , font=achievement_font_style, anchor="mm")
    
    # Adding Course Name :
    draw.text((i.width/2 , i.height/2 + 170) ,program_text , fill=program_text_color ,anchor="mm", font=program_font_style )
    
    #Copying Certificate without Dummy Name :
    
    i_copy = i.copy()

    
    # Adding Dummy Reciptant Name Into Certificate :
    
    draw.text((i.width/2, i.height/2),dummy_reciptant_name,font=name_font,fill=(11, 31, 75),anchor="mm")
    
    # Showcasing Dummy Template :
    
    i.show()
    

# Taking User Validation :

create = False

user_validation = input("Want To Generate The Certificate File ?? ('y' for 'yes' and 'n' for 'no') \n").lower().strip()

if user_validation == "y":
    create = True
elif user_validation == "n":
    create = False
else:
    print("Please Write A valid Input...")
    sys.exit()
    

# Making Directory for Generating The Certificates :

if create:
    if not os.path.exists(os.path.join(main_dir, f"{safe_program_text}-Certificates")):
        os.mkdir(os.path.join(main_dir, f"{safe_program_text}-Certificates"))
else:
    print("No File Was Generated...")
        
# Generating Cerificate Files :

if create :
    image_extension = ".png"
    for index , student in enumerate(students , 1):
        i_copy_refrence = i_copy.copy()
        draw_copy = ImageDraw.Draw(i_copy_refrence)
    
    #Adding Student Name :
        student_name = student
        draw_copy.text((i.width/2, i.height/2), student_name ,font=name_font,fill=(11, 31, 75),anchor="mm")
        
    # Saving The Final Certificate :
        
        student_file_name = student.capitalize().strip().rstrip(". ")
        i_copy_refrence.save(os.path.join(main_dir, f"{safe_program_text}-Certificates", f"{index}. {student_file_name}{image_extension}"))
        print(f"{student.strip().capitalize()}'s Certificate Generated Successfully...")
    print("All The Certificates Are Generated Successfully...")