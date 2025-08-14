# ColorSchemes

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/colorschemes.svg)](https://badge.fury.io/py/colorschemes)

## A package for aesthetically pleasing and colorblindness-friendly color schemes

<i>Copyright 2025 Ethan Dintzner</i>

A collection of several hundred multicolor palettes from Color Inspirations by Darius A. Monsef IV. [1] 
Additionally includes a series of functions that allow you to browse color pallets, test colorblind friendliness for inbuilt or custom pallets, produce matplotlib-compatible continuous colormaps, and convert from RGB to HEX. 

Below are examples of using this package:

```
import colorschemes as cs
ColorSchemes = cs.ColorSchemes()
```
The first function <tt>display_examples</tt> will display sixteen random examples of color schemes using <tt>matplotlib</tt>. It is a nice way to explore new color schemes.
```
ColorSchemes.display_examples()
```

<img src="/images/display_examples.png" align="center" alt="Color Scheme Examples">

To display a specific example color scheme in detail, such as this red-orange pallette, utilize the <tt>display_scheme</tt> function. It will plot the scheme using matplotlib and display the hex values for each color.
```
ColorSchemes.display_scheme('red_orange28')
```

<img src="/images/display_scheme.png" align="center" alt="Color Scheme Examples">

For a particular color scheme, you can access several different attributes including the hexcodes for the colors (<tt>colors</tt>), the harmony type (<tt>harmony</tt>), and the actual name (<tt>name</tt>). The <tt>colors</tt> attribute gives you a list of the hex values within this particular scheme, e.g.
```
ColorSchemes.red_orange19.colors
```
<tt>['#001860', '#036B2E', '#F09000', '#F06018', '#C00000']</tt>

An example of using the <tt>name</tt> attribute is as such:
```
ColorSchemes.red_orange19.name
```
<tt>'red_orange19'</tt>

And finally for displaying the harmony type for this particular color scheme using <tt>harmony</tt>:
```
ColorSchemes.red_orange19.harmony
```
<tt>'split-complementary'</tt>

This package has an inbuilt function to convert from hex to RGB called <tt>hex_to_rgb</tt>. It returns a 3-element list, e.g.
```
ColorSchemes.hex_to_rgb('#001860')
```
<tt>[0, 24, 96]</tt>

To convert RGB to hex, there is an inverse function called <tt>rgb_to_hex</tt> that is used similarly. The input is a 3-element list and the output is a string,
```
ColorSchemes.rgb_to_hex([0, 24, 96])
```
<tt>'#001860'</tt>

To simulate colorblindness for a particular hexcode color, use the <tt>colorblindness_test</tt> function. It returns a very simple matrix-transformation based simulation of Protanopia, Deuteranopia, Tritanopia, Protanomaly and Deuteranomaly disorders based on matrices from <tt>https://gist.github.com/Lokno/df7c3bfdc9ad32558bb7?permalink_comment_id=3943065</tt>. It is used for individual colors as such:
```
ColorSchemes.colorblindness_test('#001860')
```
<tt>['#0a0a4e', '#09074a', '#01403d', '#041057', '#041155']</tt>

To view a particular scheme from this package with the five simulated colorblindness disorders from above, run the <tt>scheme_colorblindness</tt> function on a scheme name within this package. for instance <tt>'violet_red13'</tt>. Powered by <tt>matplotlib</tt>, it will return a figure of 6 labeled panels if you run this:
```
ColorSchemes.scheme_colorblindness('violet_red13')
```

<img src="/images/scheme_colorblindness.png" align="center" alt="Color Scheme Examples">


If you have a custom list of hexcodes that you want to simulate colorblind-friendliness for, then use the <tt>custom_colorblindness</tt> function. It takes in a list of hexcodes as an input and returns six panels similar to above as an output.
```
ColorSchemes.custom_colorblindness(['#E73155', '#C72559', '#A7195E', '#860C62', '#670067','#00154A',
                                    '#002F59', '#6B6159', '#F9A516', '#FFBA5F'])
```

<img src="/images/custom_colorblindness.png" align="center" alt="Color Scheme Examples">


If you want to convert any of the schemes within this package into custom continuous <tt>matplotlib</tt> colormaps, use the <tt>scheme_to_cmap</tt> function. It takes in a scheme name as an input and returns a <tt>matplotlib</tt>-compatible colormap. It uses the <tt>matplotlib.pyplot</tt> function <tt>LinearSegmentedColormap</tt> to achieve this.
```
cmap = ColorSchemes.scheme_to_cmap('orange17')
```

<img src="/images/scheme_to_cmap.png" align="center" alt="Color Scheme Examples">

Here is an example of making a plot from a colormap generating using a scheme from ColorSchemes:
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

<img src="/images/custom_heatmap.png" align="center" alt="Color Scheme Examples">


You can also use this package for a custom list with the <tt>custom_scheme_to_cmap</tt> function:
```
cmap = ColorSchemes.custom_scheme_to_cmap(['#E73155', '#C72559', '#A7195E', '#860C62', '#670067','#00154A', '#002F59', '#6B6159', '#F9A516', '#FFBA5F'])
```

<img src="/images/custom_scheme_to_cmap.png" align="center" alt="Color Scheme Examples">

```
[1] Monsef, D. A. (2011). Color Inspirations: More Than 3,000 Innovative Palettes from the Colourlovers. Com Community. Simon and Schuster.
