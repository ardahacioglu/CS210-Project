from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_folder):
    
    # Convert the PDF into images
    try:
        # `convert_from_path` returns a list of image objects for each page in the PDF
        images = convert_from_path(pdf_path)
    except Exception as e:
        # If an error occurs during the conversion, print an error message and stop
        print(f"An error occurred while converting the PDF: {e}")
        return

    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save each page as a separate image
    for i, image in enumerate(images):
        # Create the file path for each image with a sequential name (page_1.png, page_2.png, etc.)
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        # Save the image in PNG format
        image.save(image_path, 'PNG')
        # Print a message indicating the image has been saved successfully
        print(f"Page {i + 1} image saved: {image_path}")

# Example usage - converts pdf and saves the images in the "output_images" folder
pdf_to_images("Page 195.pdf", "output_images")
