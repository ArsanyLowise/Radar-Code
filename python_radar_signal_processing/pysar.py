# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from pysar import SARData, InSAR

# Load SAR data
sar_data = SARData('path_to_sar_data_file')

# Initialize InSAR processing
insar_processor = InSAR(sar_data)

# Generate interferogram
interferogram = insar_processor.generate_interferogram()

# Plot the interferogram
plt.imshow(interferogram, cmap='jet')
plt.colorbar(label='Phase (radians)')
plt.title('Interferogram')
plt.show()
