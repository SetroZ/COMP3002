# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# Author: [Your Name]
# Last Modified: 2024-09-09


"""
Input: Colored Image
1. gray scale
2.
Output:
a)txt file of  x1 , y1 , x2 , y2 , x3 , y3 , x4 , y4
b)Image of numbers!
    x
"""
import os
import cv2
import matplotlib.pyplot as plt


def save_output(output_path, content, output_type="txt"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if output_type == "txt":
        with open(output_path, "w") as f:
            f.write(content)
        print(f"Text file saved at: {output_path}")
    elif output_type == "image":
        # Assuming 'content' is a valid image object, e.g., from OpenCV
        content.save(output_path)
        print(f"Image saved at: {output_path}")
    else:
        print("Unsupported output type. Use 'txt' or 'image'.")


def run_task1(image_path, config):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # ret2, bina_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # show(bina_img)
    edges = cv2.Canny(img, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    for contour in contours:
        # Compute the bounding box of the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Filter based on the aspect ratio (barcodes are generally wide)
        aspect_ratio = w / float(h)

        # Check if the contour has an aspect ratio similar to a barcode (e.g., width is larger than height)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    show(img)

    # TODO: Implement task 1 here
    # output_path = f"output/task1/result.txt"
    # save_output(output_path, "Task 1 output", output_type="txt")


def show(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the result using matplotlib
    plt.figure(figsize=(10, 6))
    plt.imshow(image_rgb)
    plt.title("Barcode Detection")
    plt.axis("off")  # Hide axes for better visualization
    plt.show()


run_task1("../validation/test/task1/img3.jpg", "")
# def main():
#     directory = os.fsencode("../validation/test/task1")
#     for file in os.listdir(directory):
#         filename = os.fsdecode(file)
#         run_task1(filename, "")
