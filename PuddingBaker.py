# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

from Pudding import Pudding

# # Pudding appearance

from IPython.display import Image
Image("pudding_diagram.png", width=200)

# # Baking and eating

# ## Instructions
# - You may run each cell (each box) by clicking onto it then pressing Ctrl + Enter.
# - You may change the parameters of 

# Please specify the height h, upper radius r1, and lower radius r2, of your delicious pudding
cny_pudding = Pudding(h=1, r1=2, r2=3)

# Please specify how far away from the centre relative to the radius you would like to cut the pudding.
# If you would like to keep your pudding whole, input 0.
cny_pudding.get_volume(cut_dist_ratio=0)

# Please specify the proportion of pudding volume you would like to eat
# This will tell you where to cut across the pudding
cny_pudding.find_cut_dist_from_centre(v_prop=1/5)


