#! python 3
# copies an entire folder and its content into
# a zipfile whose filename increaments
import zipfile ,os
os.chdir("d:\\")
def backupToZip(folder):

    # backup  the entire contents of "folder" into a zipfile .
    f=os.path.abspath(folder)  # make sure folder is absolute
    # figure out the filename this code should use based on
    # whatr flies already exist.
    n=1
    while True:
        zfn=os.path.basename(folder)+"_"+str(n)+".zip"
        if not os.path.exists(zfn):
            break
        n=n+1
    # todo: create the zip
    print("creating %s..." %(zfn))
    bz=zipfile.ZipFile(zfn,"w")




    # todo : walk the entire tree and compress the files in each folder.
    for fn,sfs,fns in os.walk(f):
        print("adding  files in %s..."%(fn))
        #add current folder to the zip file.
        bz.write(fn)
        #add all the files in this folder to the zip file .
        for fm in fns:
            newbase = os.path.basename(f)+ "_"
            if fm.startswith(newbase) and fm.endswith(".zip"):
                continue #dont backup the backup zip files
            bz.write(os.path.join(fn,fm))
    bz.close()
    print("Done")
backupToZip("d:\\Mathematica")
