# ``pltflow``

## What is ``pltflow``? 

* ``pltflow`` is a wrapper for matplotlib/seaborn to create beautiful charts
* It makes use of predifined styles to completely automate the chart creation process
* It also uses the concept of pipelines to create charts as following a recipe

``pltflow`` is not intended for quick and beautiful plots.
You dont need to know anything about styling to make a pretty chart. But of course you can modify any parameter using matplotlib/seaborn arguments.
<br/>


## ✅&nbsp; Installation

``pltflow`` can be installed using pip.

```bash
pip install pltflow
```
<br/>
 
## 📌&nbsp; Requirements
* python 3.6 or above
* matplotlib 2.2 or above
* seaborn 0.9.0 or above
* pandas 1.0.0 or above

<br/>  

## 🔨 Usage&nbsp;

*``pltflow`` works with pandas dataframes as data source
* It uses pipelines to convey the 'recipe' of the chart

 ```bash
 import pltflow.charts as flow

(
    flow                                                            # from the pltflow package
    .plot(df, primary="YrSold",secondary ="ppsqm", style = "vox")   # plot the df, define variables and style
    .set_ylabel("PRICE PER M2")                                     # set the y label text
    .set_xlabel("YEAR SOLD")                                        # set the x label text
    .set_title("BOSTON PRICE PER SQUARE METER")                     # set the title text
    .set_subtitle("YEARS 2006 TO 2010 | FUNDA.COM")                 # set the subtitle text
    .color_by("Neighborhood")                       # color the chart by the neighborhood (different categories)
    .focus_on("CollgCr")                            # focus on a specific category (other will be grayed out)
    .set_figsize(8,4)                               # set the figure size
    .set_yticks(np.arange(1000, 1800, 200))         # set the spacing of the y axis labels
    .set_xticks(np.arange(2006, 2011))              # set the spacing of the x axis labels
    .show()       
                                      # SHOW!!! the graph is ready!
)

```
<br/>

Currently there are 4 predifined styles: base, vox, mkbhd, and innocent

![styles](https://github.com/ismaelcv/pltflow/blob/main/images/styles_sample.png?raw=true)


  

But more are coming soon!
<br/> 

## 🐜 &nbsp; Found a bug? Missing a specific feature?

Feel free to **file a new issue** 📫&nbsp with a respective title and description issue on the ``pltflow`` repository:  [ismaelcv](https://github.com/ismaelcv/pltflow).

<br/>

## 📘&nbsp; License 
``pltflow`` is released under the GNU Lesser General Public License (LGPL) license. All accompanying documentation and manual are released under the [Creative Commons BY-SA 4.0 license](https://creativecommons.org/licenses/).
