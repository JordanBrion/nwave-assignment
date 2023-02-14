from src.scene import Scene
from src.entities import Disk

def main():
    scene = Scene(background_color=[102, 204, 255])
    radius=250
    scene.add_entity(Disk(radius=radius, position=[0, 216], color=[255, 0, 0]))
    scene.add_entity(Disk(radius=radius, position=[-250, -216], color=[0, 255, 0]))
    scene.add_entity(Disk(radius=radius, position=[250, -216], color=[0, 0, 255]))
 
# stop execution

if __name__ == "__main__":
    main()