<a id="readme-top"></a>
<!-- PROJECT SHIELDS -->
[![Commits][commits-shield]][commits-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/AnthonyClemens/NEAT-2048">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/2048_logo.svg/300px-2048_logo.svg.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">NEAT 2048</h3>

  <p align="center">
    An attempt to use the NeuroEvolution of Augmenting Topologies to play 2048. I made this as a challenge to my Python ability, algorithmic skills, and to learn NEAT.
    <br />
    <a href="https://github.com/AnthonyClemens/NEAT-2048"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AnthonyClemens/NEAT-2048">View Code</a>
    ·
    <a href="https://github.com/AnthonyClemens/NEAT-2048/issues/new?labels=bug">Report Bug</a>
    ·
    <a href="https://github.com/AnthonyClemens/NEAT-2048/issues/new?labels=enhancement">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I developed this project as a self-imposed challenge to hone my Python programming skills, reverse engineering abilities, and problem-solving capabilities. The inspiration for this endeavor came from a thought-provoking [video](https://www.youtube.com/watch?v=1g1HCYTX3Rg) by Code Bullet, in which he utilized an algorithm to solve the task at hand. I sought to demonstrate that it is possible to achieve similar results using the NEAT (NeuroEvolution of Augmented Topologies) framework, thus driving my decision to create this project.
When run, it will automatically generate `checkpoints every 100 generations`. The base NEAT organization consists of `16 input neurons`, (the game board), and `2 output neurons`, dictating `up/down` and `left/right`. All other specifications are in `config.txt`. The `fitness function` is determined by the value of merges done by the AI, and then when the AI 'dies', the maximum block found on the board will be added to the fitness.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

You will need Python >= 3.10 or pypy3 installed. 
* Python 3.10
  Linux:
  ```sh
  sudo apt install python3.10
  ```
  Windows:
  [Link to Python for Windows download page](https://www.python.org/downloads/windows/)
  MacOS:
  [Link to Python for MacOS download page](https://www.python.org/downloads/macos/)
* PyPy3
  Linux:
  ```sh
  sudo add-apt-repository ppa:pypy/ppa
  sudo apt update
  sudo apt install pypy3
  ```
  Windows/MacOS:
  [Link to PyPy3's download page](https://pypy.org/download.html)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AnthonyClemens/NEAT-2048.git
   ```
3. Install required libraries
   ```sh
   pip3 install -r requirements.txt 
   ```
4. Run the project
   ```js
   python3 main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Other than just running `python3 main.py`, additional parameters have been added, such as `-nl`, which will ignore any checkpoints present in the folder. `-h` will run the program in headless mode, skipping the pygame visuals to just crunch numbers and moves stuck counter from 1s to 0.1s. `-n (num)` will set the number of generations to run, default is set to 20,000. However, this game is very difficult to automate with the NEAT algorithm, so normally very long 100k+ generations will be required due to the complexity.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/AnthonyClemens/NEAT-2048/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AnthonyClemens/NEAT-2048" alt="contrib.rocks image" />
</a>



<!-- CONTACT -->
## Contact
Anthony Clemens - [anthony.clemens831@gmail.com](mailto:anthony.clemens831@gmail.com)

Project Link: [https://github.com/AnthonyClemens/NEAT-2048](https://github.com/AnthonyClemens/NEAT-2048)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Code Bullet](https://www.youtube.com/@CodeBullet)
* [My wife, Marissa, for always supporting me]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AnthonyClemens/NEAT-2048.svg?style=for-the-badge
[contributors-url]: https://github.com/AnthonyClemens/NEAT-2048/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AnthonyClemens/NEAT-2048.svg?style=for-the-badge
[forks-url]: https://github.com/AnthonyClemens/NEAT-2048/network/members
[stars-shield]: https://img.shields.io/github/stars/AnthonyClemens/NEAT-2048.svg?style=for-the-badge
[stars-url]: https://github.com/AnthonyClemens/NEAT-2048/stargazers
[issues-shield]: https://img.shields.io/github/issues/AnthonyClemens/NEAT-2048.svg?style=for-the-badge
[issues-url]: https://github.com/AnthonyClemens/NEAT-2048/issues
[commits-shield]: https://img.shields.io/github/commit-activity/t/AnthonyClemens/NEAT-2048?style=for-the-badge
[commits-url]: https://github.com/AnthonyClemens/NEAT-2048/commits
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/anthony-clemens831
