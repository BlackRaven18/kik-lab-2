class FileUtils:

    forbidden_chars = [" ","\n","\r","\t",",",".",";","-","!","?",":","\\","/","(",")","[","]","{","}","'",'"',"`","1","2","3","4","5","6","7","8","9","0"]
    default_files_directory = "files/"
    

    def remove_forbidden_chars_from_text(text):
        text = text.upper()
        for char in FileUtils.forbidden_chars:
            text = text.replace(char, "")

        return text
    
    def read_file(filename, remove_forbidden_chars = False) -> str:
        file = ""

        with open(FileUtils.default_files_directory + filename, "r", encoding="utf-8-sig") as f:
            file = f.read()

        if remove_forbidden_chars:
            file = FileUtils.remove_forbidden_chars_from_text(file)

        return file
    
    def write_file(filename, text):
        with open(FileUtils.default_files_directory + filename, "w") as f:
            f.write(text)