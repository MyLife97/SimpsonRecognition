from __future__ import (
    division,
    print_function,
)

import selectivesearch
import skimage 

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

import matplotlib.image as mpimg



def main():

    # loading astronaut image
    # img = skimage.data.astronaut()
    # img = mpimg.imread('./Test_no_noise/' + '40.jpg')
    # img = mpimg.imread('./Test/' + '3.jpg')
    img = mpimg.imread('./Trans/' + '105.jpg')

    # perform selective search
    img_lbl, regions = selectivesearch.selective_search(
        img, scale=500, sigma=0.9, min_size=10)

    candidates = set()

    for r in regions:
        # excluding same rectangle (with different segments)
        if r['rect'] in candidates:
            continue
        # excluding regions smaller than 2000 pixels
        if r['size'] < 4000:
            continue
        # distorted rects
        x, y, w, h = r['rect']
        if w / h > 1.2 or h / w > 1.8:
            continue
        candidates.add(r['rect'])

    # draw rectangles on the original image
    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(img)
    for x, y, w, h in candidates:
        print(x, y, w, h)
        rect = mpatches.Rectangle(
            (x, y), w, h, fill=False, edgecolor='red', linewidth=1)
        ax.add_patch(rect)

    plt.show()

if __name__ == "__main__":
    main()

