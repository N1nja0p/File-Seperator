#FILE SEPERATOR CREATED BY ABHIMANYU SHARMA A.K.A N1nja0p
import os 
import shutil
dict_extensions = {
    'Audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
    'Video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg','.vid'),
    'Document_extensions' : ('.doc', '.pdf', '.txt','.docx','pptx','.db','.xlsx'),
    'Executable_extensions':('.exe','.msi'),
    'Image_extensions':('.png','.jpg','.jpeg','.jfif','.bnp','.icon','.ico','.ods','.webp'),
    'Python_extensions':('.py','.pyw'),
    'Java_extensions':('.jar','.java','.jdk','.kt'),
    'Android_extensions':('.apk',),
    'Gif_extensions':('.gif',),
    'Zip_extensions':('.7z','.rar','.tag.gz','.zip'),
    'Disc_extensions':('.iso','.img'),
}
print("Welcome To File Seperator")
name=input("Enter Your Name : ")
folderpath=input(f"Hey {name.title()}, Please Enter Your Folder Path : ")
def file_finder(folder_path,file_extensions):
    return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]
for extension_type,extension_tuple in dict_extensions.items():
    folder_name=extension_type.split("_")[0]+"Files"
    folder_path=os.path.join(folderpath,folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath,extension_tuple):
        item_path=os.path.join(folderpath,item)
        item_new_name=os.path.join(folder_path,item)
        shutil.move(item_path,item_new_name)