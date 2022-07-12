<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/jnywong/monte-carlo-estimate-pi">
    <img src="estimate-pi.png" alt="Logo" width="180" height="180">
  </a>

<h3 align="center">monte-carlo-estimate-pi</h3>

  <p align="center">
    Simple python script to estimate pi using the Monte Carlo method.
    <br />
    <a href="https://github.com/jnywong/monte-carlo-estimate-pi"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/jnywong/monte-carlo-estimate-pi">View Demo</a>
    ·
    <a href="https://github.com/jnywong/monte-carlo-estimate-pi/issues">Report Bug</a>
    ·
    <a href="https://github.com/jnywong/monte-carlo-estimate-pi/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This is a small project that uses the Monte Carlo method to estimate $\pi$.

### Method

The area of a circle is 

$$
A_c = \pi r^2.
$$

The area of a square enclosing the circle is

$$
A_s = (2r)^2 = 4 r^2,
$$

where $r$ is the radius of the circle.

We estimate $\pi$ by looking at the ratio between these two areas:

$$
\frac{A_c}{A_s} = \frac{\pi r^2}{4 r^2} \Rightarrow \pi \approx4\frac{A_c}{A_s}.
$$

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This code requires Python 3.

<!-- USAGE EXAMPLES -->
## Usage

Run the code using

```shell
python3 estimate-pi.py
```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [ ] Create an interactive dashboard so that the user can choose the number of points 
- [ ] Host the interactive app on a website

See the [open issues](https://github.com/jnywong/monte-carlo-estimate-pi/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See [LICENSE.md](LICENSE.md) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jenny Wong - [@_jennywong_](https://twitter.com/_jennywong_) - j.wong.1@bham.ac.uk

Project Link -  [https://github.com/jnywong/monte-carlo-estimate-pi](https://github.com/jnywong/monte-carlo-estimate-pi)

<p align="right">(<a href="#top">back to top</a>)</p>



<!--ACKNOWLEDGMENTS -->
## Acknowledgments

* [Geeksforgeeks](https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jnywong/monte-carlo-estimate-pi.svg?style=for-the-badge
[contributors-url]: https://github.com/jnywong/monte-carlo-estimate-pi/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jnywong/monte-carlo-estimate-pi.svg?style=for-the-badge
[forks-url]: https://github.com/jnywong/monte-carlo-estimate-pi/network/members
[stars-shield]: https://img.shields.io/github/stars/jnywong/monte-carlo-estimate-pi.svg?style=for-the-badge
[stars-url]: https://github.com/jnywong/monte-carlo-estimate-pi/stargazers
[issues-shield]: https://img.shields.io/github/issues/jnywong/monte-carlo-estimate-pi.svg?style=for-the-badge
[issues-url]: https://github.com/jnywong/monte-carlo-estimate-pi/issues
[license-shield]: https://img.shields.io/github/license/jnywong/monte-carlo-estimate-pi.svg?style=for-the-badge
[license-url]: https://github.com/jnywong/monte-carlo-estimate-pi/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/thisisjennywong
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 