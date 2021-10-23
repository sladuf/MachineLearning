from os import read, truncate
import struct

def to_csv(name, maxdata):
    #data file open
    lbl_f = open("./mnist/data/"+name+"-labels", "rb")
    img_f = open("./mnist/data/"+name+"-images", "rb")
    csv_f = open("./mnist/data/"+name+".csv", "w", encoding="utf-8")

    # read 8byte -> mag = magic number(4byte) / lbl_count = number of items(4byte)
    mag, lbl_count = struct.unpack(">II", lbl_f.read(8))
    # read 8byte -> mag = magic number(4byte) / img_count = number of items(4byte)
    mag, img_count = struct.unpack(">II", img_f.read(8))
    # image file의 다음 byte : rows(4byte) , columns(4byte)
    rows, cols = struct.unpack(">II", img_f.read(8))
    pixel = rows * cols
    

    res = []
    for idx in range(lbl_count):
        if idx > maxdata : break
        # label file의 다음 byte : data(1byte)
        label = struct.unpack("B", lbl_f.read(1))[0]
        # image file의 다음 byte : pixel(1byte) * size
        bdata = img_f.read(pixel)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label)+",")
        csv_f.write(",".join(sdata)+"\r\n")

        '''
        # sample data
        if idx < 1:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            iname = "./mnist/data/{0}-{1}-{2}.pgm".format(name,idx,label)
            with open(iname, "w", encoding="utf-8") as f :
                f.write(s)
        '''
            
    csv_f.close()
    lbl_f.close()
    img_f.close()

to_csv("train", 60000)
to_csv("test", 1000)