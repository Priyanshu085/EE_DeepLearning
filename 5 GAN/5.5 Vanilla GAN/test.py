import numpy as np
import cv2
from keras.models import load_model
from matplotlib import pyplot

def save_plot(examples, n):
    n = int(n)
    examples = (examples + 1) / 2.0
    examples = examples * 255
    file_name = f"fake_sample.png"

    cat_image = None
    for i in range(n):
      start_idx = i * n
      end_idx = (i + 1) * n

      image_list = examples[start_idx:end_idx]
      if i == 0:
        cat_image = image_list
      else:
        cat_image = np.concatenate((cat_image, image_list), axis=0)

    cat_image = cat_image.astype(np.uint8)  # Convert cat_image to uint8 data type
    cv2.imwrite(file_name, cat_image)


if __name__ == "__main__":
    model = load_model("saved_model/g_model.h5")
    
    n_samples = 100
    latent_dim = 64
    latent_points = np.random.normal(size=(n_samples, latent_dim))
    examples = model.predict(latent_points)
    save_plot(examples, np.sqrt(n_samples))