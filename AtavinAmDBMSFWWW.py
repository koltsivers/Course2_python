import os
data_folder = "data"
def createGalleryHtml():
    gallery_elements = []
    for f in os.listdir(data_folder):
        if f.endswith(".txt"):
            gallery_elements.append(f[:-4])
    with open(os.path.join(os.path.abspath(data_folder), "launch.html"), "w") as launch_file:
        launch_file.write("<html>\n<head>\n<title style='font-family: COMIC SANS MS;'>Известные города России</title>\n</head>\n<body>\n<style>body{background-color: LightYellow;}\n</style>\n"
                       "<div style='font-family: COMIC SANS MS; font-size: 40; text-align: center; top: 5%;'>ГАЛЕРЕЯ</div>\n"
                       "<div style='font-family: COMIC SANS MS; font-size: 35; text-align: center; top: 7%;'>Известные города России</div>\n"
                       "<div style='font-family: COMIC SANS MS; font-size: 35; text-align: center; top: 9%;'>Можете начать просмотр с любого города</div>\n")
        for i, element in enumerate(gallery_elements):
            launch_file.write(f'<a href="{element}.html" style="font-family: COMIC SANS MS; display: block; text-align: center; font-size: 25; top: 14+{i}%;">{element}</a><br>\n')
        launch_file.write("<div style='font-family: COMIC SANS MS; font-size: 30; text-align: center; top: 95%;'>Авторские права: Атавин Даниил, Москва, 2024</div>\n</body>\n</html>")
    for element in gallery_elements:
        with open(os.path.join(os.path.abspath(data_folder), f"{element}.html"), "w") as element_file:
            element_file.write(f"<html>\n<head>\n<title>{element}</title>\n</head>\n<body>\n<div style='font-family: COMIC SANS MS; font-size: 30; text-align: center; top: 1%;'>{element}</div>\n")
            element_file.write("<style>body{background-color: LightYellow;}\n</style>\n")
            image_path = os.path.join(os.path.abspath(data_folder), f"{element}.png")
            text_path = os.path.join(os.path.abspath(data_folder), f"{element}.txt")
            if os.path.exists(image_path):
                element_file.write(f"<img src='{image_path}' style='max-width: 40%; display: block; margin-left: auto; margin-right: auto; top 40%'><br>\n")
            else:
                element_file.write("<p>Изображение недоступно</p><br>\n")
            if os.path.exists(text_path):
                with open(text_path, "r", encoding="utf-8") as textfile:
                    text_content = textfile.read()
                    element_file.write(f'<p style="font-family: COMIC SANS MS; font-size: 18; text-align: center; position: absolute; top: 60%">{text_content}</p><br>\n')
            else:
                element_file.write("<p>Текст недоступен</p><br>\n")
            element_index = gallery_elements.index(element)
            prev_element = gallery_elements[(element_index - 1) % len(gallery_elements)]
            next_element = gallery_elements[(element_index + 1) % len(gallery_elements)]
            element_file.write(f'<a href="launch.html" style="font-family: COMIC SANS MS; font-size: 20; position: absolute; top: 90%; left: 645px;">Перейти к началу</a><br>\n')
            element_file.write(f'<a href="{prev_element}.html" style="font-family: COMIC SANS MS; font-size: 20; position: absolute; top: 90%; left: 20px">Предыдущий: {prev_element}</a><br>\n')
            element_file.write(f'<a href="{next_element}.html" style="font-family: COMIC SANS MS; font-size: 20; position: absolute; top: 90%; right: 20px">Следующий: {next_element}</a><br>\n')
            element_file.write("</body>\n</html>")