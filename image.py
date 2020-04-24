from PIL import Image


def create_image(img_names: list, pdf_name: str) -> None:
    if (len(img_names) <= 0):
        raise Exception('No file was selected')

    img1 = Image.open(img_names[0])
    img_names.pop(0)

    img_list = []

    for img in img_names:
        img_list.append(Image.open(img))

    img1.save(f'{pdf_name}.pdf', "PDF", resolution=100,
              save_all=True, append_images=img_list)
