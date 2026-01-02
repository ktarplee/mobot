# Calvin's mobot

## Setup

Run `raspi-config` to enable the i2c interface which is needed for the servo controller.

Install direnv and set it up

```bash
sudo apt install direnv
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
```

Clone the repo and enable envrc

```bash
git clone git@github.com:ktarplee/mobot.git
cd mobot
```

```bash
sudo apt install -y python3-picamera2
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Running

```bash
uv sync --extra=rpi
uv run terminal.py
uv run sonar4.py
```

## GnuPlot

Run `uv run sonar4.py > data.csv` then run `gnuplot` to plot the data

```bash
gnuplot -p plot/theta.gp
gnuplot -p plot/cartesian.gp
```

## Camera

Install camera drivers with `sudo apt install libraspberrypi-bin`.

Then capture images with `rpicam-jpeg --output ~/test.jpg`.

[How to stream RPI camera to a web page](https://raspberrytips.com/how-to-live-stream-pi-camera/).

## Troubleshooting

```bash
sudo apt-get install i2c-tools
i2cdetect -y 1
```

Ensure that 0x40 shows up.
