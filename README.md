# ColorSchemes

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/colorschemes.svg)](https://badge.fury.io/py/colorschemes)

A package for aesthetically pleasing and colorblindness-friendly color schemes

Copyright 2025 Ethan Dintzner

A collection of several hundred multicolor palettes from Color Inspirations by Darius A. Monsef IV. [1] 
Additionally includes a series of functions that allow you to browse color pallets, test colorblind friendliness for inbuilt or custom pallets, produce matplotlib-compatible continuous colormaps, and convert from RGB to HEX. 

Below is an example of using this package:

```
import colorschemes as cs
ColorSchemes = cs.ColorSchemes()

# to display sixteen random examples of color schemes using matplotlib
ColorSchemes.display_examples()
```
<div style="text-align: center;">
  <img src="/images/display_examples.png" style="max-width:25%; height:auto;" alt="Color Scheme Examples">
</div>
```
# to display a specific example color scheme, such as this nice rainbow pallette
# shows the scheme using matplotlib and the hex values for each color
ColorSchemes.display_scheme('red_orange28')
```
<img src="/images/display_scheme.png" align="center" alt="Color Scheme Examples",style="max-width:50%; height:auto;">
```
# for a particular color scheme, you can access different attributes
# this gives you a list of the hex values within this particular scheme
ColorSchemes.red_orange19.colors
```
<tt>['#001860', '#036B2E', '#F09000', '#F06018', '#C00000']</tt>
```
# this prints a string for the name of the color scheme
ColorSchemes.red_orange19.name
```
<tt>'red_orange19'</tt>
```
# this prints a string indicating the type of harmony for the scheme, e.g. complementary, monochromatic, triadic, etc.
ColorSchemes.red_orange19.harmony
```
<tt>'split-complementary'</tt>
```
# to convert hex to RGB, one can use the inbuilt function hex_to_rgb. returns a 3-element list
ColorSchemes.hex_to_rgb('#001860')
```
<tt>[0, 24, 96]</tt>
```
# to convert RGB to hex, there is an inverse function called rgb_to_hex
ColorSchemes.rgb_to_hex([0, 24, 96])
```
<tt>'#001860'</tt>
```
# to simulate colorblindness for a particular hexcode color, use the colorblindness_test function
# it returns a very simple matrix-transformation based simulation of Protanopia, Deuteranopia, Tritanopia,
# Protanomaly and Deuteranomaly disorders.
# based on matrices from https://gist.github.com/Lokno/df7c3bfdc9ad32558bb7?permalink_comment_id=3943065
ColorSchemes.colorblindness_test('#001860')
```
<tt>['#0a0a4e', '#09074a', '#01403d', '#041057', '#041155']</tt>
```
# to view a particular scheme from this package with the five simulated colorblindness disorders from above,
# run the scheme_colorblindness function on a scheme name within this package. for instance 'violet_red13'.
# powered by matplotlib, it will return a figure of 6 labeled panels
ColorSchemes.scheme_colorblindness('violet_red13')
```
<img src="/images/scheme_colorblindness.png" align="center" alt="Color Scheme Examples",style="max-width:50%; height:auto;">
```
# if you have a custom list of hexcodes that you want to simulate colorblind-friendliness for, then use the
# custom_colorblindness function. takes in a list of hexcoes as an input and returns six panels similar to above
# as an output.
ColorSchemes.custom_colorblindness(['#E73155', '#C72559', '#A7195E', '#860C62', '#670067','#00154A',
                                    '#002F59', '#6B6159', '#F9A516', '#FFBA5F'])
```
<img src="/images/custom_colorblindness.png" align="center" alt="Color Scheme Examples",style="max-width:50%; height:auto;">
```
# if you want to convert any of the schemes within this package into custom continuous matplotlib colormaps,
# use the scheme_to_cmap function. it takes in a scheme name as an input and returns a matplotlib colormap.
# it uses the matplotlib pyplot function LinearSegmentedColormap
cmap = ColorSchemes.scheme_to_cmap('orange17')
```
<img src="/images/scheme_to_cmap.png" align="center" alt="Color Scheme Examples",style="max-width:50%; height:auto;">
```
# making a multivariable function to plot our new colormap
y, x = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
z = (1 - x / 2. + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
z = z[:-1, :-1]
z_min, z_max = -np.abs(z).max(), np.abs(z).max()

# making a heatmap using the colormap
fig, ax = plt.subplots()
c = ax.pcolormesh(x, y, z, cmap=cmap)
ax.set_title('custom heatmap')
# set the limits of the plot to the limits of the data
ax.axis([x.min(), x.max(), y.min(), y.max()])
fig.colorbar(c, ax=ax)
plt.show()
```
<img src="/images/custom_heatmap.png" align="center" alt="Color Scheme Examples",style="max-width:50%; height:auto;">
```
# you can also use this function for a custom list with the custom_scheme_to_cmap
cmap = ColorSchemes.custom_scheme_to_cmap(['#E73155', '#C72559', '#A7195E', '#860C62', '#670067','#00154A', '#002F59', '#6B6159', '#F9A516', '#FFBA5F'])
```
<img src="/images/custom_scheme_to_cmap.png" align="center" alt="Color Scheme Examples",style="max-width:50%; height:auto;">
```
[1] Monsef, D. A. (2011). Color Inspirations: More Than 3,000 Innovative Palettes from the Colourlovers. Com Community. Simon and Schuster.
