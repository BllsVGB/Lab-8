import cv2

def show_variant_image():
    variant_image = cv2.imread('variant-1.jpg', cv2.IMREAD_GRAYSCALE)

    if variant_image is None:
        print("Ошибка загрузки изображения variant-1.jpg.")
        return

    variant_image_resized = cv2.resize(variant_image, (720, 540), interpolation=cv2.INTER_LINEAR)

    cv2.imshow('Variant Image', variant_image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    show_variant_image()
