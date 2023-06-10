# PhotoBorder
This simple python script accepts in input pathway to a collection of photos, as well as border pixel width. From there, it will add a white border according to those specifications to all files in that folder, placing them into an inner "Processed" folder.
Output Ratio is 1:1

# Requirements:
- Python
- May require pip install pillow

# Running:
- Execute border.py (can run in powershell)
- Enter full path to target images
    - It will process ALL images and place in a new child folder
- Provide number of pixels to add to the maximum dimension:

## Example:
- Image is 300x400px
- Input pixel is 300
- Final image is 700x700px

