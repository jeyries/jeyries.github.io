

from pathlib import Path
from PIL import Image

def generate_inkscape(width, svg, png):
    import subprocess
    subprocess.call([
        "inkscape", 
        "-o", str(png),
        #"--export-width=%d" % int(width),
        "--export-background-opacity=0",
        "%s" % str(svg)
        ])

def generate_cairosvg(width, svg, png):
    import cairosvg
    print("generating", png, "from", svg)
    cairosvg.svg2png(url=str(svg), 
        write_to= str(png), 
        output_width= int(width), 
        output_height= int(width))



####

render_dir = Path("_render")
img_dir = Path("img")

names = ["ratp", "tf1", "mappy", "unibet", "dashlane", "calculator", "connect4"]
for name in names:
    
    img = Image.open(render_dir / f"{name}.webp")
    img = img.convert("RGBA")
    img.save(render_dir / "temp" / f"{name}.png", "PNG")

    #with open(resources / f"{name}.svg", "w") as f:
    #    f.write(rendering_svg(name))

    generate_inkscape(width= 512,
                      svg= render_dir / f"{name}.svg",
                      png= render_dir / "temp" / f"{name}-rendered.png")

    img = Image.open(render_dir / "temp" / f"{name}-rendered.png")
    img = img.convert("RGBA")
    # set compression level
    img.save(img_dir / "portfolio" / f"{name}.webp", "WEBP", quality= 90)


## profile
    
generate_inkscape(width= 256,
                      svg= render_dir / "profile.svg",
                      png= render_dir / "temp" / "profile-rendered.png")

img = Image.open(render_dir / "temp" / f"profile-rendered.png")
img = img.convert("RGBA")
# set compression level
img.save(img_dir / "profile.webp", "WEBP", quality= 90)

