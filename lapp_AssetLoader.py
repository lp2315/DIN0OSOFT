import pyglet as pyg
########################################
# # # AssetLoader for App # # # file handling and sprite batching
########################################

usr_font = 'TACKERLEN'

batch_1 = pyg.graphics.Batch()

########################################


AssetLoader = pyg.resource.Loader(
        path=['Assets'])


assidx = AssetLoader.reindex()

########################################


def font_addit(font):
    AssetLoader.add_font(font + '.otf')

    pyg.font.have_font(font)
    pyg.font.load(font)


###


def spr_12_addit(file):
    png = AssetLoader.image(file)

    pnx = png.width
    pny = png.height

    pdx = pnx // 12
    pdy = pny // 12

    pngrid = pyg.image.ImageGrid(
        png,
        rows=pdy,
        columns=pdx)

    pngrid.get_texture()

    txgrid = pyg.image.TextureGrid(pngrid)

    txseq = txgrid[(0, 0):]

    ani = pyg.image.Animation.from_image_sequence(
        sequence=txseq,
        duration=0.25,
        loop=True)

    pyg.sprite.Sprite(ani, x=300, y=300, batch=batch_1)


########################################
