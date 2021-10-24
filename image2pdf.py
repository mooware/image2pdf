def create_image_pdf(outpath, imagepaths):
    from PIL import Image
    images = []
    for fn in imagepaths:
        print("reading image", fn)
        images.append(Image.open(fn))
    print("writing pdf", outpath)
    images[0].save(outpath, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
    print("done")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("usage: image2pdf <output.pdf> <inputimage.ext>...")
        sys.exit(1)
    outfile = sys.argv[1]
    infiles = sys.argv[2:]
    create_image_pdf(outfile, infiles)
