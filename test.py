from PIL import Image

import matplotlib.pyplot as plt
enemy_image=Image.open("assets/projectile.png")
enemy_image=enemy_image.resize((200,200))
plt.imshow(enemy_image)
plt.show()