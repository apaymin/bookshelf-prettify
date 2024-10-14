import xml.etree.ElementTree as ET
import glob
import os
import zipfile

def get_field_value(xml_field):
    ''' Get value of xml field. If field is empty (e.g. None), returns empty string'''
    if xml_field == None:
        return ""
    else:
        return xml_field.text

def unzip_fb2_books(dir, clean_up = True):
    ''' Unzip all fb2 books from archives in given folder
    Archives, that contains only one extracted file, can be removed'''

    zip_archive_list = glob.glob(f"{dir}\\*.zip")
    if not zip_archive_list:
        print('Archives with .fb2 and .epub books not found')
        return

    book_cnt = 0
    deleted_cnt = 0
    del_flag = False

    for zip_archive in zip_archive_list:
        with zipfile.ZipFile(zip_archive, 'r') as zf:
            for filename in zf.namelist():
                if (filename.split('.')[-1] == 'fb2'):
                    zf.extract(filename, dir)
                    book_cnt += 1
                    if len(zf.namelist()) == 1:
                        del_flag = True
                        deleted_cnt += 1
        if del_flag and clean_up:
            os.system(f"rm \"{zip_archive}\"")
            del_flag = False
            
    print(f"Unzipped {book_cnt} .fb2 and .epub books, {deleted_cnt} archives removed.")
    return

def rename_fb2_books(dir, new_dir, delete_orig = True):
    ''' Rename fb2 books in one format:
        Feynman R. P. - Surely You're Joking, Mr. Feynman! (1997)
    Renamed books can be moved to new directory
    Original files can be removed'''

    if not os.path.isdir(dir):
        print(f"Directory {dir} does not exist")
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)
        print(f"Created folder for storing books: {new_dir}")

    fb2_book_list = glob.glob(f"{dir}\\*.fb2") 
    if not fb2_book_list:
        print('.fb2 books not found')

    renamed_cnt = 0

    for book in fb2_book_list:
        tree = ET.parse(book)
        root = tree.getroot()
        tag = root.tag.split("}")[0]+"}"

        first_name = get_field_value(root.find(f'{tag}description/{tag}title-info/{tag}author/{tag}first-name'))
        middle_name = get_field_value(root.find(f'{tag}description/{tag}title-info/{tag}author/{tag}middle-name'))
        last_name = get_field_value(root.find(f'{tag}description/{tag}title-info/{tag}author/{tag}last-name'))
        book_title = get_field_value(root.find(f'{tag}description/{tag}title-info/{tag}book-title'))
        
        pub_year = get_field_value(root.find(f'{tag}description/{tag}publish-info/{tag}year'))
        pub_year = "" if (pub_year == "") else f" ({pub_year})"

        if (middle_name != ""):
            os.system(f"cp \"{book}\" \"{new_dir}\\{last_name} {first_name[0]}. {middle_name[0]}. - {book_title}{pub_year}.fb2\"")
        else:
            os.system(f"cp \"{book}\" \"{new_dir}\\{last_name} {first_name[0]}. - {book_title}{pub_year}.fb2\"")

        if delete_orig:
            os.system(f"rm \"{book}\"")

        renamed_cnt += 1

    print(f"Renamed {renamed_cnt} .fb2 books")



if __name__ == "__main__":      
    dir = "C:\\Users\\Anton\\Downloads\\Books\\"
    new_dir = f"{dir}Clean books"

    unzip_fb2_books(dir, clean_up = True)
    rename_fb2_books(dir, new_dir, delete_orig = True)

    #TODO check for same names after renaming


