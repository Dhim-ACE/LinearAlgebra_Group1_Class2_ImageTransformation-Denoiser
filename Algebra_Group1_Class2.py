import streamlit as st
from PIL import Image, ImageFilter, ImageTransform

def denoise_image_pillow(image):
    """
    Applies Median Filter for Denoising using Pillow.

    Args:
        image: Input image (PIL format).

    Returns:
        Denoised image (PIL format).
    """
    return image.filter(ImageFilter.MedianFilter(size=3))

def translate_image(image, x_offset, y_offset):
    """
    Translates an image by a specified offset in both x and y directions.

    Args:
        image: Input image (PIL format).
        x_offset: Horizontal offset in pixels (positive for right, negative for left).
        y_offset: Vertical offset in pixels (positive for down, negative for up).

    Returns:
        Translated image (PIL format).
    """
    return image.transform(image.size, Image.AFFINE, (1, 0, x_offset, 0, 1, y_offset))

def scale_image(image, scale_factor):
    """
    Scales an image by a specified factor.

    Args:
        image: Input image (PIL format).
        scale_factor: Scaling factor (float, e.g., 0.5 for half size, 2.0 for double size).

    Returns:
        Scaled image (PIL format).
    """
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    return image.resize((new_width, new_height), Image.ANTIALIAS)

def skew_image(image, shear_x, shear_y):
    """
    Skews an image by specified shear angles in x and y directions.

    Args:
        image: Input image (PIL format).
        shear_x: Shear angle in x direction (radians).
        shear_y: Shear angle in y direction (radians).

    Returns:
        Skewed image (PIL format).
    """
    return image.transform(image.size, Image.AFFINE, (1, shear_x, 0, shear_y, 1, 0))

def rotate_image(image, angle):
    """
    Rotates an image by a specified angle in degrees.

    Args:
        image: Input image (PIL format).
        angle: Rotation angle in degrees (positive for clockwise, negative for counter-clockwise).

    Returns:
        Rotated image (PIL format).
    """
    return image.rotate(angle)

def image_processing_page():
    st.title("Image Processing")

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        # Denoising
        denoised_image = denoise_image_pillow(image)

        # Transformation Options
        st.sidebar.header("Transformations")
        x_offset = st.sidebar.number_input("X Offset (pixels)", min_value=-image.width, max_value=image.width, value=0)
        y_offset = st.sidebar.number_input("Y Offset (pixels)", min_value=-image.height, max_value=image.height, value=0)
        scale_factor = st.sidebar.number_input("Scale Factor (float)", min_value=0.1, max_value=5.0, value=1.0)
        shear_x = st.sidebar.number_input("Shear X (radians)", min_value=-0.5, max_value=0.5, value=0.0)
        shear_y = st.sidebar.number_input("Shear Y (radians)", min_value=-0.5, max_value=0.5, value=0.0)
        rotation_angle = st.sidebar.number_input("Rotation Angle (degrees)", min_value=-360, max_value=360, value=0.0)

        # Apply Transformations
        transformed_image = denoised_image
