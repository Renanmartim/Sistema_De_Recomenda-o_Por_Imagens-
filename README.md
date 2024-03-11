# Sistema_De_Recomenda-o_Por_Imagens-


<section>
  <h2>Description</h2>
    <p>This repository contains code for a recommendation system that suggests similar products based on their images.
    <p>It utilizes pre-trained VGG16 model for feature extraction and cosine similarity for recommendation.</p>
</section>

<section>
  <h2>What the code does</h2>
    <h1>This code performs the following tasks:</h1>
      <p>It imports necessary libraries like NumPy, TensorFlow (Keras), Pandas, and others.</p>
      <p>It loads the VGG16 pre-trained model for image classification.</p>
      <p>Defines a function extract_characteristics to extract features from an image using the VGG16 model.</p>
      <p>Defines a directory containing images and extracts features for all images in that directory.</p>
      <p>Defines a function recommend_product_most_similar to recommend the most similar product based on the features extracted from images.</p>
      <p>Defines a function extract_number to extract numbers from image file names.</p>
      <p>Defines a function search_similar_images_by_text to search for similar images using Google search based on a given query text.</p>
      <p>Demonstrates an example usage of the above functions to recommend the most similar product based on a query image, extract a number from the recommended image's filename, read a CSV file, set the index, access a specific value from the DataFrame, and finally search for similar images based on the retrieved text description.</p>
      <p>Overall, the code utilizes pre-trained deep learning models for feature extraction from images and combines it with text processing techniques to perform product recommendation and image searching tasks.</p>
</section>


<section>
    <h2>Requirements</h2>
    <ul>
      <li>Python 3.x</li>
      <li>Numpy</li>
      <li>OpenCV</li>
      <li>Pandas</li>
      <li>Requests</li>
      <li>Keras</li>
      <li>Scikit-learn</li>
    </ul>
</section>

<section>
  <h2>Usage</h2>
    <ol>
      <li><strong>Clone the repository:</strong>
        <pre><code>git clone https://github.com/yourusername/recommendation-system.git</code></pre>
      </li>
      <li><strong>Navigate to the repository directory:</strong>
        <pre><code>cd recommendation-system</code></pre>
      </li>
      <li><strong>Install dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
      </li>
      <li><strong>Organize your data:</strong> Place your product images in the <code>Images</code> directory.</li>
      <li><strong>Run the code:</strong> Execute the <code>recommendation_system.py</code> file. You may need to modify paths according to your data location.
          <pre><code>python recommendation_system.py</code></pre>
      </li>
      <li><strong>Explore the results:</strong> The code will recommend the most similar product based on the input image. It will also search for similar images based on text extracted from the product description.</li>
    </ol>
</section>

<section>
  <h2>Acknowledgments</h2>
    <ul>
      <li>This project utilizes the VGG16 model and the concept of cosine similarity for product recommendation.</li>
      <li>Thanks to the developers of Keras, OpenCV, Pandas, and Scikit-learn for their invaluable contributions.</li>
    </ul>
</section>

<footer>
  <p>&copy; 2024 Recommendation System Project. All Rights Reserved.</p>
</footer>

