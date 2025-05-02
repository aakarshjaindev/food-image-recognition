def load_image(image_path):
    import cv2
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at the path: {image_path}")
    return image

def save_image(image, save_path):
    import cv2
    success = cv2.imwrite(save_path, image)
    if not success:
        raise ValueError(f"Failed to save image at the path: {save_path}")