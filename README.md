<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->




<!-- PROJECT LOGO -->
<br />

<h3 align="center">Bookshelf prettify</h3>

  <p align="center">
    Small project to organize my e-book library.
    <br />


<!-- ABOUT THE PROJECT -->
## About The Project

This project is made for one simple task - rename all my e-books in one style to sort them easily, e.g. `Cline E. - Ready Player One (2021).fb2`.

This version works only for `.fb2` files.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Usage Examples

Before renaming books you may need to extract them from `.zip` archives. This can be achieved with `unzip_fb2_books` function.
It takes path to directory with compressed books as input argument.

```python
dir = '\\Books'
# clean_up flag is used to remove archives with only one `.fb2` file after extracting
# It is set True on default
unzip_fb2_books(dir, clean_up = False)
```

Use function `rename_fb2_books` to organize books:
```python
# Keep books in the same directory and remove original files
rename_fb2_books(dir, dir, delete_orig = True)
# Move books to new directory and keep original files
rename_fb2_books(dir, new_dir, delete_orig = False)
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

