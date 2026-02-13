# To copy the contents of a file and other persmissions

# copyfile() - copies the contents of a file
# copy() - copyfile() + permission mode + the destination 
# copy2() - copy() + copies meta data(the fil's creation and modification times)

# They all take two argumnts: the source filea nd the destinatin file

# we need to import the library that does this
import shutil 
shutil.copyfile("C:/Users/My Device/Desktop/pythonWorkspace/file_management/sourceFile.txt", "copy.txt")

