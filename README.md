# AirInstruments

Since the beginning of mankind humans have dreamt of two things: flying and playing air guitars with sound. Unfortunately, the Wright Brothers beat me to the former so I had to settle for rock and roll. 

https://user-images.githubusercontent.com/29150631/127755466-e66a46de-c45f-4c03-8f12-1c073bfb6810.mp4

# Usage
The application is extremely easy to use, simply stand in front of your webcam and pretend you're playing a guitar. (Note: only works for standard guitar-holding - *sorry left handers*!) 

### Command line
`python src/main.py`

Use `python src/main.py false` if you don't want your skeleton to be drawn.

### While running

You can type a number to change the instrument. Currently there are 4 instruments.

Press:
1. ukulele
2. bass
3. guitar
4. funk_guitar

# Setup

This project depends on FluidSynth as well as several Python packages.

## Downloading Project

Choose one of the following

Browser: https://github.com/SjDuque/AirInstruments/archive/refs/heads/main.zip

Command: `git clone https://github.com/SjDuque/AirInstruments.git`

## Python Packages:

This project uses mediapipe, opencv, and pyFluidSynth. I do recommend creating a new virtual environment but I'm not your parent so I can't make you do anything. 

### Creating a new environment
Open a terminal in the root directory of the project:

`python -m venv venv`

Windows: `.\venv\Scripts\activate`

Mac/Linux: `source venv/bin/activate`


### Using pip

`python -m pip install opencv-contrib-python mediapipe pyFluidSynth`

Links to packages:
* https://pypi.org/project/mediapipe/
* https://pypi.org/project/pyFluidSynth/
* https://pypi.org/project/opencv-python/

*Note: While you could just use opencv-python, I highly recommend using opencv-contrib-python because in my experience it causes less issues.*

## Linux

~~Use your package manager of choice. You must be bright if you're using linux, find it our yourself.~~

~~For example, if you're using Ubuntu:~~

```
sudo apt-get update
sudo apt-get install fluidsynth
```

~~At this point you should be able to run the program.~~

I can't even get FluidSynth to work on Ubuntu so I recommend using Windows or MacOS. 

## MacOS

Use Homebrew to install FluidSynth. If you don't have Homebrew, shame on you.

`brew install fluid-synth`

After this you should be good to run the program.

https://brew.sh/

## Windows

### The issues

Unfortunately, Windows users have to go through more suffering than they already endure from using a ~~terrible~~ great operating system.

In order to use FluidSynth you have to install the zip file and add the bin to your PATH variable. Additionally, the most recent version of FluidSynth breaks the pyFluidSynth package because pyFluidSynth looks for an outdated file.

### Easier Method

This requires you to install an older version of FluidSynth. If you care about the newest version then go to the harder method. 

* Easier: https://github.com/FluidSynth/fluidsynth/releases/tag/v2.1.8

* Harder: https://github.com/FluidSynth/fluidsynth/releases 

1. Download the zip the zip of your choice.
2. Extract the files to your directory of choice (I chose `C:/Users/\*name*/fluidsynth`)
3. Add the bin to your PATH variable (Ex. I chose added `C:/Users/\*name*/fluidsynth/bin`)
4. Sanity check: type `fluidsynth` into a ***new***  terminal (Close any terminal that you have open. If you have VS Code open then close that, too. It will save you from losing your mind, trust me.)
5. At this point, if you installed v2.1.8 you should be able to run the program.

### Harder method

1. Complete the easier method.
2. In the virtual environment that you created earlier, find fluidsynth.py and open it in your editor of choice. (`.\venv\Lib\site-packages\fluidsynth.py`)
3. Find the following code block (Line 36):
```python
lib = find_library('fluidsynth') or \
    find_library('libfluidsynth') or \
    find_library('libfluidsynth-2') or \
    find_library('libfluidsynth-1')
```
and add `find_library('libfluidsynth-3') or \`, changing the code to:
```python
lib = find_library('fluidsynth') or \
    find_library('libfluidsynth') or \
    find_library('libfluidsynth-3') or \
    find_library('libfluidsynth-2') or \
    find_library('libfluidsynth-1')
```
4. At this point you should be able to run the program.

# Future Plans

The following is in the no particular order of importance.

1. I plan on implementing custom songs in the future, similar to guitar hero. The notes will play in order, the user only has to strum.

2. Add ability to change limbs. I understand that not everyone can strum with their right arm, or you even want to. Eventually, you will be able to strum with any body part you desire. 

3. Removing the necessity of FluidSynth. It works just fine but I'd rather use TinySoundFont so I don't have to set any paths or change the package files.

4. Mobile App
