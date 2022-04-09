import matplotlib.pyplot as plt


def display_match(image, template, x, y):
    # Reference: https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_template.html

    fig = plt.figure(figsize=(8, 3))
    ax1 = plt.subplot(2, 1, 1)
    ax2 = plt.subplot(2, 1, 2)

    ax1.imshow(image, cmap=plt.cm.gray)
    ax1.set_axis_off()
    ax1.set_title('image')
    # highlight matched region
    hcoin, wcoin = template.shape
    rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor='r', facecolor='none')
    ax1.add_patch(rect)

    ax2.imshow(template, cmap=plt.cm.gray)
    ax2.set_axis_off()
    ax2.set_title('template')

    plt.show()

    return
