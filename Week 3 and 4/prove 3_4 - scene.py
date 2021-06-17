'''
Prove 3 - scene.py
Abi Priebe
5/8/21
'''
'''
During this lesson, you will write code that draws the sky, the ground, and clouds. 
During the next lesson, you will write code that completes the scene. The scene that 
your program draws may be very different from the example scene above. However, your 
scene must be outdoor, the sky must have clouds, and the scene must include repetitive 
elements such as blades of grass, trees, leaves on a tree, birds, flowers, insects, 
fish, pickets in a fence, dashed lines on a road, buildings, bales of hay, snowmen, 
snowflakes, or icicles. Be creative.

Begin your program by copying and pasting the following code into a new file named 
scene.py. This beginning code imports the tkinter library and creates a window and a 
canvas that your program can draw to.
'''
import tkinter as tk

def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    """
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    
    # Call your functions here
    # draw sky
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    draw_sky(canvas, scene_width, scene_height)

    # draw clouds
    cloud1_center_x = scene_left + 100
    cloud1_center_y = scene_bottom - 400
    draw_cloud(canvas, cloud1_center_x, cloud1_center_y)

    cloud2_center_x = scene_left + 200
    cloud2_center_y = scene_bottom - 400
    draw_cloud(canvas, cloud2_center_x, cloud2_center_y)

    cloud3_center_x = scene_left + 150
    cloud3_center_y = scene_bottom - 425
    draw_cloud(canvas, cloud3_center_x, cloud3_center_y)

    cloud4_center_x = scene_left + 130
    cloud4_center_y = scene_bottom - 370
    draw_cloud(canvas, cloud4_center_x, cloud4_center_y)

    cloud5_center_x = scene_left + 170
    cloud5_center_y = scene_bottom - 370
    draw_cloud(canvas, cloud5_center_x, cloud5_center_y)

    cloud6_center_x = scene_left + 150
    cloud6_center_y = scene_bottom - 400
    draw_cloud(canvas, cloud6_center_x, cloud6_center_y)

    cloud7_center_x = scene_left + 275
    cloud7_center_y = scene_bottom - 375
    draw_cloud(canvas, cloud7_center_x, cloud7_center_y)

    cloud8_center_x = scene_left + 325
    cloud8_center_y = scene_bottom - 400
    draw_cloud(canvas, cloud8_center_x, cloud8_center_y)

    cloud9_center_x = scene_left + 325
    cloud9_center_y = scene_bottom - 360
    draw_cloud(canvas, cloud9_center_x, cloud9_center_y)

    cloud10_center_x = scene_left + 25
    cloud10_center_y = scene_bottom - 350
    draw_cloud(canvas, cloud10_center_x, cloud10_center_y)

    cloud11_center_x = scene_left + 75
    cloud11_center_y = scene_bottom - 325
    draw_cloud(canvas, cloud11_center_x, cloud11_center_y)

    # draw hills
    hill_x0 = -scene_width / 4
    hill_x1 = 3*scene_width / 4
    hill_y0 = scene_height / 2
    hill_y1 = 3*scene_height / 2
    draw_hill(canvas, hill_x0, hill_x1, hill_y0, hill_y1)

    hill_x0 = scene_width / 2
    hill_x1 = 5*scene_width / 4
    hill_y0 = 2*scene_height / 3
    hill_y1 = 3*scene_height / 2
    draw_hill(canvas, hill_x0, hill_x1, hill_y0, hill_y1)

    # draw trees
    tree_center = scene_left + 600
    tree_top = scene_top + 100
    tree_height = 275
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 700
    tree_top = scene_top + 100
    tree_height = 300
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center = scene_left + 200
    tree_top = scene_top + 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    # draw house
    house_center_x = scene_left + 275
    house_center_y = scene_top + 250
    house_height = 50
    draw_house(canvas, house_center_x, house_center_y, house_height)


# Define functions here
def draw_sky(canvas, width, height):
    x0 = 0
    x1 = width 
    y0 = height
    y1 = 0

    # Draw the sky. 
    canvas.create_rectangle(x0, y0, x1, y1,
        fill="skyblue2")

def draw_cloud(canvas, center_x, center_y):
    x0 = center_x - 40
    x1 = center_x + 40
    y0 = center_y - 25
    y1 = center_y + 25

    # Draw the cloud.
    canvas.create_oval(x0, y0, x1, y1, 
        fill="aliceBlue", outline="aliceBlue")

def draw_hill(canvas, x0, x1, y0, y1):
    # Draw the hill
    canvas.create_oval(x0, y0, x1, y1, 
        fill="green4")

def draw_pine_tree(canvas, peak_x, peak_y, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

def draw_house(canvas, center_x, center_y, height):
    # base
    x0 = center_x - 50
    x1 = center_x + 50
    y0 = center_y - 50
    y1 = center_y + 50

    canvas.create_rectangle(x0, y0, x1, y1,
            outline="gray20", fill="PaleVioletRed3")

    # roof
    x0 = center_x - 60
    y0 = center_y - 40
    x1 = center_x + 60
    y1 = center_y - 40
    x2 = center_x
    y2 = center_y - 100

    canvas.create_polygon(x0, y0, x1, y1, x2, y2,
            outline="gray20", fill="IndianRed4")

    # windows
    x0 = center_x - 40
    x1 = center_x - 10
    y0 = center_y - 30
    y1 = center_y

    canvas.create_rectangle(x0, y0, x1, y1,
            outline="black", fill="azure")

    x0 = center_x + 40
    x1 = center_x + 10
    y0 = center_y - 30
    y1 = center_y

    canvas.create_rectangle(x0, y0, x1, y1,
            outline="black", fill="azure")

    # door
    x0 = center_x - 15
    x1 = center_x + 15
    y0 = center_y + 50
    y1 = center_y + 5

    canvas.create_rectangle(x0, y0, x1, y1,
            outline="black", fill="gray20")

# Call the main function so that
# this program will start executing.
main()