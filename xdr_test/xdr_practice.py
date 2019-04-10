import xdrlib

def xdr_packer():
    p = xdrlib.Packer()
    p.pack_list([1, 2, 3], p.pack_int)
    print(p)

def xdr_exception():
    p = xdrlib.Packer()
    try:
        p.pack_double(8.01)
    except xdrlib.ConversionError as instance:
        print('packing the double failed:', instance.msg)

if __name__ == "__main__":
    xdr_packer()