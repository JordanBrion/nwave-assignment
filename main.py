from src.scene import Scene
from src.entities import Disk
from src.renderer import Renderer
from src.viewport import Viewport
from src.serialize import JsonSerializer, XmlSerializer
from src.filewriter import FileWriter

def main():
    scene = Scene(background_color=[102, 204, 255])
    radius=250
    scene.add_entity(Disk(radius=radius, position=[0, 216], color=[255, 0, 0]))
    scene.add_entity(Disk(radius=radius, position=[-250, -216], color=[0, 255, 0]))
    scene.add_entity(Disk(radius=radius, position=[250, -216], color=[0, 0, 255]))
    
    jpg_writer = FileWriter("/Users/jordanbrion/Downloads/aaa1.jpg")
    renderer = Renderer(writer=jpg_writer)
    viewport = Viewport(width=1100, height=1000, renderer=renderer)
    viewport.render(scene)

    png_writer = FileWriter("/Users/jordanbrion/Downloads/aaa2.png")
    renderer.writer = png_writer
    viewport.render(scene)

    #JsonSerializer().serialize_scene(scene)
    #XmlSerializer().serialize_scene(scene)

# stop execution

if __name__ == "__main__":
    main()