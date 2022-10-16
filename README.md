# GPS Convert

<!-- ABOUT THE PROJECT -->
## About The Project

This GPS Convert tool written in Python converts GPS coordinates from decimal degrees to DDM format (`dd,mm.mmmmH`)

Decimal degree coordinates is what you can get from Google Maps, for example: 

![alt text](https://github.com/anairinac/gpsconvert/blob/main/images/decimaldegrees.png?raw=true)

## Fun Fact

This tool was initially created because I wanted to use Adobe Bridge to organize my photos, but when trying to create a template to apply GPS metadata to my photos with the tool, I found out my Google Maps location information was on a different format than the one Bridge recognizes (DDM).

In the future, I think it would be cool to add other GPS formats for more conversions to happen.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You just need to have [Python](https://www.python.org/) installed.


### Installation

You can start using this tool to convert GPS coordinates between formats.

1. Go to your Terminal of choice.
2. Clone the repository with HTTPS:
   ```sh
   git clone https://github.com/anairinac/gpsconvert.git
   ```
3. Or with SSH:
    ```sh
    git clone git@github.com:anairinac/gpsconvert.git
    ```
4. Change into the repository: `cd gpsconvert`


<!-- USAGE EXAMPLES -->
## Usage

1. Run the tool: 
    ```sh
    python3 gpsconvert.py
    ```
2. Enter your latitude when prompted and click ENTER.
3. Enter your longitude when prompted and click ENTER.

Depending on how you have Python configured on your machine, you would run it with `python` or `python3`.


The whole process should look like this:

![](https://github.com/anairinac/gpsconvert/images/gpsconvert.gif)


<!-- CONTRIBUTING -->
## Contributing

I created this with the idea of sharing it with anyone who might need these kind of GPS conversions, and any contribution is appreciated as well.

Please fork the repo and create a pull request in case you have any suggestions, improvements or new features that you thought of. 

1. Fork the repo.
2. Create a branch for your repo: 
    ```sh
    git checkout -b feature/AwesomeFeature
    ```
3. Add your changes: 
    ```sh
    git commit -m "Adding an awesome feature"
    ```
4. Push to your branch: 
    ```sh
    git push origin feature/AwesomeFeature
    ```
5. Open your Pull Request :)


<!-- CONTACT -->
## Contact

Irina Calvo - [@irinacalvoc](https://twitter.com/irinacalvoc)

Project Link: [https://github.com/anairinac/gpsconvert](https://github.com/anairinac/gpsconvert)


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [@othneildrew](https://github.com/othneildrew) - For the [README template](https://github.com/othneildrew/Best-README-Template)