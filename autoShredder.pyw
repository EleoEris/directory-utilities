from pathlib import Path
from json import dumps
from random import randbytes, randint
from datetime import datetime

### Best to put in a startup folder and set the date as shred_if variable
### at the bottom of this file

class AutoShredder():
    def __init__(self,
                 ### FOLDER TO SHRED
                 folderName         : str,
                 ### AUTOSHRED IF OPENED AFTER THE GIVEN DATE
                 date               : datetime,
                 ### FILES WILL BE MOVED TEMPORARILY TO A FOLDER WITH THIS NAME
                 erasure_dir_name   = "to-shred"):
        self.target         = Path(folderName)
        self.erasure_date   = date
        self.erasure_dir    = Path(erasure_dir_name)

    def run(self):
        if self.is_after_date():
            self.erasure_dir.mkdir(exist_ok = True)
            self.shred_pt1(self.target)
            self.shred_pt2()
            print("ERASED!")
            input()

    def shred_pt1(self, folder: Path):
        for file in folder.iterdir():
            self.shred_data(file)

    def shred_pt2(self):
        ### I don't wanna import any more modules
        for file in self.erasure_dir.iterdir():
            if file.is_dir():
                file.rmdir()
            else:
                file.unlink()
        new_name = str(randint(10**150, 10**200))
        Path(self.target).rename(self.erasure_dir / new_name)
        (self.erasure_dir / new_name).rmdir()
        self.erasure_dir.rmdir()
        

    def shred_data(self, file: Path):
        try:
            if file.is_dir():
                self.shred_pt1(file)
                file.rename(self.erasure_dir / str(randint(10**150, 10**200)))
            else:
                file.write_bytes(randbytes(len(file.read_bytes())))
                Path(file).rename(self.erasure_dir / str(randint(10**150, 10**200)))
        except FileExistsError:
            self.shred_data(file)
        

    def is_after_date(self):
        return datetime.now() > self.erasure_date

    ### NOT USED - made as experiment and might reuse in later projects    
    def make_json_tree(self, folder: Path):
        tree = {folder.name : []}
        for file in folder.iterdir():
            if file.is_dir():
                tree[folder.name].append([self.make_json_tree(file)])
            else:
                tree[folder.name].append(file.name)
        return tree


if __name__ == '__main__':
    shred_if = datetime(2012, 12, 21, 13, 40)
    debug = AutoShredder(r"test", shred_if)
    debug.run()

