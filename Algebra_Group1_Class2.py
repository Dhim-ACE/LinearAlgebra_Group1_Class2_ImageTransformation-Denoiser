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

def denoising_page():
  st.title("Image Denoising with Pillow")

  uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

  if uploaded_file is not None:
    image = Image.open(uploaded_file)

    denoised_image = denoise_image_pillow(image)

    st.image([image, denoised_image], caption=['Original Image', 'Denoised Image'], use_container_width=True)

def transformation_page():
  st.title("Image Transformation (Translate, Scale, Skew)")

  uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

  if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Input fields for transformation parameters
    x_offset = st.number_input("X Offset (pixels)", min_value=-image.width, max_value=image.width, value=0)
    y_offset = st.number_input("Y Offset (pixels)", min_value=-image.height, max_value=image.height, value=0)
    scale_factor = st.number_input("Scale Factor (float)", min_value=0.1, max_value=5.0, value=1.0)
    shear_x = st.number_input("Shear X (radians)", min_value=-0.5, max_value=0.5, value=0.0)
    shear_y = st.number_input("Shear Y (radians)", min_value=-0.5, max_value=0.5, value=0.0)

    # Apply transformations based on user input
    transformed_image = image.copy()  # Avoid modifying the original image
    transformed_image = translate_image(transformed_image, x_offset, y_offset)
    transformed_image = scale_image(transformed_image, scale_factor)
    transformed_image = skew_image(transformed_image, shear_x, shear_y)

    # Display original and transformed images
    st.image([image, transformed_image], caption=['Original Image', 'Transformed Image'], use_container_width=True)

def main_page():
  st.title("Linear Algebra Group 1 Class 2 [2023]")

  col1, col2 = st.columns(2)

  with col1:
    try:
      # Coba untuk menggunakan jalur relatif untuk gambar
      image_path = "PresidentUniversityLogo.png"  # Gambar ini harus ada di dalam folder 'images'
      st.image(image_path, caption="President University Logo", use_container_width=True)
    except Exception as e:
      st.error(f"Error loading image: {e}")

  with col2:
    st.write("*Group Members:*")
    st.write("- Achmad Ridho Raziqin Ahsit")
    st.write("- Dhimas Ariyanto")
    st.write("- Muhammad Isfan Nabil Hanif")
    st.write("- Pambudi Setyo Wicaksono")

def about_page():
  st.title("About Image Transformation: Denoiser")

  col1, col2 = st.columns(2)

  with col1:
    # Load the static DenoiserEffect.png from a file path
    try:
      # Gambar statis DenoiserEffect.png
      image_path = "DenoiserEffect.png"  # Pastikan gambar ini berada dalam folder yang sama dengan file kode
      st.image(image_path, caption="Denoiser Effect", use_container_width=True)
    except Exception as e:
      st.error(f"Error loading image: {e}")

  with col2:
    st.write("*Image Denoising*")
    st.write("Image denoising is a technique used to reduce noise in images. Noise can be caused by various factors, such as sensor noise, transmission errors, or poor lighting conditions.")
    st.write("The *Median Filter* technique is one of the basic methods for image denoising. It works by applying a filter that preserves edges while reducing noise, making it suitable for basic denoising operations.")

if __name__ == "__main__":
  page = st.sidebar.selectbox("Select a Page", ["1. Linear Algebra Project", "2. Image Transformation: Denoiser", "3. About Image Transformation", "4. Image Transformation (Translate, Scale, Skew)"])

  if page == "1. Linear Algebra Project":
    main_page()
  elif page == "2. Image Transformation: Denoiser":
    denoising_page()
  elif page == "3. About Image Transformation":
    about_page()
  elif page == "4. Image Transformation (Translate, Scale, Skew)":
    transformation_page()
